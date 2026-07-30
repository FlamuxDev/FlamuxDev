<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--  ABDULRAHMAN FARAJ · FlamuxDev — AI Agent Engineer                      -->
<!--  Banner, request-path diagram, telemetry band and footer are            -->
<!--  hand-authored animated SVGs in /assets. No template, no render service.-->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<img src="assets/banner.svg" width="100%" alt="Abdulrahman Faraj — AI Agent Engineer" />

<br/>

I build **AI agents that carry real transactions** — booking a clinic appointment over WhatsApp, selling a merchant's catalog in Arabic, answering from a private knowledge base with tools attached. Multi-tenant, in production, mostly shipped solo. The interesting part is never the prompt; it's everything wrapped around it: retrieval that ranks correctly, tool loops that stay bounded, guards that stop an agent from claiming work it never did, and deploys that can be undone.

<img src="assets/metrics.svg" width="100%" alt="Measured results: recall@10 0.861, 26ms warm p50, 92 REST endpoints, 68/68 tests, 11-agent council, 36 tables" />

<img src="assets/rule.svg" width="100%" alt="" />

## &nbsp;`01`&nbsp;&nbsp;THE REQUEST PATH

<img src="assets/agent-loop.svg" width="100%" alt="Agent request path: ingress, guard, retrieve, reason, act, verify, stream" />

Every stage below is code I own in a running system — not a reference architecture.

| # | Stage | What it actually means in my systems |
|:--|:--|:--|
| `01` | **Ingress** | Meta webhook → HMAC signature verification → debounce + idempotency key, so a redelivered message never double-books a slot |
| `02` | **Guard** | Prompt-injection corpus run as a quality gate · per-agent origin allowlists (a state-changing request with no `Origin` is rejected) · tool output wrapped in trust guards before it re-enters the prompt |
| `03` | **Retrieve** | pgvector HNSW cosine **in parallel with** FTS (SQLite FTS5 trigram over normalised Arabic), fused by **RRF** · embeddings refreshed differentially by content hash · two-layer + semantic cache |
| `04` | **Reason** | Bounded Gemini tool-loop, three-layer context manager, per-run token budgets, and a no-LLM fallback path that still answers when the model is down |
| `05` | **Act** | Per-agent **MCP** servers (cached clients, encrypted headers) · domain tools (availability, booking, catalog, pricing) · connectors (Odoo, Dynatrace, Splunk) · automatic provider failover |
| `06` | **Verify** | A server-side **integrity guard**: the agent cannot *claim* an action it did not actually perform. Structural validators reject malformed sections and re-prompt correctively |
| `07` | **Stream** | Socket.IO fan-out over a Redis adapter (cluster-safe) and Postgres `NOTIFY` for live agent progress in the UI |

> [!NOTE]
> Most of the repositories behind this page are **private client/product code**. What is public here is the architecture, the measurements, and the engineering practice — not the source.

<img src="assets/rule.svg" width="100%" alt="" />

## &nbsp;`02`&nbsp;&nbsp;SYSTEMS

| System | What it is | Surface | State |
|:--|:--|:--|:--|
| **Botify + Campify** | Multi-tenant AI agent & customer-engagement platform: RAG over private knowledge, MCP tool-calling, voice, live human handoff, campaign automation | 7-package monorepo · widget · 2 dashboards | `PRODUCTION` |
| **Mawid AI** <sub>موعد</sub> | WhatsApp booking agent for Gulf clinics, salons and workshops — books, reschedules, cancels and reminds, in Arabic and English | `gomawid.com` | `PRODUCTION` |
| **Sham v2** <sub>شمسي</sub> | Arabic educational discovery agent — schools, teachers, events across Jordan, over chat, WhatsApp and voice | API · WhatsApp · voice · MCP | `PRODUCTION` |
| **Luma Architect** | An orchestration engine where **11 specialised agents** turn a plain-language idea into a full engineering blueprint — with a debate round and an arbitration agent | Worker + web | `IN BUILD` |
| **Tamm** <sub>تمّ</sub> | WhatsApp commerce for GCC merchants — an Arabic sales agent on top of a multi-tenant commerce engine | NestJS API · Next.js web | `IN BUILD` |
| **Ray** | Cross-platform desktop agent — multimodal chat, workspace files, ~85 skills, MCP connectors, cron routines, artifacts canvas | Tauri desktop (Linux/Windows) | `PRE-MVP` |

<br/>

<details>
<summary><b>&nbsp;⟩&nbsp; Botify — the hot path, and what makes it survive contact with tenants</b></summary>

<br/>

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#1A0F09','primaryTextColor':'#FDBA74','primaryBorderColor':'#EA580C','lineColor':'#9A3412','secondaryColor':'#231309','tertiaryColor':'#0A0A0B','fontFamily':'ui-monospace, monospace','fontSize':'13px'}}}%%
flowchart LR
    W[Embeddable widget<br/>Shadow DOM · no framework] --> API[Express API<br/>REST + Socket.IO]
    D[Tenant dashboard] --> API
    API --> ORG{Org scope + RBAC<br/>suspension kill-switch}
    ORG --> RAG[(pgvector HNSW<br/>cosine · strict grounding)]
    ORG --> TL[5 tool loaders<br/>in parallel with retrieval]
    RAG --> LOOP[Gemini tool-loop<br/>injection-guarded · bounded]
    TL --> LOOP
    LOOP --> FLT[Stream marker filter]
    FLT --> IO((Socket.IO fan-out<br/>Redis adapter))
    LOOP --> Q[[BullMQ workers<br/>ingestion · analysis · outreach]]
    Q --> QA[Post-conversation<br/>AI quality analysis]
```

- **Multi-tenancy is the schema, not a filter** — `Organization` is the tenant root, every query is org-scoped, RBAC with string permissions, a separate platform-admin identity, and an org suspension kill-switch.
- **Knowledge ingestion** — PDF/DOCX/HTML/crawler → chunking → batched Gemini embeddings → HNSW index, with strict-grounding mode and knowledge-conflict detection.
- **Security posture** — AES-256-GCM for tenant secrets at rest, HMAC-signed private media URLs, Redis-backed rate limits, sanitised widget markdown.
- **Deploys that can be undone** — a migration guard that refuses diffs containing `DROP`, a pre-deploy `pg_dump` snapshot, migration + client regeneration on the server, then a `/api/ready` health gate with a documented rollback.

</details>

<details>
<summary><b>&nbsp;⟩&nbsp; Mawid AI — an agent that is allowed to touch the calendar</b></summary>

<br/>

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#1A0F09','primaryTextColor':'#FDBA74','primaryBorderColor':'#EA580C','lineColor':'#9A3412','secondaryColor':'#231309','tertiaryColor':'#0A0A0B','fontFamily':'ui-monospace, monospace','fontSize':'13px'}}}%%
flowchart TD
    M[Meta webhook] --> SIG{App-secret<br/>signature check}
    SIG --> RES[Resolve org by number<br/>store · transcribe voice]
    RES --> CTX[Load org context<br/>services · staff · hours · policies · KB]
    CTX --> AG[Gemini 2.5 Flash agent<br/>Vercel AI SDK · tools]
    AG --> TOOLS[search availability · book<br/>reschedule · cancel · quote]
    TOOLS --> LOCK[[Slot locking<br/>concurrency-safe booking]]
    LOCK --> DB[(Postgres + pgvector<br/>Drizzle · 36 tables)]
    AG --> GRD{Integrity guard<br/>claim ≟ actual effect}
    GRD -- mismatch --> FIX[Correct the reply]
    GRD -- ok --> OUT[Reply on WhatsApp]
```

- **The dependency graph is enforced by tooling.** Four workspaces — `core → backend → ai → web`, one direction only. A `backend → ai` import is an **ESLint error**, not a code-review argument. That is what let the frontend, backend and AI tracks move without breaking each other.
- **`core` is a pure leaf** — date/timezone/scheduling/rules logic with no I/O, which is why the booking rules are actually testable.
- **The box never builds.** CI builds the Docker image and pushes it to GHCR; the server only pulls and restarts. Rollback is re-deploying a known-good SHA.
- Baseline that must stay green before merge: `tsc` clean · **68/68 tests** · production build OK.

</details>

<details>
<summary><b>&nbsp;⟩&nbsp; Sham v2 — the rewrite, and the numbers that justified it</b></summary>

<br/>

Design principle: **model-driven understanding, data-derived vocabulary, truth from SQL.**

| | Previous system | **Sham v2** |
|:--|:--|:--|
| Domain vocabulary | ~400 lines of hard-coded synonyms, types and neighbourhoods | **Live gazetteer** derived from the database at boot and after each sync — a new word in the data works with no code change |
| Query understanding | Rules + regex first, LLM for the rare case | **Structured-output Gemini first** (temp 0, few-shot, enums), version-keyed two-layer cache, **plus a non-LLM fallback that keeps working when the model fails** |
| Search | KNN + FTS + RRF | Same proven core, but understanding and embedding run **in parallel**, with background completion on timeout |
| Stability | A tool error killed the reply | Per-tool and per-call timeouts, exponential backoff, fallback model, circuit breaker, single-flight |

**Measured against the previous live system, not against itself:** recall@10 `0.77 → 0.861` · warm p50 `~60ms → ~26ms` · aggregate accuracy held at `100%` · 98 tests · 95-query golden eval suite.

The rewrite kept the published API contract **byte-for-byte** — web, mobile and the voice agent kept working with zero changes.

</details>

<details>
<summary><b>&nbsp;⟩&nbsp; Luma Architect — eleven agents, a debate round, and an arbiter</b></summary>

<br/>

An idea in plain language goes in; a complete engineering document comes out — requirements, architecture, database, API, interfaces, security, testing, deployment. Eleven specialised agents, each named after a computing pioneer, each with one strict role.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#1A0F09','primaryTextColor':'#FDBA74','primaryBorderColor':'#EA580C','lineColor':'#9A3412','secondaryColor':'#231309','tertiaryColor':'#0A0A0B','fontFamily':'ui-monospace, monospace','fontSize':'13px'}}}%%
flowchart TD
    T1[Turing · analysis and plan] --> G[Grove · business]
    G --> L[Lovelace · requirements]
    L --> B[Brooks · architecture]
    L --> C[Codd · database]
    L --> F[Fielding · API]
    L --> N[Norman · interfaces]
    B --> D[Diffie · security]
    C --> D
    F --> D
    N --> D
    D --> H[Hopper · testing]
    H --> V[Torvalds · operations]
    V --> M{Debate<br/>cross-review}
    M --> T2[Turing · arbitration]
    T2 --> K[Knuth · final assembly]
```

- **The four-way fan-out** (architecture / database / API / interfaces) runs **in parallel** after requirements — the single biggest latency win in the pipeline.
- **Jobs are claimed atomically** with `FOR UPDATE SKIP LOCKED`, so two workers can never run the same blueprint.
- **Every state change is broadcast** — a row in the message log plus Postgres `NOTIFY`, so the user watches the council work live instead of staring at a spinner.
- **Validators before persistence** — per-agent structural validators, a Mermaid gate, a consistency checker, and a corrective re-prompt that feeds the rejection back to the agent as guidance.
- **Cost is a design constraint** — development runs against a mock provider returning fixtures (zero cost, offline); real full-pipeline runs are scheduled and budgeted.

I also lead the AI team building it: four pairs with explicit ownership, a two-review merge gate, and a stated definition of done.

</details>

<details>
<summary><b>&nbsp;⟩&nbsp; Tamm & Ray — commerce agent, and an agent on the desktop</b></summary>

<br/>

**Tamm (تمّ)** — an Arabic sales agent over WhatsApp on top of a multi-tenant commerce engine: browsing, cart, delivery, ordering and *"where is my order?"*. NestJS + Prisma, **92 REST endpoints** generated into an OpenAPI document and a ready Postman collection. The e2e suite boots its own embedded Postgres and runs every case against real HTTP and a real database — it is the merge gate. The agent is exercised through a **scripted fake LLM** so the suite stays deterministic, offline and free; a separate live flag verifies the real Gemini wiring end to end (prompt → function calling → tools → a placed order).

**Ray** — a desktop agent for Linux and Windows: streamed multimodal chat with vision, voice in and out, a workspace file tree with a live FS watcher, an artifacts canvas that live-renders HTML/SVG/Mermaid in a sandbox, ~85 bundled skills, 7 MCP connectors, cron-scheduled routines, a Spotlight-style global launcher, and full Arabic + RTL. Tauri 2 + React 19 over a Python agent core; Windows MSI/NSIS/portable builds packaged in CI.

</details>

<img src="assets/rule.svg" width="100%" alt="" />

## &nbsp;`03`&nbsp;&nbsp;HOW I ENGINEER

<table>
<tr>
<td width="50%" valign="top">

**`Determinism around a non-deterministic core`**

The agent is tested through a scripted fake LLM, so the suite is offline, free and repeatable. A separate opt-in flag exercises the real provider wiring. AI code that can only be tested by talking to a model is AI code that is never tested.

**`Eval before opinion`**

Golden-query suites with `recall@10` and latency tracked against the **previous live baseline** — a rewrite ships when the numbers say so, not when it feels faster.

**`Mock-first, cost-aware`**

Default provider is a mock returning fixtures: zero-cost, offline, no key in anyone's `.env`. Real runs are scheduled, budgeted and logged.

</td>
<td width="50%" valign="top">

**`Architecture enforced by tooling`**

Package boundaries live in `tsconfig` paths and ESLint `no-restricted-imports`. A backward import fails the build instead of starting a debate.

**`Deploys that can be undone`**

Migration guard against destructive diffs · pre-deploy database snapshot · health gate before traffic · images built in CI and *pulled* by the server · rollback is one known-good SHA.

**`Failure is an input, not an incident`**

Per-call timeouts, exponential backoff, circuit breakers, single-flight, provider failover, and a degraded path that still answers when the model is unavailable.

</td>
</tr>
</table>

<img src="assets/rule.svg" width="100%" alt="" />

## &nbsp;`04`&nbsp;&nbsp;STACK

**`AI & AGENTS`**

<img src="https://img.shields.io/badge/Gemini_2.5-0A0A0B?style=flat-square&logo=googlegemini&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/Vercel_AI_SDK-0A0A0B?style=flat-square&logo=vercel&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/LangChain-0A0A0B?style=flat-square&logo=langchain&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/MCP-0A0A0B?style=flat-square&logo=anthropic&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/pgvector_·_HNSW-0A0A0B?style=flat-square&logo=postgresql&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/RRF_hybrid_retrieval-0A0A0B?style=flat-square&logo=databricks&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/ElevenLabs_voice-0A0A0B?style=flat-square&logo=elevenlabs&logoColor=F97316&labelColor=0A0A0B" />

**`BACKEND & DATA`**

<img src="https://img.shields.io/badge/TypeScript-0A0A0B?style=flat-square&logo=typescript&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/Node_≥20-0A0A0B?style=flat-square&logo=nodedotjs&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/NestJS-0A0A0B?style=flat-square&logo=nestjs&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/Express-0A0A0B?style=flat-square&logo=express&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/Python_≥3.11-0A0A0B?style=flat-square&logo=python&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/PostgreSQL-0A0A0B?style=flat-square&logo=postgresql&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/Prisma_·_Drizzle-0A0A0B?style=flat-square&logo=prisma&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/Redis_·_BullMQ-0A0A0B?style=flat-square&logo=redis&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/SQLite_·_FTS5-0A0A0B?style=flat-square&logo=sqlite&logoColor=F97316&labelColor=0A0A0B" />

**`FRONTEND & DELIVERY`**

<img src="https://img.shields.io/badge/Next.js_16-0A0A0B?style=flat-square&logo=nextdotjs&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/React_19-0A0A0B?style=flat-square&logo=react&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/Tailwind_v4-0A0A0B?style=flat-square&logo=tailwindcss&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/Tauri_2-0A0A0B?style=flat-square&logo=tauri&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/Turborepo_·_pnpm-0A0A0B?style=flat-square&logo=turborepo&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/Docker-0A0A0B?style=flat-square&logo=docker&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/GitHub_Actions_·_GHCR-0A0A0B?style=flat-square&logo=githubactions&logoColor=F97316&labelColor=0A0A0B" />
<img src="https://img.shields.io/badge/AWS_EC2_·_Caddy_·_PM2-0A0A0B?style=flat-square&logo=amazonwebservices&logoColor=F97316&labelColor=0A0A0B" />

<img src="assets/rule.svg" width="100%" alt="" />

## &nbsp;`05`&nbsp;&nbsp;CURRENTLY

```yaml
shipping:
  - Mawid AI      → onboarding Gulf tenants onto WhatsApp Cloud API
  - Botify        → tool-calling depth: more connectors, tighter grounding
  - Luma Architect→ first full eleven-agent run against real providers

studying:
  - agent evaluation — scoring tool-use traces, not just final answers
  - per-user sandboxed compute (Firecracker · gVisor · E2B)
  - on-device and edge inference for latency-bound Arabic voice

principle: "an agent you cannot measure is a demo, not a product"
```

<img src="assets/rule.svg" width="100%" alt="" />

## &nbsp;`06`&nbsp;&nbsp;CONTACT

<a href="mailto:abdfaraj.dev@gmail.com"><img src="https://img.shields.io/badge/Email-0A0A0B?style=for-the-badge&logo=gmail&logoColor=F97316&labelColor=0A0A0B" height="34" /></a>
<a href="https://linkedin.com/in/abd-ulrahman-faraj-io"><img src="https://img.shields.io/badge/LinkedIn-0A0A0B?style=for-the-badge&logo=linkedin&logoColor=F97316&labelColor=0A0A0B" height="34" /></a>
<a href="https://gomawid.com"><img src="https://img.shields.io/badge/gomawid.com-0A0A0B?style=for-the-badge&logo=googlechrome&logoColor=F97316&labelColor=0A0A0B" height="34" /></a>
<a href="https://shamsieh.ai"><img src="https://img.shields.io/badge/shamsieh.ai-0A0A0B?style=for-the-badge&logo=vercel&logoColor=F97316&labelColor=0A0A0B" height="34" /></a>

> [!TIP]
> The fastest way to a useful conversation: send me the problem in one paragraph — the constraint, the traffic, and what "correct" means for you.

<br/>

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=FlamuxDev&show_icons=true&count_private=true&hide_border=true&hide_title=true&title_color=F97316&icon_color=EA580C&text_color=A8A29E&bg_color=0A0A0B" height="150" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=FlamuxDev&layout=compact&hide_border=true&hide_title=true&title_color=F97316&text_color=A8A29E&bg_color=0A0A0B&langs_count=8" height="150" />

</div>

<br/>

<img src="assets/footer.svg" width="100%" alt="أنظمة وكلاء تعمل في الإنتاج — agent systems that run in production" />
