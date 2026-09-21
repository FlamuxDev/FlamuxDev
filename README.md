<div align="center">

# ABDULRAHMAN FARAJ

### AI Agent Systems Engineer

**I build AI agents that survive contact with production.**

*measured · grounded · reversible*

<br />

[![GitHub](https://img.shields.io/badge/GitHub-FlamuxDev-111111?style=flat-square\&logo=github\&logoColor=white)](https://github.com/FlamuxDev)
[![Email](https://img.shields.io/badge/Email-abdfaraj.dev%40gmail.com-111111?style=flat-square\&logo=gmail\&logoColor=white)](mailto:abdfaraj.dev@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abdulrahman_Faraj-111111?style=flat-square\&logo=linkedin\&logoColor=white)](https://linkedin.com/in/abd-ulrahman-faraj-io)

</div>

<br />

> **An agent you cannot measure is a demo, not a product.**

---

## CURRENTLY

```text
FOCUS
────────────────────────────────────────────────────────────
Botify       → onboarding Gulf tenants onto WhatsApp Cloud API
             → deepening production tool-calling

Luma         → building Luma Architect
             → running the first full eleven-agent council
               against real providers

RESEARCH     → agent evaluation over tool-use traces
             → sandboxed compute
             → edge Arabic voice
```

---

## WHAT I BUILD

I work on the layer between **LLMs and real systems**.

Not just prompts.
Not just chat interfaces.

I design agents with:

```text
memory
    ↓
planning
    ↓
tool use
    ↓
state
    ↓
execution
    ↓
verification
    ↓
learning
```

The goal is simple:

**an agent that can act reliably when the environment is not simple.**

---

## ENGINEERING DOCTRINE

### 01 · Determinism around a non-deterministic core

LLMs are probabilistic.

Everything around them should not be.

Test infrastructure uses scripted fake models for
offline, free and repeatable verification, with explicit
opt-in paths for exercising real provider integrations.

---

### 02 · Eval before opinion

I prefer traces and measurements over intuition.

Golden-query suites, retrieval metrics, latency baselines,
tool-use evaluation and regression testing decide whether
a change ships.

**A rewrite ships when the numbers say it should.**

---

### 03 · Architecture enforced by tooling

Architectural rules should not live in documentation.

Package boundaries, TypeScript paths, lint rules and build
constraints make invalid dependencies fail automatically.

**The compiler should win the argument.**

---

### 04 · Failure is an input

Production agents will encounter:

```text
timeouts
rate limits
provider failures
partial tool execution
stale state
network errors
unexpected model output
```

Systems therefore need:

**timeouts · backoff · circuit breakers · failover · degraded paths**

The goal is not zero failure.

The goal is **controlled failure**.

---

### 05 · Reversible by default

Deployments should be easy to undo.

```text
migration guard
      ↓
pre-deploy snapshot
      ↓
health gate
      ↓
known-good SHA
      ↓
rollback
```

A production change without a recovery path is incomplete.

---

### 06 · No unbacked claims

An agent saying that something happened does not make it true.

Server-side integrity checks compare:

```text
claimed action
       ↕
actual system effect
```

before the result is allowed to become part of the user-facing response.

---

## SYSTEMS I'M BUILDING

### BOTIFY

**AI personal assistant agents for production environments.**

Multi-agent runtime infrastructure covering:

```text
agent runtime
memory
learning
tool calling
decisioning
approvals
automations
connectors
background execution
evaluation
```

The goal is not another chatbot.

It is an **agent that can actually operate.**

→ https://botifyarabia.ai/

---

### LUMA ARCHITECT

**Conversation → architecture → implementation**

An AI software-architecture system built around
multi-agent collaboration.

The experiment:

```text
user intent
     ↓
specialized agents
     ↓
architecture / research / implementation reasoning
     ↓
agent council
     ↓
validated engineering output
```

Currently being tested against real model providers.

---

## STACK

### LANGUAGES & RUNTIME

![TypeScript](https://img.shields.io/badge/TypeScript-111111?style=flat-square\&logo=typescript\&logoColor=3178C6)
![Python](https://img.shields.io/badge/Python-111111?style=flat-square\&logo=python\&logoColor=3776AB)
![Node.js](https://img.shields.io/badge/Node.js-111111?style=flat-square\&logo=node.js\&logoColor=5FA04E)

### BACKEND & DATA

![Postgres](https://img.shields.io/badge/PostgreSQL-111111?style=flat-square\&logo=postgresql\&logoColor=4169E1)
![Redis](https://img.shields.io/badge/Redis-111111?style=flat-square\&logo=redis\&logoColor=DC382D)
![Prisma](https://img.shields.io/badge/Prisma-111111?style=flat-square\&logo=prisma\&logoColor=2D3748)

### AI SYSTEMS

```text
Gemini 2.5
Vercel AI SDK
LangChain
MCP
pgvector
HNSW
RRF hybrid retrieval
ElevenLabs
```

### INFRASTRUCTURE

```text
Docker
AWS
GitHub Actions
Express
NestJS
Next.js
React
Tailwind
Tauri
```

---

## HOW I THINK ABOUT AGENTS

```text
              ┌───────────────┐
              │     MODEL     │
              └───────┬───────┘
                      │
              ┌───────▼───────┐
              │    DECISION   │
              └───────┬───────┘
                      │
          ┌───────────┼───────────┐
          │           │           │
      memory        tools       policy
          │           │           │
          └───────────┼───────────┘
                      │
              ┌───────▼───────┐
              │   EXECUTION   │
              └───────┬───────┘
                      │
              ┌───────▼───────┐
              │ VERIFICATION  │
              └───────┬───────┘
                      │
              ┌───────▼───────┐
              │    LEARNING   │
              └───────────────┘
```

The model is one component.

**The system around the model is the product.**

---

## SELECTED AREAS

`AI Agents` · `Agent Runtime` · `Tool Calling` · `Memory`
`Evaluation` · `RAG` · `Multi-Agent Systems`
`Automation` · `Production AI` · `Arabic AI`

---

## CONNECT

**Fastest way to have a useful conversation:**

Send one paragraph covering:

`the constraint · the traffic · what "correct" means`

**Email**
[abdfaraj.dev@gmail.com](mailto:abdfaraj.dev@gmail.com)

**Web**
https://gomawid.com/
https://shamsieh.ai/

**LinkedIn**
https://linkedin.com/in/abd-ulrahman-faraj-io

---

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=FlamuxDev&show_icons=true&count_private=true&hide_border=true&title_color=EAEAEA&icon_color=FF5722&text_color=9CA3AF&bg_color=00000000" height="160" />

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=FlamuxDev&layout=compact&hide_border=true&title_color=EAEAEA&text_color=9CA3AF&bg_color=00000000&langs_count=8" height="160" />

</div>

<br />

<div align="center">

`BUILD → MEASURE → VERIFY → SHIP → LEARN`

</div>
