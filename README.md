<div align="center">

<a href="https://github.com/FlamuxDev">
  <img src="assets/hero.svg" width="100%" alt="Abdulrahman Faraj — AI Agent Systems Engineer" />
</a>

<br />

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=20&duration=2800&pause=900&color=FF6B35&center=true&vCenter=true&width=820&lines=AI+Agent+Systems+Engineer;Building+systems+around+the+model;Reasoning+%E2%86%92+Tools+%E2%86%92+Execution+%E2%86%92+Verification;Measured.+Grounded.+Reversible." />

<br /><br />

<a href="https://github.com/FlamuxDev">
  <img src="https://img.shields.io/github/followers/FlamuxDev?style=for-the-badge&logo=github&label=FOLLOWERS&labelColor=111111&color=FF6B35" />
</a>
<a href="https://github.com/FlamuxDev?tab=repositories">
  <img src="https://img.shields.io/github/stars/FlamuxDev?style=for-the-badge&logo=github&label=STARS&labelColor=111111&color=FF6B35" />
</a>
<a href="mailto:abdfaraj.dev@gmail.com">
  <img src="https://img.shields.io/badge/EMAIL-CONNECT-111111?style=for-the-badge&logo=gmail&logoColor=white&color=FF6B35" />
</a>

</div>

---

<div align="center">

### I DON'T BUILD CHATBOTS.

## I BUILD THE SYSTEM AROUND THE MODEL.

*Clinics booked over WhatsApp · merchants selling in Arabic · answers grounded in private knowledge — live traffic, not demos.*

</div>

<br />

<table align="center">
<tr>
<td align="center" width="25%">

### THINK

Reasoning
Planning
Context
Memory

</td>

<td align="center" width="25%">

### ACT

Tools
APIs
Agents
Automation

</td>

<td align="center" width="25%">

### VERIFY

Evaluation
Traces
Policies
Integrity

</td>

<td align="center" width="25%">

### LEARN

Feedback
History
Signals
Adaptation

</td>
</tr>
</table>

---

# `01` · ENGINEERING

I work on the infrastructure that turns probabilistic models into **reliable software systems**.

My interest is not simply getting a model to produce a good answer.

It is making the entire system around that model:

```text
observable
debuggable
measurable
recoverable
reversible
composable
```

---

# `02` · THE WAY I BUILD

```text
                           ┌──────────────────────┐
                           │        USER          │
                           └──────────┬───────────┘
                                      │
                                      ▼
                           ┌──────────────────────┐
                           │       CONTEXT        │
                           │ memory · state · RAG │
                           └──────────┬───────────┘
                                      │
                                      ▼
                    ┌────────────────────────────────┐
                    │             MODEL              │
                    │                                │
                    │ reasoning · planning · choice │
                    └───────────────┬────────────────┘
                                    │
                    ┌───────────────┼────────────────┐
                    │               │                │
                    ▼               ▼                ▼
                 MEMORY           TOOLS            POLICY
                    │               │                │
                    └───────────────┼────────────────┘
                                    ▼
                           ┌──────────────────────┐
                           │      EXECUTION       │
                           │ jobs · APIs · state  │
                           └──────────┬───────────┘
                                      │
                                      ▼
                           ┌──────────────────────┐
                           │    VERIFICATION      │
                           │ effects ≠ claims     │
                           └──────────┬───────────┘
                                      │
                                      ▼
                           ┌──────────────────────┐
                           │       LEARNING       │
                           │ traces · feedback    │
                           └──────────┬───────────┘
                                      │
                                      └───────────────► NEXT RUN
```

> **The model is a component. The architecture is the product.**

---

# `03` · ENGINEERING PRINCIPLES

<table>
<tr>
<td width="50%" valign="top">

### DETERMINISM AROUND UNCERTAINTY

The model can be probabilistic.

The infrastructure around it should not be.

Tests, state transitions, contracts, retries and failure handling should remain predictable.

</td>

<td width="50%" valign="top">

### EVAL BEFORE OPINION

I prefer traces and measurements over intuition.

```text
golden cases
      ↓
tool-use traces
      ↓
metrics
      ↓
regression
      ↓
ship / reject
```

</td>
</tr>

<tr>
<td width="50%" valign="top">

### FAILURE IS A STATE

Timeouts, provider failures, partial execution and malformed model output are not edge cases.

They are part of the architecture.

</td>

<td width="50%" valign="top">

### EVERYTHING SHOULD BE REVERSIBLE

```text
change
  ↓
snapshot
  ↓
health gate
  ↓
deploy
  ↓
verify
  ↓
rollback
```

A system without a recovery path is unfinished.

</td>
</tr>
</table>

---

# `04` · WHAT I WORK ON

```text
┌──────────────────────────────────────────────────────────┐
│                    AI AGENT SYSTEMS                      │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Agent Runtime                                           │
│  ├── state machines                                      │
│  ├── execution loops                                     │
│  ├── decision systems                                    │
│  └── long-running tasks                                  │
│                                                          │
│  Context Engineering                                     │
│  ├── memory                                              │
│  ├── retrieval                                           │
│  ├── context assembly                                    │
│  └── user state                                          │
│                                                          │
│  Tool Infrastructure                                     │
│  ├── tool calling                                        │
│  ├── connector lifecycle                                 │
│  ├── permissions                                         │
│  └── external systems                                    │
│                                                          │
│  Reliability                                             │
│  ├── evaluation                                          │
│  ├── observability                                       │
│  ├── retries / backoff                                   │
│  ├── failover                                            │
│  └── integrity checks                                    │
│                                                          │
│  Multi-Agent Systems                                     │
│  ├── specialization                                      │
│  ├── orchestration                                       │
│  ├── delegation                                          │
│  └── agent-to-agent workflows                            │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

# `05` · MY DEVELOPMENT LOOP

```text
          ┌─────────────┐
          │   RESEARCH  │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │   SPECIFY   │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │   DESIGN    │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │   BUILD     │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │   TEST      │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │   EVALUATE  │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │   SHIP      │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │   LEARN     │
          └──────┬──────┘
                 │
                 └───────────────► RESEARCH
```

### `BUILD → MEASURE → VERIFY → SHIP → LEARN`

---

# `06` · NOW

```yaml
lines:     onboarding Gulf tenants onto WhatsApp Cloud API · deepening tool-calling in Botify
building:  Luma Architect — first full eleven-agent council run against real providers
studying:  agent evaluation over tool-use traces · sandboxed compute · edge Arabic voice
```

---

# `07` · STACK

<div align="center">

<img src="https://skillicons.dev/icons?i=ts,python,nodejs,nestjs,express,postgres,redis,prisma,nextjs,react,tailwind,docker,aws,githubactions&perline=7" />

<br /><br />

<img src="https://skillicons.dev/icons?i=git,github,linux,bash,vscode&perline=5" />

</div>

<br />

<div align="center">

`TypeScript` · `Python` · `PostgreSQL` · `Redis` · `Prisma`
`Next.js` · `React` · `Docker` · `AWS` · `GitHub Actions`
`LLMs` · `RAG` · `MCP` · `Tool Calling` · `Multi-Agent Systems`

</div>

---

# `08` · AI SYSTEM MAP

```mermaid
flowchart LR
    U[USER] --> C[CONTEXT]
    C --> M[MODEL]

    M --> D{DECISION}

    D -->|message| R[RESPONSE]
    D -->|tool| T[TOOL]
    D -->|delegate| A[AGENT]
    D -->|approval| P[POLICY]
    D -->|complete| X[VERIFIED RESULT]

    T --> E[EXECUTION]
    A --> E
    P --> E

    E --> V[VERIFICATION]
    V --> L[LEARNING]
    L --> S[STATE]
    S --> C
```

---

# `09` · SIGNALS

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=FlamuxDev&show_icons=true&count_private=true&hide_border=true&rank_icon=github&title_color=EAEAEA&icon_color=FF6B35&text_color=9CA3AF&bg_color=00000000" height="170" />

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=FlamuxDev&layout=compact&hide_border=true&title_color=EAEAEA&text_color=9CA3AF&bg_color=00000000&langs_count=8" height="170" />

</div>

<br />

<div align="center">

<img src="https://streak-stats.demolab.com?user=FlamuxDev&theme=transparent&hide_border=true&ring=FF6B35&fire=FF6B35&currStreakLabel=EAEAEA&sideLabels=9CA3AF&dates=6B7280" width="75%" />

</div>

---

# `10` · CONTRIBUTIONS

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=FlamuxDev&bg_color=00000000&color=9CA3AF&line=FF6B35&point=EAEAEA&area=true&hide_border=true" width="100%" />

<br />

<img src="https://raw.githubusercontent.com/FlamuxDev/FlamuxDev/output/github-contribution-grid-snake-dark.svg" width="100%" />

</div>

---

# `11` · PRINCIPLE

<div align="center">

## “An agent you cannot measure is a demo, not a product.”

<br />

`OBSERVE`  `→`  `MEASURE`  `→`  `VERIFY`  `→`  `IMPROVE`

<br /><br />

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=16&duration=3500&pause=1200&color=9CA3AF&center=true&vCenter=true&width=720&lines=Build+systems.+Not+just+prompts.;Make+failure+observable.;Make+change+reversible.;Make+AI+operational." />

</div>

---

<div align="center">

### ABDULRAHMAN FARAJ · عبد الرحمن فرج · 2026

*الأنظمة الحيّة لا تنام — the lines never sleep.*

[GitHub](https://github.com/FlamuxDev) ·
[LinkedIn](https://linkedin.com/in/abd-ulrahman-faraj-io) ·
[Website](https://gomawid.com)

</div>
