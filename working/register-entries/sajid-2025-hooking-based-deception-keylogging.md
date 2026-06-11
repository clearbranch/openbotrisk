# Sajid et al. (2025) - Hooking-based deception framework against keylogging

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded arXiv PDF `SRC-074-sajid-2025-hooking-based-deception-keylogging.pdf`.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.
- **Source handling decision**: keep as a smaller related entry. It is not bot-specific, but it is useful for the cyber-deception / runtime instrumentation / anti-tamper strand.

## Bibliographic

- **Citation**: Sajid, M. S. I., Ahmed, S., & Sosnoski, R. (2025). *Secure Development of a Hooking-Based Deception Framework Against Keylogging Techniques*. arXiv:2508.04178v1. Posted 6 August 2025.
- **Source URL or path**: uploaded PDF `SRC-074-sajid-2025-hooking-based-deception-keylogging.pdf`.
- **Publication status**: arXiv preprint. Treat as not peer-reviewed unless later venue publication is confirmed.
- **Category**: academic / cyber deception / endpoint instrumentation
- **Evidence basis**: empirical-method demonstration / preprint
- **Operational proximity**: measured-but-bounded — evaluates deception against keylogger malware samples and a custom anti-hooking keylogger, but not web bots or browser automation.
- **Tags**: cyber-deception, API-hooking, keyloggers, anti-hooking, runtime-instrumentation, EasyHook, Microsoft-Detours, decoy-injection, input-perturbation, Hook-Integrity-Manager, trampoline-obfuscation, clone-DLL-detection, guard-pages, Windows-APIs, malware-evasion

## What it claims

- Keyloggers capture sensitive user input such as credentials, financial details, and private messages.
- Traditional defences focus on detection/removal, but deception can corrupt attacker-collected data while preserving opportunities for intelligence gathering.
- API hooking can intercept input-related API calls and inject false or misleading data.
- Naive API hooking is vulnerable because advanced malware can detect, remove, or bypass hooks.
- The paper proposes a hardened hooking-based deception framework that:
  - intercepts input-related APIs;
  - injects realistic decoy keystrokes or perturbed input;
  - detects tampering;
  - restores or protects hooks against evasion.
- The framework uses EasyHook and Microsoft Detours.
- It was evaluated against a custom “super keylogger” and 50 real-world malware samples across ten keylogger families.
- The authors report that the framework maintained deception and resisted tested anti-hooking strategies with negligible overhead.

## What evidence it provides

This is a **method demonstration and evaluation paper**, not a bot-detection source.

It provides:

- a taxonomy of userland keylogger techniques and associated APIs;
- a runtime-deception architecture:
  - Hooking Layer;
  - Deception Engine;
  - Hook Integrity Manager;
- a threat model for user-mode keyloggers;
- four key API categories:
  - direct input acquisition;
  - window message inspection;
  - hook-based capture;
  - auxiliary collection such as clipboard and form submission;
- deception policies:
  - decoy injection;
  - input perturbation;
- anti-hooking resilience techniques:
  - active hook verification;
  - clone DLL detection;
  - trampoline obfuscation;
  - guard pages on hooked code;
- evaluation against 50 malware samples and a custom multi-vector “super keylogger”.

It does **not** provide:

- web-bot evidence;
- browser anti-bot detection evidence;
- current commercial endpoint-product evidence;
- independent replication;
- production deployment evidence;
- evidence for scraping, credential stuffing, scalping, CAPTCHA defeat, or account creation.

## Key quantitative and factual details

| Detail | Reported value / treatment |
|---|---|
| Real-world malware samples | 50 |
| Keylogger families | 10: Agent Tesla, AppleSeed, RokRAT, gh0st RAT, WarzoneRAT, Astaroth, Micropsia, NightClub, Azorult, Lokibot |
| Analysis tools | Cuckoo Sandbox, Rohitab API Monitor, OllyDBG |
| Hooking libraries | EasyHook and Microsoft Detours |
| Super keylogger capture methods | five: polling, event hooks, GUI message spying, clipboard monitoring, HTTP/form-grabbing simulation |
| Anti-hooking methods tested | `.text` section restoration, IAT rebinding, alternate DLL loading, signature-based memory scanning |
| CPU overhead in polling tests | consistently below 1% across five 60-second runs |
| WarzoneRAT polling detail | about 131 `GetAsyncKeyState` calls per minute in the reported case |
| Real-world sample outcome | paper says all 50 had targeted API calls intercepted and logged fake rather than real input |

## Important visual/source evidence

- **Table I / page 2** maps userland keylogger techniques to APIs: `SetWindowsHookEx`, `GetAsyncKeyState`, `PeekMessage`, clipboard APIs, HTTP/network APIs, screen logging APIs, mouse APIs, browser DOM key events, raw input APIs, and process injection APIs.
- **Figure 1 / page 3** shows the deception framework architecture: benign user process, keylogger, hooked API, detour, deception engine, Hook Integrity Manager, active hook verification, clone DLL detection, trampoline obfuscation, and guard pages.
- The evaluation section reports low overhead and all-50-sample interception/deception results, but this should be treated as the authors’ preprint evaluation, not external validation.

## Signals or techniques mentioned

- keylogging;
- cyber deception;
- decoy keystrokes;
- API hooking;
- runtime interception;
- EasyHook;
- Microsoft Detours;
- `GetAsyncKeyState`;
- `GetKeyState`;
- `SetWindowsHookEx`;
- `PeekMessage`;
- `GetMessage`;
- `OpenClipboard`;
- `GetClipboardData`;
- `HttpSendRequest`;
- `InternetWriteFile`;
- `WSASend`;
- browser DOM key events;
- input perturbation;
- decoy injection;
- Hook Integrity Manager;
- active hook verification;
- clone DLL detection;
- trampoline obfuscation;
- guard pages;
- `.text` section restoration;
- IAT rebinding;
- alternate DLL loading;
- dynamic API resolution;
- memory scanning;
- sandbox/debugger/timing evasion.

## Threat types covered

Directly covered:

- keylogging;
- credential theft;
- form grabbing;
- clipboard theft;
- malware evasion against userland hooks;
- deception against surveillance malware.

Indirect relevance to openbotrisk:

- client-side/endpoint instrumentation can itself be attacked;
- defensive deception may complement detection;
- anti-tamper and resilience matter when defenders instrument an adversarial runtime;
- browser-side key events and form submission APIs overlap conceptually with web automation and account-abuse workflows.

OAT mapping is weak and mostly indirect:

- **OAT-008 Credential Stuffing / ATO context** — indirect because keyloggers can steal credentials later used in ATO/credential stuffing, but the paper is not about stuffing.
- **OAT-019 Account Creation / OAT-011 Scraping** — no direct mapping.
- Treat this as cyber-deception background, not an OAT evidence source.

## What is strong

- Useful smaller source for the “defensive instrumentation is an adversarial runtime” theme.
- Shows a concrete deception approach: feed attackers false data instead of only detecting/removing them.
- Good complement to the ML/cybersecurity background entry because it gives a practical endpoint-deception mechanism.
- Useful analogy to client-side anti-bot systems:
  - defenders place logic/hooks/instrumentation in a hostile environment;
  - attackers try to detect or bypass that instrumentation;
  - defenders need anti-tamper and recovery mechanisms.
- Stronger than generic deception discussion because it includes real malware sample evaluation and a custom adversarial “super keylogger”.

## What is weak or limited

- arXiv preprint, not confirmed peer-reviewed.
- Not web-bot-specific.
- Windows/userland keyloggers only; kernel and hardware keyloggers are out of scope.
- The framework assumes a prior detection event; it is not a standalone detector.
- Deployment would require integration with EDR/analyst workflows.
- The custom “super keylogger” includes LLM-assisted generated components; useful for stress testing but not direct evidence of in-the-wild tools.
- The results are reported by the authors and not independently reproduced here.
- It should not be used to support claims about CAPTCHA, proxies, browser fingerprints, or bot-management systems.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  Defensive control of an adversarial endpoint runtime where malicious code tries to observe sensitive user input and evade instrumentation.

- **What does it fail to represent?**  
  It does not represent web-bot detection, browser automation, anti-bot challenge systems, or production bot-management. It is endpoint malware deception.

- **What additional evidence would be needed to go further?**  
  Peer review, independent replication, EDR integration studies, endpoint telemetry, broader malware families, and sources that connect endpoint instrumentation/deception to web-account abuse.

## What it cannot show

- It cannot show web-bot detection effectiveness.
- It cannot show current anti-bot vendor practice.
- It cannot show that deception works against browser automation.
- It cannot show live deployment success.
- It cannot show that kernel/hardware keyloggers are affected.
- It cannot replace bot-management, browser-security, or authentication sources.

## Project impact

Use this as a **smaller cyber-deception/runtime-instrumentation support entry**.

Best uses:

- support the ML/cybersecurity/deception strand;
- explain deception as a complement to detection;
- provide an example of runtime interception and anti-tamper hardening;
- strengthen the broader point that defenders’ client-side/endpoint controls can be targeted and must be resilient.

Do not use it as:

- bot evidence;
- OAT evidence;
- web anti-bot detection evidence;
- current commercial product evidence;
- a procedural guide to hooking or malware analysis.

## Relationship to other register entries

- **Cao thesis**: both involve defensive control of client-side execution, but Cao is browser-principal isolation while Sajid et al. is endpoint API hooking/deception.
- **Tschacher/Incolumitas bot-detection architecture**: both treat client-side data/control as contested, but Tschacher is web-bot architecture; Sajid et al. is endpoint malware deception.
- **DataDome VM obfuscation**: both concern defensive logic in adversarial client-side environments; DataDome is anti-bot product hardening, Sajid et al. is endpoint hook hardening.
- **Pushan deobfuscation / Xu layered obfuscation**: relevant to the anti-tamper and protection-of-defensive-code theme.
- **AI/ML cybersecurity background**: this entry gives a concrete deception/instrumentation example for that broader section.

## Dual-use containment

Moderate dual-use. The paper discusses keylogger APIs and anti-hooking tactics. Use it for deception architecture, runtime instrumentation, and limitations. Avoid reproducing implementation steps, code, or malware-building details.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `sajid-2025-hooking-based-deception-keylogging` |
| Title | *Secure Development of a Hooking-Based Deception Framework Against Keylogging Techniques* |
| Authors | Md Sajidul Islam Sajid; Shihab Ahmed; Ryan Sosnoski |
| Year | 2025 |
| Category | academic / cyber deception / endpoint instrumentation |
| Evidence basis | empirical-method demonstration / preprint |
| Operational proximity | measured-but-bounded |
| Signals / techniques | API hooking; decoy injection; input perturbation; EasyHook; Detours; anti-hooking; hook integrity; trampoline obfuscation; clone DLL detection; guard pages |
| Threat types | keylogging; credential theft; form grabbing; malware evasion; indirect relevance to account-abuse defence |
| Project use | Smaller support source for cyber deception and resilient client-side/runtime instrumentation |
| Main caution | Not bot-specific; assumes prior detection; userland Windows keyloggers only; preprint |
| Entry file | `sajid-2025-hooking-based-deception-keylogging.md` |
