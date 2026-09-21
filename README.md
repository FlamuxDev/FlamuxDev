# Abdulrahman Faraj · عبد الرحمن فرج

**AI agent engineer.** I take agents from demo to production — measured, grounded, and reversible.

> *An agent you cannot measure is a demo, not a product.*

---

### Now

```yaml
lines:     onboarding Gulf tenants onto WhatsApp Cloud API · deepening tool-calling in Botify
building:  Luma Architect — first full eleven-agent council run against real providers
studying:  agent evaluation over tool-use traces · sandboxed compute · edge Arabic voice
```

### How I keep agents safe in production

- **Determinism around a non-deterministic core** — scripted fake LLM for tests (offline, free, repeatable); a separate opt-in flag exercises real provider wiring.
- **Eval before opinion** — golden-query suites with `recall@10` and latency vs. the previous live baseline. A rewrite ships when the numbers say so.
- **Architecture enforced by tooling** — package boundaries in `tsconfig` paths and ESLint rules; a backward import fails the build, not a debate.
- **Deploys that can be undone** — migration guard · pre-deploy snapshot · health gate · rollback is one known-good SHA.
- **Failure is an input** — timeouts, backoff, circuit breakers, provider failover, and a degraded path that still answers when the model is down.
- **No unbacked claims** — a server-side integrity guard compares claimed actions against actual effects before a reply leaves the system.

### Stack

`Gemini 2.5` · `Vercel AI SDK` · `LangChain` · `MCP` · `pgvector + HNSW` · `RRF hybrid retrieval` · `ElevenLabs`
`TypeScript` · `NestJS` · `Python` · `PostgreSQL` · `Prisma / Drizzle` · `Redis + BullMQ`
`Next.js` · `React` · `Tailwind` · `Tauri` · `Docker` · `GitHub Actions` · `AWS EC2 + Caddy + PM2`

---

📫 **Fastest way to a useful conversation:** [abdfaraj.dev@gmail.com](mailto:abdfaraj.dev@gmail.com) — one paragraph: the constraint, the traffic, and what "correct" means for you.

🔗 [LinkedIn](https://linkedin.com/in/abd-ulrahman-faraj-io) · [gomawid.com](https://gomawid.com) · [shamsieh.ai](https://shamsieh.ai)
