# FP-Agent: Fingerprinting AI Browsing Agents

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: Claude (chat interface)
- **Model name + version, if known**: Claude Opus 4.8
- **Source access**: full text (provided as the arXiv PDF, incl. appendices)
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: Wang, E., Shafiq, Z., & Vekaria, Y. (2026). *FP-Agent: Fingerprinting AI Browsing Agents.* arXiv:2605.01247v1 [cs.CR], 2 May 2026. University of California, Davis. NSF awards 2138139, 2103439.
- **Source URL or path**: `arxiv.org/abs/2605.01247` (provided as `2605_01247v1.pdf`). Artifacts: code at `github.com/ethanbwang/fp-agent`; data at OSF (`osf.io/j6b5p`). URLs taken from the paper; confirm resolution before citing on site.
- **Date accessed**: 2026-06-06
- **Category**: academic
- **Evidence basis**: empirical-academic; empirical-operational (Cloudflare case study) — a controlled honey-site measurement study, with one section testing a live deployed defender (Cloudflare free bot management) against the same agents
- **Operational proximity**: `measured` (honey-site). The register places honey-site experiments at `measured` (cf. SRC-015), and this is a controlled honey-site measurement of real commercial AI agents plus an external check of a deployed defender. Nuance for framing distance, not a downgrade: the agents perform **benign** tasks, so it measures agent *traffic characteristics / detectability*, not abuse against a target. This is the **second `measured`-tier source** in the register and the same lab lineage as SRC-015 (Shafiq on both).
- **Tags**: ai-agent, behavioural, fingerprinting, methods, cloud-browser, detection, honey-site

## What it claims

- First controlled measurement study of seven AI browsing agents (OpenAI Atlas Browser and ChatGPT Agent, Anthropic's Claude for Chrome, Perplexity Comet, "Manus", plus open-source Browser Use and Skyvern) versus human users, using browser and behavioural fingerprints collected on an instrumented honey website across three tasks (flight booking, shopping, forum).
- Browser fingerprints alone give limited discriminative power (browser-only F1 ≈ 0.80), especially when multiple agents share a fingerprint (Atlas Agent, Browser Use, and Claude share one on macOS). Agents' browser fingerprints largely reflect their execution environment; current agents do not actively vary them.
- Behavioural fingerprints are highly distinctive (behavioural F1 ≈ 0.999; combined ≈ 1.0), separating agents from humans and from one another.
- Concrete behavioural tells: paste-based vs keystroke typing; change-event-based programmatic form filling; repeated delete-and-retype; direct "teleport" to click targets with no continuous mouse movement; and scrolling styles ranging from instant element-into-view jumps to multi-burst exploration. Humans show much higher and more variable inter-key/hold latencies (mean inter-key ≈ 120 ms vs single-digit-to-tens-of-ms for agents) and continuous mouse movement.
- Cloudflare case study: FP-Agent detects all seven agents; Cloudflare's free bot management blocks only one (Manus), and that block appears to rest on self-identification (Manus is a verified bot in Cloudflare's directory), not behavioural detection. Cloudflare blocked some server-side requests (ClaudeBot, Perplexity-User, ChatGPT-User) but not the locally-running agents themselves.
- Real-time detection is feasible: combined-classifier F1 plateaus after ~1 minute of behavioural data, behavioural-only after ~3 minutes.
- Voluntary self-identification (robots.txt, allowlists, Web Bot Auth) is insufficient because agents can decline to participate or sign inconsistently.
- This is an arms race: current agents do not actively evade out of the box, but future agents may adopt more human-like behaviour and erode these signals.
- Generalisation is bounded: closed-world classifier (cannot identify unseen agents as new classes); behavioural-only performance drops on unseen *tasks* (F1 down to ~0.63), while the combined classifier degrades negligibly (≤ 0.068).

## What evidence it provides

- 1,000 trials per agent split across the three tasks; 546 human instances from 56 recruited undergraduates performing tasks on their own machines (IRB-exempt; IP hashed). Honey website uses visitor-specific random-path subpages (method from Venugopalan et al. / SRC-015) for clean ground truth.
- Instrumentation: FingerprintJS for browser fingerprints plus custom JS event listeners for behaviour; 418 browser + 50 behavioural features. XGBoost multi-class classifiers, 80–20 split, six classifier configurations (three feature sets × two class sets).
- Analysis: XGBoost gain + SHAP for feature importance; Mann-Whitney U with rank-biserial effect sizes; Brown-Forsythe for variance; confusion matrices; per-class keystroke-latency statistics with 95% CIs.
- Cloudflare case study run on the free tier with AI Crawl Control and Block AI Bots enabled. Public code (GitHub) and data (OSF) released.

## Signals or techniques mentioned

- Browser-fingerprint features (via FingerprintJS): screen resolution, system/platform, fonts and font-preference pixel sizes, plugins, HDR/colour gamut, CPU cores, RAM, timezone, max touch points — and the finding that these track the execution environment.
- Behavioural-fingerprint features: typing inter-key and hold latency (mean/variance), backspace-delete counts, DOM input/change event counts, paste-event presence; scroll distance/duration (mean/variance, burst structure); mouse-movement curvature angle/distance/direction (and their near-absence for agents — click-only "teleport").
- Agent architecture taxonomy: DOM-based vs vision-based vs hybrid; tool calls wrapping Playwright or the Chrome DevTools Protocol; single- vs multi-agent. Scrolling/typing styles mapped to these (direct jumps ↔ DOM-based; multi-burst ↔ vision-based).
- Methods: XGBoost, SHAP, Mann-Whitney U, Brown-Forsythe.
- Defences referenced: robots.txt, Cloudflare Content Signals, Web Bot Auth (HTTP Message Signatures), Cloudflare Bot Management / verified-bots directory, and named industry agent-detection products (HUMAN Agentic Trust, DataDome Agent Trust) — named as landscape, not tested.

## Threat types covered

`Not threat-specific.` The study measures detectability of AI browsing agents **regardless of intent**; the agents perform benign tasks. The paper names scraping (OAT-011), credential stuffing (OAT-008), scalping (OAT-005), and CAPTCHA solving as malicious *potentials* of browsing agents, but does not study any of them. Relevant to the project as AI-agent *detection* evidence, not as evidence about a specific abuse type.

## Framing distance

- **What real-world problem does it approximate?** Whether the current generation of commercial AI browsing agents can be distinguished from humans (and each other) by browser/behavioural fingerprints during realistic web tasks, and how a deployed defender (Cloudflare free tier) fares against them. It is a strong, current snapshot of the agent/human behavioural gap.
- **What does it fail to represent?** A controlled honey site, not production traffic; benign tasks, not abusive use or agents tuned to evade; a closed-world set of seven known agents, not open-world detection of unseen ones; a narrow human population (56 undergraduates on their own machines), which the authors note inflates the human-vs-agent browser-fingerprint separation; only Cloudflare's **free** tier with two AI toggles (not enterprise Bot Management, and not HUMAN/DataDome despite naming them); and a point-in-time measurement (ChatGPT Agent already showed fingerprint drift mid-study).
- **What additional evidence would be needed to go further?** Production-traffic validation; open-world detection; agents adversarially tuned toward human-like behaviour; a broader human population; enterprise-tier and multi-vendor defender comparison; and longitudinal stability of the behavioural tells.

## What it cannot show

- It cannot show agents are undetectable in production, nor that these behavioural tells survive adversarial humanisation — the authors explicitly frame this as an arms race whose signals may weaken.
- It cannot generalise to unseen agents (closed-world); the behavioural classifier already drops sharply (F1 −0.37) on unseen tasks.
- The absence of shared human/agent browser fingerprints is partly an artefact of humans using their own machines vs agents on a few configs — the authors warn against reading it as real-world impossibility.
- The Cloudflare result ("detects only 1 of 7") is specific to the free tier with those toggles and cannot be generalised to all Cloudflare deployments, the enterprise product, or other vendors named but not tested.
- It does not establish the prevalence of AI-agent traffic; the Cloudflare 2024/2025 prevalence figures it cites (38.7% of top-million sites saw AI bot traffic; 8.7% of HTML traffic) are background context, not this paper's measurement, and should be attributed to those sources.
- **Dual-use note**: this is a detection paper, not a bypass guide, and its signals are defender-side. But its own arms-race section is, in effect, a list of the tells future agents will close. The entry records the behavioural tells at the class level (paste vs keystroke; teleport-click; environment-correlated fingerprints) as **current-snapshot detection signals**, not durable ones, and does not reproduce the agents' internal input-implementation code as an evasion recipe.

## Project impact

- **Fills the AI-agent-detection evidence gap** flagged as the most important hole in the Background/landscape draft: this is the first *independent (non-vendor)* source on whether AI browsing agents are detectable, complementing the defender-vendor framing (SRC-009 Kasada, SRC-010 HUMAN). It is the agent-*detection* counterpart the register was missing.
- **Second `measured`-tier source** after SRC-015, and a rare non-vendor **external check of a deployed defender** (Cloudflare free tier detects 1/7) — parallel to how SRC-015 externally checks DataDome. Strengthens the thin top of the proximity ladder.
- Strong anchor for a Techniques page on **behavioural detection of AI agents**: concrete, current discriminators with effect sizes (typing latency/variance, mouse teleport, scroll burst structure), plus the finding that **browser fingerprints alone are weak when shared** — supports the project's "fingerprints useful but unstable" argument line.
- Supports the threat-model "AI-agent shift" section with independent evidence that current agents do not actively evade, but that this is explicitly an arms race.
- Candidate for the project's methodology/reproduction strand: public code (GitHub) and data (OSF).
- **Flags for register/page use**:
  - The paper attributes Manus to "Meta" (ref [74] = `manus.im`). This appears to be a **factual error in the source** — Manus is not a Meta product. Do not propagate; verify and correct attribution before any citation.
  - Treat the "Cloudflare detects 1/7" result as free-tier-specific, and the behavioural tells as a dated snapshot.
  - Cross-citation worth recording: shares methodology and an author (Shafiq) with SRC-015.
