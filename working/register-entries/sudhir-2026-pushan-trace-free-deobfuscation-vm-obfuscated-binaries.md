# Sudhir et al. (2026) - Pushan: trace-free deobfuscation of virtualization-obfuscated binaries

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded arXiv PDF `SRC-078-pushan-trace-free-deobfuscation-of-virtualization.pdf`; supporting academic PDF `SRC-078-enhance-virtual-machine-based-code-obfuscation-sec.pdf`; public tutorial PDF `SRC-078-hiding-code-like-a-spy-vm-based-code-obfuscation-in-c-with-runtime-decryption-by-piyush-medium.pdf`.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.
- **Source handling decision**: keep Pushan as a standalone academic entry. Use Kuang et al. 2018 as supporting background on stronger VM obfuscation. Do not create a standalone entry for the Medium tutorial.

## Bibliographic

### Main source

- **Citation**: Sudhir, A., Basque, Z. L., Gibbs, W., Bajaj, A. P., Singaria, P. S., Zakocs, M., Hu, J., Schloegel, M., Bao, T., Doupe, A., Shoshitaishvili, Y., & Wang, R. (2026). *Pushan: Trace-Free Deobfuscation of Virtualization-Obfuscated Binaries*. arXiv:2603.18355v1. Posted 18 March 2026.
- **Source URL or path**: uploaded PDF `SRC-078-pushan-trace-free-deobfuscation-of-virtualization.pdf`.
- **Publication status**: arXiv preprint. Treat as not peer-reviewed unless later venue publication is confirmed.

### Supporting background source

- **Citation**: Kuang, K., Tang, Z., Gong, X., Fang, D., Chen, X., & Wang, Z. (2018). *Enhance virtual-machine-based code obfuscation security through dynamic bytecode scheduling*. Computers & Security, 74, 202–220. https://doi.org/10.1016/j.cose.2018.01.008
- **Source URL or path**: uploaded PDF `SRC-078-enhance-virtual-machine-based-code-obfuscation-sec.pdf`.

### Weak contextual source not separately registered

- **Citation**: Piyush. (2025). *Hiding Code Like a Spy: VM-Based Code Obfuscation in C (with Runtime Decryption)*. Medium. Published 23 April 2025.
- **Source URL or path**: uploaded PDF `SRC-078-hiding-code-like-a-spy-vm-based-code-obfuscation-in-c-with-runtime-decryption-by-piyush-medium.pdf`.

## Category and treatment

- **Category**: academic
- **Evidence basis**: empirical-method demonstration / deobfuscation research / preprint
- **Operational proximity**: measured-but-bounded — evaluates a deobfuscation technique against many VM-obfuscated binaries and commercial protectors, but this is reverse-engineering research rather than web-bot detection telemetry.
- **Tags**: VM-obfuscation, virtualization-obfuscation, deobfuscation, reverse-engineering, malware-analysis, VMProtect, Themida, Tigress, Pushan, VPC-sensitivity, symbolic-emulation, CFG-recovery, decompilation, anti-reverse-engineering, client-side-detection-arms-race

## What it claims

- Virtualization/VM-based obfuscation is one of the strongest protection mechanisms against automated and manual reverse engineering.
- It is used to hinder analysis of malware and protected software by translating original instructions into custom VM bytecode and executing them through injected VM interpreters.
- Existing automated deobfuscation methods have important limitations:
  - trace-based methods only recover paths that are executed;
  - dynamic symbolic execution scales poorly due to path explosion and constraint-solving difficulty;
  - many outputs are not well-formed enough for ordinary decompilers to produce analyst-friendly pseudocode.
- Pushan introduces a trace-free approach that uses VPC-sensitive, constraint-free symbolic emulation to recover complete control-flow graphs from virtualization-obfuscated binaries.
- Pushan then applies semantics-preserving simplifications and decompilation to produce C-like pseudocode.
- The authors evaluate Pushan on more than 1,000 binaries, including Tigress, VMProtect, Themida, CTF challenges, and a real-world VMProtect-obfuscated malware sample.
- The paper argues that Pushan is the first approach to enable effective end-to-end analysis of code protected by virtualization.

## What evidence it provides

This is a **method demonstration and evaluation paper**.

It provides:

- a technical explanation of VM-based obfuscation;
- a comparison of deobfuscation methods;
- a new algorithmic approach:
  - VPC-sensitive CFG recovery;
  - constraint-free symbolic emulation;
  - semantics-preserving simplification;
  - decompilation to C pseudocode;
- comparison with prior methods;
- evaluations against:
  - Tigress-generated VM-obfuscated binaries;
  - commercial-strength obfuscators VMProtect and Themida;
  - CTF challenges;
  - a real-world VMProtect-obfuscated malware sample from VirusTotal;
- a useful framing of why trace-based deobfuscation misses logic;
- a practical reminder that VM obfuscation increases analysis cost but is not invulnerable.

## Main quantitative details

| Evaluation component | Reported result |
|---|---:|
| Tigress-generated binaries | 1,000 |
| Tigress cases successfully analysed/deobfuscated/decompiled | 988 / 1,000 |
| Prior state-of-the-art comparison on Tigress | 68 complete CFGs |
| VMProtect/Themida evaluation set | 28 unique obfuscated binaries |
| VMProtect/Themida cases with 100% CFG similarity | 17 / 28 |
| CTF bespoke VM samples | 5 / 5 succeeded |
| Real-world malware sample | VMProtect-obfuscated VirusTotal sample analysed |

## Important visual/source evidence

- **Table 1 on page 3** compares Pushan with prior VM-deobfuscation techniques and marks Pushan as producing a CFG, handling complex programs, recovering complete CFGs, and producing decompilable code.
- **Figure 1 on page 3** illustrates VM-based obfuscation: original code translated into bytecode, interpreted by a fetch/decode/dispatch loop and handlers.
- **Figure 4 on page 5** shows Pushan’s analysis pipeline: obfuscated binary → VM-obfuscated CFG → flat CFG by constraint-free symbolic emulation → simplified CFG → C pseudocode.
- The Kuang et al. supporting source includes **Figure 1 on page 3**, showing a classic VM-based obfuscation process: code extraction, virtualization, bytecode generation, and file patching.
- The Kuang et al. source also explains dynamic scheduling and multiple VMs as a way to resist cumulative reverse-engineering attacks.

## Signals or techniques mentioned

- virtualization-based obfuscation;
- VM-based obfuscation;
- custom bytecode;
- VM interpreter;
- VM handlers;
- virtual program counter / VPC;
- control-flow graph / CFG recovery;
- trace-based deobfuscation;
- dynamic symbolic execution;
- path explosion;
- SMT solving;
- constraint-free symbolic emulation;
- semantics-preserving simplification;
- decompilation;
- C pseudocode output;
- VMProtect;
- Themida;
- Tigress;
- malware analysis;
- commercial-strength obfuscators;
- dynamic bytecode scheduling;
- multiple VMs;
- cumulative reverse-engineering attacks;
- opcode/handler mapping diversity.

## Threat types covered

This source is not an OWASP OAT source and does not measure web-bot abuse.

Directly covered:

- reverse engineering of protected binaries;
- malware analysis under obfuscation;
- deobfuscation of VM-protected code;
- limits of VM obfuscation.

Indirect relevance to openbotrisk:

- reverse engineering of client-side anti-bot detection;
- analysis of obfuscated browser-side detection or challenge logic, by analogy;
- anti-bot arms race where defender-side detection logic is protected and attackers build deobfuscation capability.

## What is strong

- Strong academic counterweight to vendor claims about VM obfuscation.
- Useful for avoiding the false claim that VM obfuscation is unbreakable.
- Good evidence that VM obfuscation raises cost but remains an active target for automated deobfuscation research.
- Provides concrete evaluation results, not just conceptual discussion.
- Useful for the review’s “arms race” framing:
  - defenders obfuscate detection logic;
  - researchers/attackers develop deobfuscation methods;
  - defenders add diversity, regeneration, and multiple VMs;
  - the cycle continues.
- Useful bridge to DataDome because it supports a balanced statement: DataDome’s VM obfuscation is plausible defensive hardening, but the broader research field keeps moving.

## What is weak or limited

- Preprint, not confirmed peer-reviewed.
- Focuses on native binaries and malware analysis, not browser JavaScript anti-bot scripts.
- Does not evaluate DataDome or any specific bot-management vendor’s browser VM.
- Does not show that real-world attackers can or cannot deobfuscate current client-side bot protections.
- Does not measure bot abuse, scraping, credential stuffing, or ticketing abuse.
- Does not provide production telemetry.
- The technique’s direct transfer to browser-delivered anti-bot code should be treated as an analogy unless backed by more specific evidence.
- It is dual-use: the same methods that help defenders analyse malware may help adversaries analyse protected detection logic.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  The reverse-engineering side of the client-side detection arms race. It shows that VM-obfuscated code can be targeted by increasingly capable deobfuscation tools.

- **What does it fail to represent?**  
  It does not directly study anti-bot JavaScript, browser-delivered VM bytecode, or live fraud tooling. It is mainly about binary deobfuscation and malware analysis.

- **What additional evidence would be needed to go further?**  
  Browser-specific deobfuscation studies, red-team evaluations of anti-bot scripts, vendor telemetry, attacker write-ups, and independent testing against real client-side bot-management protections under authorised conditions.

## What it cannot show

- It cannot show that DataDome’s VM obfuscation can be defeated.
- It cannot show that all VM obfuscation is weak.
- It cannot show bot-detection performance.
- It cannot show abuse prevalence.
- It cannot show live attacker capability against current anti-bot vendors.
- It cannot establish whether browser VM obfuscation has the same properties as native binary VM obfuscation.

## Project impact

Use this as the **academic arms-race / limits source for VM obfuscation**.

Best uses:

- balance vendor claims about VM-based obfuscation;
- explain why obfuscation is a cost-increasing measure, not an absolute guarantee;
- support the review’s point that protecting detection logic creates a reverse-engineering contest;
- add rigour to the DataDome entry;
- show that deobfuscation research produces measurable advances.

Do not use it as:

- evidence that a particular bot-management vendor is bypassable;
- web-bot detection evidence;
- proof of real-world attacker use;
- a procedural deobfuscation guide;
- a source for implementation details in the public-facing review.

## Relationship to other register entries

- **DataDome VM-based obfuscation**: direct pairing. DataDome shows commercial defensive adoption; Pushan shows the deobfuscation research counter-pressure.
- **Kuang et al. DSVMP**: supports the background on dynamic scheduling, multiple VMs, and diversity against cumulative attacks.
- **Medium VM-obfuscation tutorial**: do not register separately; only weak evidence that VM-obfuscation ideas are accessible in public tutorials.
- **Laperdrix / Berke**: browser/device fingerprints may be collected by client-side code, which then needs protection.
- **Cloudflare / DataDome / HUMAN bot-management entries**: this is not a bot-detection signal source; it is about protection of detection logic.
- **CAPTCHA / challenge entries**: relevant where challenge or device-check code is exposed client side and becomes a reverse-engineering target.

## Note on supporting sources

### Kuang et al. 2018

Kuang et al. is useful background if you need a more formal explanation of stronger VM obfuscation designs. It proposes DSVMP, using dynamic instruction scheduling and multiple VMs so the same protected logic can follow different execution paths and use different opcode/handler mappings across runs. It is a good supporting citation for the idea that VM obfuscation has its own internal arms race.

### Medium tutorial

The Medium source is too procedural and code-heavy for a standalone register entry. It should only be mentioned, if needed, as evidence that VM-obfuscation concepts are public and accessible. Do not reproduce its code or anti-debugging workflow in the project.

## Dual-use containment

High dual-use. Deobfuscation techniques can help malware analysts and defenders, but can also help attackers reverse engineer protected detection logic. Use this source to discuss limits, evaluation, and arms-race dynamics. Avoid turning it into a deobfuscation playbook.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `sudhir-2026-pushan-trace-free-deobfuscation-vm-obfuscated-binaries` |
| Title | *Pushan: Trace-Free Deobfuscation of Virtualization-Obfuscated Binaries* |
| Authors | Ashwin Sudhir et al. |
| Year | 2026 |
| Category | academic |
| Evidence basis | empirical-method demonstration / deobfuscation research / preprint |
| Operational proximity | measured-but-bounded |
| Signals / techniques | VM obfuscation; bytecode; VPC sensitivity; CFG recovery; symbolic emulation; decompilation; VMProtect; Themida; Tigress |
| Threat types | reverse engineering of protected code; indirect relevance to client-side anti-bot detection arms race |
| Project use | Academic counterweight and limits source for VM obfuscation in client-side detection protection |
| Main caution | Native-binary deobfuscation preprint; not direct evidence against browser anti-bot scripts or current vendor protections |
| Entry file | `sudhir-2026-pushan-trace-free-deobfuscation-vm-obfuscated-binaries.md` |
