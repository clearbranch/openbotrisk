# MaxMind GeoIP/GeoLite Knowledge Base — IP-geolocation & IP-intelligence accuracy/methodology

## Extraction run metadata

- **Extraction date**: 2026-06-06
- **Extraction agent**: Claude (chat interface)
- **Model name + version, if known**: Claude Opus 4.8
- **Source access**: hub page + two articles read in full ("Geolocation accuracy", "Proxy detection and anonymous IP"); the remaining cluster articles are enumerated by title from the hub and **not individually reviewed** (citation-integrity note — see What it cannot show).
- **Prompt version**: source-extraction-prompt v3 (2026-06)

## Bibliographic

- **Citation**: MaxMind, Inc. *GeoIP and GeoLite Knowledge Base* (article cluster). © 2025 MaxMind, Inc. Articles read: hub "GeoIP and GeoLite"; "Geolocation accuracy"; "Proxy detection and anonymous IP".
- **Source URL or path**: hub `https://support.maxmind.com/knowledge-base/geoip-and-geolite`; accuracy `…/articles/maxmind-geolocation-accuracy`; proxy/anonymous-IP `…/articles/anonymizer-and-proxy-data-maxmind`. Cluster also contains (by title, not reviewed): Choose the right geolocation product; Country/city-level geolocation; IP geolocation data; Geolocation coverage; Upgrade from GeoLite; Correct GeoIP data; Choose the IP-intelligence data you need; IP network data; Business VPNs and Consumer Privacy Networks; User context data; plus Work-with-Databases / Web-Services / Pricing sections. All fetched 2026-06-06; resolve.
- **Date accessed**: 2026-06-06
- **Category**: vendor — **note**: recorded as vendor (provenance: MaxMind vendor documentation), but it *functions* as a foundations/methodology reference (the proxy taxonomy and accuracy caveats), not as abuse evidence. Minor category ambiguity, flagged.
- **Evidence basis**: capability-doc; vendor-claim — vendor documentation of its own data products' accuracy, limits, and detection capabilities. Not empirical measurement of abuse.
- **Operational proximity**: `capability`. It documents a detection *capability* (proxy/anonymizer classification, with accuracy estimates) and data methodology — it observes no abuse against any target. The accuracy figures and "hardest to detect" statements are vendor self-description, not measurement. Most of the accuracy/methodology content is effectively `n/a` to the abuse-proximity axis; `capability` is assigned for the proxy-detection capability claims.
- **Tags**: ip-geolocation, ip-intelligence, proxy-detection, residential-proxy, vpn, tor, network-origin, detection-signal, accuracy-limits, vendor, methodology

## What it claims / provides

**Geolocation accuracy (accuracy article):**
- IP geolocation is inherently imprecise; MaxMind does not guarantee 100% accuracy. Accuracy varies by country, distance, IP type (cellular vs broadband, IPv4 vs IPv6), and ISP practices.
- GeoIP data is never precise enough to identify a household, individual, or street address.
- For anonymizers/hosts, the data describes the *server running the VPN/host*, not the end-user — you can geolocate the web server but not the person behind it.
- Self-estimated accuracy: ~99.8% at country level; for US IPs, ~80% at state/region level and ~66% at city level (within a 50 km radius). Other-country accuracy via their comparison page.
- "Missing" IPs (no DB row) are often privacy opt-outs (or unrouted IPs); data-privacy regulation prevents confirming opt-out as the cause.
- Mobile, VPN, and consumer-privacy-network IPs are less precisely locatable; the data falls back to less-granular fields (e.g. country/subdivision only) rather than guessing city.
- Paid tiers add an accuracy radius and confidence factors (Enterprise DB, Insights web service) for fallback logic. Licence requires keeping databases up to date.

**Proxy detection and anonymous IP (proxy article):**
- Anonymizers hide the end-user's IP; all geolocation/intelligence for an anonymous IP corresponds to the host, not the end-user.
- Five anonymizer types are flagged: VPN, hosting providers, public proxies, **residential proxies**, and TOR exit nodes.
- Key admission: **residential proxies are harder to detect than other proxy types because their IPs appear to belong to legitimate residential ISPs.**
- Hosting-provider traffic is treated as a proxy signal in itself: end-user traffic from a hosting provider is probably a VPN even if not otherwise flagged.
- Advanced (paid: Anonymous Plus / Insights / minFraud) anonymizer signals: `provider_name` (e.g. named VPN services), `anonymizer_confidence` (1–99; e.g. 99 = precise match to a known anonymizing service, 30 = likely based on observation), and `network_last_seen` (to avoid blocking stale/reallocated IPs).
- Other privacy networks (e.g. Apple iCloud Private Relay) are noted as a distinct category.

## Signals or techniques mentioned

- Network-origin / IP-intelligence signal family: ASN / IP network data, hosting-vs-residential, connection type, user type (business/residential), domain, ISP, and the five-way anonymizer classification (VPN / hosting / public proxy / residential proxy / Tor).
- Reliability instrumentation: accuracy radius, confidence factors, `anonymizer_confidence` scoring, `network_last_seen` freshness.
- The load-bearing methodological caveat: anonymizer/host data describes the *server*, not the end-user — so an IP-origin signal locates the egress, not the actor.

## Threat types covered

`Not threat-specific` / cross-cutting. The material concerns IP-intelligence signals (network origin, proxy/VPN/Tor classification) that are inputs to many abuse types, not any single OAT. Relevant to the project as detection-signal *methodology and reliability*, not as abuse evidence.

## Framing distance

- **What real-world problem does it approximate?** The accuracy, limits, and product-level methodology of commercial IP-geolocation and IP-intelligence (incl. proxy/anonymizer) data — i.e. how reliable the network-origin signal class is, documented by a major vendor of that data.
- **What does it fail to represent?** It is vendor self-documentation: the accuracy figures are MaxMind's own estimates (not independently verified), and "residential proxies are harder to detect" is qualitative with no detection-rate or false-positive figures. It describes data products, not observed abuse — no prevalence, no bot-specific measurement. The five-type anonymizer taxonomy is MaxMind's framing.
- **What additional evidence would be needed to go further?** Independent validation of the accuracy/coverage estimates; detection-rate and false-positive data for residential-proxy classification specifically; and any prevalence figures (which this source does not attempt).

## What it cannot show

- It cannot show how prevalent any abuse is, nor any detection efficacy in the field — it is capability/accuracy documentation, not measurement.
- Residential-proxy detection is described as hard, but with **no quantified detection or false-positive rate** — the most decision-relevant number is precisely what's absent.
- The accuracy headline (99.8% country) is a vendor self-estimate, and degrades sharply below country level (≈66% US city within 50 km) — useful as a caution, not a guarantee.
- It is **not abuse evidence**; it is cross-cutting signal methodology only.
- Only the hub + two articles were read. The rest of the cluster (notably "Business VPNs and Consumer Privacy Networks", "IP network data", "User context data", "Geolocation coverage") is listed by title and **not characterised in detail** — extend this entry if any becomes load-bearing rather than assuming its contents.
- No actor/campaign content, no recipes — dual-use containment not engaged.

## Project impact

- **Foundations/methodology anchor for the network-origin & IP-intelligence signal class** — what IP→geo/ASN/proxy data can and cannot tell you, with the load-bearing caveat that anonymizer/host data locates the *server, not the end-user*. Gives the project concrete accuracy numbers (≈99.8% country → ≈66% city) to support the "signals are useful but imperfect / public-data limits" argument with a citable figure rather than a hand-wave.
- **The defender-tooling complement to the residential-proxy arms-race thread.** Where bad-asn-list (datacenter blocking), Wikimedia (residential proxies defeat IP limits), Thales (residential proxies + valid fingerprints), and FP-Agent (agents on residential networks) describe the *problem*, this documents the *commercial detection response*: a five-type anonymizer taxonomy with an explicit residential-proxy flag, confidence scoring, provider names, and last-seen freshness — plus the candid vendor admission that residential proxies are the hardest to detect because they look like legitimate residential ISPs. That admission, from a proxy-detection vendor, corroborates the arms-race framing from the detection side and closes the loop on the thread.
- Establishes that **proxy / datacenter / residential / VPN / Tor classification is a productized commercial signal** (Anonymous IP, Anonymous Plus, Insights, minFraud) — i.e. defenders buy this capability, they don't only hand-roll ASN lists like bad-asn-list.
- Possible methodology input for the project's own EDA framing of network-origin features and their reliability limits (accuracy radius, confidence, freshness as concepts).
- **Flags**: (1) vendor self-documentation — accuracy figures and "hardest to detect" are MaxMind's own and unverified; treat as capability/accuracy claims, not measurement; (2) only hub + 2 of the cluster's articles were read — the entry deliberately covers the cluster as one source but characterises only what was read; (3) category recorded as `vendor` though it functions as a foundations/methodology reference — a minor instance of the category-vocab strain noted elsewhere.
