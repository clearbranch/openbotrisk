# TODO — live-site bot-signal investigation (SCOPING, not committed)

> Status: scoping only. This file is gitignored and deliberately outside the
> repo tree. Nothing here is a commitment; it exists to force the hard
> decisions to the front before any code or data collection starts.
> The defining feature of this investigation vs. the existing synthetic
> ones: **real data, real uncertainty, no ground truth by construction.**
> That is the whole point and also the whole risk.

---

## 0. The one-paragraph framing (write this first, revise last)

The existing investigations use synthetic data where the abusive groups are
detectable by construction. This one inverts that: instrument a real,
low-traffic site, observe the bot traffic that actually arrives, and
separately run known bot techniques against the site to see which signals
light up. The honest contribution is **"what is actually visible from a
realistic small-operator vantage point"** — including, prominently, what is
*not* visible. If the page cannot clearly state what it could not see, it
should not ship.

---

## 1. The two experiments are different and must stay separate

Conflating these is the fastest way to overclaim. Decide the split before
collecting anything.

### 1a. OBSERVATIONAL — characterise unbidden bot traffic
- What arrives without being invited: scrapers, SEO/search crawlers,
  vulnerability scanners, LLM data-collection bots, analytics/ad fraud.
- Strengths: real adversaries, real prevalence, genuinely under-documented
  for *small* sites (most public bot-rate stats are enterprise-scale).
- Weakness: zero ground truth. "Is this a bot" is inferred, not known.
- Honest claim ceiling: *descriptive*. "Here is the background bot rate and
  its visible structure on one small UK site over N weeks."

### 1b. RED-TEAM — run known techniques against own site, measure visibility
- Full ground truth (you know exactly what you emitted) and full control.
- BUT: only characterises *your own attacker model*, not a real adversary.
  The validity claim is narrow: "these signals distinguish *my scripted
  access* from *my normal browsing*." Label this explicitly, repeatedly.
- This is where the residual-signal family lives (TLS/JA3, header order,
  timing, client-side behavioural) because you can *emit* those deliberately.

### Decision needed
- [ ] Are 1a and 1b one page with two clearly-walled sections, or two pages?
      (Leaning: two pages. 1a is observational/descriptive; 1b is a
      controlled experiment. Different evidence tiers, different claims.)

---

## 2. FEASIBILITY GATE — infrastructure decides everything (resolve before signals)

The signals most worth having are exactly the ones a static-host + Google
Analytics stack **cannot** provide. Confront this first; it determines
whether the project is even possible in the form imagined.

### What each layer can and cannot see
| Vantage point | Gives you | Cannot give you |
|---|---|---|
| GitHub Pages (static, as-is) | nothing server-side | logs, headers, IP, TLS — all absent |
| Google Analytics | sanitised, sampled, JS-gated client data | anything from non-JS clients (most scrapers), raw IP, headers |
| Client-side JS (own) | mouse/keystroke/scroll, JS-execution fact | anything from clients that don't run JS |
| Reverse proxy / CDN (e.g. Cloudflare) | request logs, IP/ASN, UA, some bot scoring, JA3/JA4 on higher tiers | depends on tier; deep client behaviour |
| Edge function / worker | structured request metadata you define | you now own the code + privacy surface |
| Small real server | everything incl. raw TLS handshake | maintenance burden + attack surface + full data-controller role |

### The blunt facts to internalise
- **JS-execution-as-signal is real and free.** Most commodity scrapers do
  not run JS. So a request that hits the HTML but never fires the GA/beacon
  JS is *probably* a non-rendering client. The *absence* of client-side
  signal is itself a usable signal — possibly the single most accessible
  finding on a static+GA stack. Worth pursuing even if nothing else is.
- **JA3/JA4, header order, server-side IP/ASN require terminating or
  proxying the connection.** Static hosting gives none of these.
- **The interesting bots and the observable signals barely overlap** on the
  cheapest stack: the bots you can fingerprint client-side are the ones
  sophisticated enough to run JS; the bots you can only see server-side are
  the ones a static host can't see at all.

### Decision needed (this is the load-bearing one)
- [ ] Minimum infra that exposes server-side signals without becoming a
      burden or a liability. Candidate: **Cloudflare (free/pro) in front of
      the existing Pages site** — request logs + bot score + IP/ASN, no
      server to run. Check what JA3/JA4 actually requires (likely paid tier;
      confirm, don't assume).
- [ ] Fallback if no proxy: scope the page *honestly down* to
      "what GA + a client-side beacon can and cannot see," and make the
      JS-execution-absence finding the centrepiece. Still a real page.
- [ ] Explicitly reject: standing up a real server just for raw TLS, unless
      the JA3 finding is judged worth the burden + attack surface + GDPR
      controller role. Default = no.

---

## 3. GOVERNANCE GATE — UK GDPR, resolve in parallel with §2, before any logging

Non-negotiable for a UK-based public site. The page's credibility *depends*
on visibly getting this right — studying tracking must not mean quietly
building a tracker. Cheaper to design in than retrofit (cf. the PCI/keyed-hash
point that started this whole thread).

- [ ] Lawful basis for processing IP + fingerprint + behavioural signals on
      real visitors. (Legitimate interest is plausible but needs an LIA;
      document it.)
- [ ] Privacy notice updated *before* collection, not after. Says what is
      collected, why, retention, how to object.
- [ ] Retention limit + deletion. Short. Aggregate-then-discard raw where
      possible.
- [ ] Pseudonymise at intake: keyed-hash IPs and any identifier rather than
      storing raw, exactly as recommended for the card data in the
      clustering thread. Store the salt/key separately.
- [ ] Red-team (1b) traffic is self-generated → not third-party personal
      data → much lighter. Use this asymmetry: lean on 1b for anything
      sensitive, keep 1a aggregate-only.
- [ ] Decide consent posture: behavioural-biometric collection on real
      visitors may need consent, not just LI. The red-team path sidesteps
      this entirely. Another reason 1b carries the heavy signal work.

---

## 4. SIGNAL INVENTORY (only meaningful after §2 resolves)

Tag each: [SERVER] needs proxy/server · [CLIENT] needs JS execution ·
[GA] visible in Google Analytics (sanitised).

- [ ] User-agent string + UA/behaviour consistency [SERVER, partial GA]
- [ ] IP → ASN/ISP, datacentre-vs-residential classification [SERVER]
      (ties to MaxMind GeoIP register work already done)
- [ ] JA3 / JA4 TLS fingerprint [SERVER, likely paid CDN tier]
- [ ] HTTP header set + ordering [SERVER]
- [ ] JS-execution fact: did the client run the beacon at all [CLIENT/GA]
      ← the free, high-value one on a static stack
- [ ] Request timing / inter-request intervals / crawl pattern [SERVER]
- [ ] Path patterns: robots.txt fetch, sitemap crawl, 404-scanning,
      wp-admin probing (the vuln-scanner tell) [SERVER]
- [ ] Mouse/keystroke/scroll dynamics [CLIENT, consent-sensitive — 1b only]
- [ ] Honeypot endpoints/links invisible to humans, visited only by
      indiscriminate crawlers [SERVER, cheap, high signal, low privacy cost]

Note: honeypots + JS-execution-absence are the two cheapest, highest-signal,
lowest-privacy-cost items. If the proxy decision stalls, these two alone
could carry an observational page.

---

## 5. THE "WHAT GOOGLE ANALYTICS ACTUALLY GIVES YOU" sub-page

Standalone candidate, smaller scope, possibly the easiest to ship first.
The honest reverse-engineering: what can and cannot be inferred about bot
traffic from GA alone, given its sampling, JS-gating, and bot-filtering.
- [ ] Document GA's own (opaque) bot filtering — it silently drops "known
      bots," so GA *systematically under-counts* exactly the population of
      interest. That limitation IS the finding.
- [ ] Cross-check GA numbers against proxy logs (if §2 yields a proxy) to
      quantify the gap. Strong page if both data sources exist.
- [ ] Ship-on-its-own viability: yes, even with no proxy, as a
      "limits of analytics for bot study" piece. Low risk, real content.

---

## 6. EVALUATION — the part that makes or breaks credibility

No ground truth in 1a. State the inference method for every "this is a bot"
claim. Borrow the split/merge honesty framing from the fingerprint page:
every classification has a false-positive and false-negative mode, and on
real data neither is measurable directly — only triangulated.

- [ ] 1b gives the only real ground truth: known emitted traffic. Use it to
      *calibrate* what a signal looks like, then apply (cautiously) to 1a.
- [ ] Never present a 1a bot-rate as precise. Ranges + method, not points.
- [ ] Pre-register (privately) what you expect to see, so the page can
      honestly report surprises vs confirmations rather than post-hoc
      storytelling. (Same discipline as the ORR decision register.)

---

## 7. RISKS / OPEN QUESTIONS (the things that could sink it)

- [ ] Traffic volume. A personal site may get too little bot traffic for
      anything but anecdote. Mitigation: longer collection window; or accept
      the page is a *method demonstration on small data*, not a prevalence
      study — and say so. Check current GA volume before committing.
- [ ] The red-team self-attack only ever validates against your own attacker
      model. Cannot be fixed, only disclosed. The page must not let a reader
      mistake "I caught my own script" for "this catches real adversaries."
- [ ] Scope creep into building an actual tracking/surveillance stack.
      Guard: aggregate-and-discard, keyed-hash at intake, red-team-first.
- [ ] Maintenance burden. Anything beyond a proxy is a standing liability on
      a solo open-source project. Default to the lowest-infra option that
      still yields a real finding.
- [ ] Does this duplicate the threat-model / commercial-defender-landscape
      pages at survey level? Check before committing — the value here is the
      *primary-data experiment*, so make sure it adds over the survey.

---

## 8. SUGGESTED SEQUENCING (if it goes ahead)

1. Resolve §2 (infra) and §3 (governance) on paper. No collection until both
   are answered. These gate everything.
2. Ship the §5 GA-limits sub-page first — smallest, lowest-risk, real, and
   it surfaces the JS-gating/bot-filtering facts the bigger page will lean on.
3. Stand up honeypots + JS-execution-absence logging (§4) — cheapest real
   signals, lowest privacy cost.
4. If proxy lands: add server-side signals, build the observational page (1a).
5. Run the controlled red-team (1b) last, with the most signal access, as the
   companion experiment with actual ground truth.

---

## Parking lot (related, not this project)
- Behavioural-biometrics arms-race page — synthetic, no live data needed,
  cleaner build. May be the better *next* investigation than this one.
- TLS-fingerprinting deep-dive as part-2 of the browser-fingerprint page.
- Proxy/residential-IP detection page (ties to MaxMind work).

---

## 9. PUBLIC LABELLED DATASETS — the evaluation anchor (added after EDA notebooks)

Four EDA notebooks exist (`openbotrisk.eda`-driven, mechanical descriptive
reports). Three carry **real labels**, which is exactly the thing the
synthetic pages and this live-site project lack. The pattern to exploit:

> **Public labelled dataset = calibration (measurable error rate).
> Live-site own traffic = application (no labels, error rate only
> triangulated).** Each method page gets both: "here is the error rate we
> measured where labels exist, and here is why we cannot measure it directly
> on our own traffic." This *closes the no-ground-truth hole* in §6.

### Dataset → method-page mapping
| Dataset | Label | Best paired with | Fit | Watch out for |
|---|---|---|---|---|
| `web-robot-sessions` (Figshare 3477932) | `ROBOT` 0/1, session-level | a real-data **behavioural bot-detection** page; calibration anchor for the live-site behavioural work | **strongest, most on-remit** | labels are the *original paper's heuristic* (UA/robots.txt/known-crawler). Model must not just relearn the UA rule — make that circularity the page's central point. |
| `ieee-fraud-detection` (Kaggle IEEE-CIS) | `isFraud` ~3.5% | real-data companion to the **identifier-graph** page | strong | label is *card-level, propagated* (entity-resolution subtlety — actually useful); V-cols anonymised; keep to checkout/card-testing slice per scope |
| `talkingdata-adtracking` (Kaggle, ~7 GB) | `is_attributed` | real-data home for the **synchrony** method (click-timing per IP/device) | good for synchrony only | `is_attributed`=legit conversion, NOT a bot label. Fraud inferred from absence+volume. 7 GB DuckDB streaming. Do not present as a labelled bot classifier. |
| `ctu-13` (CTU Stratosphere netflow) | Botnet/Legit/Background | — | **SCOPE-BOUNDARY RISK** | network-layer C2 / malware netflow = SOC/intrusion territory, explicitly excluded by repo scope. `Background` ≠ verified-legit. 13 spliced families. **Decide keep-or-cut deliberately; default lean = cut.** |

### Decisions needed
- [ ] `web-robot-sessions`: promote to its own real-data investigation. This
      is probably a *better and lower-risk next page than the live-site
      project*, and it de-risks the live-site project by providing the
      calibration the live data can't. Consider doing it FIRST.
- [ ] Guard against the label-circularity trap: hold out UA-derived features,
      or explicitly compare "UA-rule baseline" vs "behavioural model" so the
      page measures *marginal* signal over the heuristic that made the labels.
- [ ] `ctu-13`: explicit keep/cut on scope grounds. Do not let "it has
      botnets in it" override the web-facing-abuse boundary.
- [ ] `ieee` and `talkingdata`: position as the "on real data" extensions
      already listed for the two synthetic pages, not as new standalone work.
- [ ] Check what `openbotrisk.eda` writes these reports into (`working/eda/`)
      and whether those descriptive reports should themselves become linked
      dataset pages on the site (cheap, honest, and they document provenance).
