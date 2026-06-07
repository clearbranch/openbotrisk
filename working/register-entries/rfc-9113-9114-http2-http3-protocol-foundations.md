# RFC 9113 and RFC 9114 - HTTP/2 and HTTP/3 protocol foundations

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded MHT captures:
  - `RFC 9113_ HTTP_2.mht`
  - `RFC 9113_ HTTP_2 _ RFC Editor.mht`
  - `RFC 9114_ HTTP_3.mht`
  - `Design Documents.mht`
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.
- **Source handling decision**: combine RFC 9113 and RFC 9114 into one protocol-foundation entry. Do not combine the Chromium Design Documents index with these RFCs; it belongs with the Chromium/browser-architecture sources.

## Bibliographic

### Canonical sources

- **Citation**: Thomson, M., & Benfield, C. (Eds.). (2022). *HTTP/2*. RFC 9113. Internet Engineering Task Force. https://doi.org/10.17487/RFC9113
- **Citation**: Bishop, M. (Ed.). (2022). *HTTP/3*. RFC 9114. Internet Engineering Task Force. https://doi.org/10.17487/RFC9114

### Uploaded captures

- `RFC 9113_ HTTP_2.mht` — canonical RFC text capture.
- `RFC 9113_ HTTP_2 _ RFC Editor.mht` — RFC Editor information/page capture for the same RFC. Treat as duplicate/supporting metadata, not a separate register row.
- `RFC 9114_ HTTP_3.mht` — canonical RFC text capture.
- `Design Documents.mht` — Chromium design-documents index. Related only as browser-architecture navigation; not part of this protocol-standard entry.

### Status

- RFC 9113 is Standards Track, published June 2022. It obsoletes RFC 7540 and RFC 8740.
- RFC 9114 is Standards Track, published June 2022.
- RFC 9113 should supersede the earlier local RFC 7540 register entry for current HTTP/2 claims.

## Category and treatment

- **Category**: foundations
- **Evidence basis**: protocol-standard / technical specification
- **Operational proximity**: foundational — defines protocol mechanics and terminology; not observed abuse evidence, not bot-detection evidence, and not control-effectiveness evidence.
- **Tags**: RFC9113, RFC9114, HTTP/2, HTTP/3, IETF, protocol-standard, HTTP-semantics, binary-framing, streams, multiplexing, flow-control, QPACK, HPACK, QUIC, ALPN, h2, h3, request-response, protocol-foundations, protocol-fingerprinting-context

## What the sources claim

### RFC 9113 / HTTP/2

- HTTP/2 is an optimized expression of HTTP semantics.
- It improves network efficiency and reduces latency through field compression and multiple concurrent exchanges on the same connection.
- It obsoletes RFC 7540 and RFC 8740.
- It defines HTTP/2 version identification, connection setup, connection preface, frames, streams, multiplexing, flow control, priority signalling, error handling, frame types, HTTP semantic mapping, and HTTP/2 security considerations.

### RFC 9114 / HTTP/3

- HTTP/3 maps HTTP semantics over QUIC.
- QUIC provides features desirable for HTTP transport, including stream multiplexing, per-stream flow control, and low-latency connection establishment.
- HTTP/3 identifies which HTTP/2 features are subsumed by QUIC and how HTTP/2 extensions can be ported to HTTP/3.
- It defines connection setup, endpoint discovery, connection reuse, HTTP semantic mapping, stream mapping, HTTP/3 frame layout, frame types, error handling, extensions, security considerations, and IANA registrations.

## What evidence it provides

This is a pair of **primary protocol specifications**, not empirical or threat sources.

They provide:

- formal terminology for HTTP/2 and HTTP/3;
- protocol mechanics for frames, streams, flow control, and multiplexing;
- HTTP semantics over different transports;
- connection setup and protocol identification details;
- HTTP/2 over TLS and HTTP/3 over QUIC background;
- security considerations including denial of service, cross-protocol attacks, intermediary encapsulation, compression, padding/traffic analysis, privacy, and early data/migration concerns for HTTP/3.

They do **not** provide:

- bot-detection methodology;
- anti-bot controls;
- abuse prevalence;
- traffic measurements;
- scraper or bot capability evidence;
- fingerprinting taxonomy;
- TLS/HTTP/2/HTTP/3 fingerprinting measurements;
- implementation behaviour across browsers, proxies, scrapers, or anti-bot products;
- evidence that protocol-level fingerprints distinguish humans from bots.

## Details most relevant to openbotrisk

### Protocol version and transport matter

HTTP/2 and HTTP/3 preserve HTTP semantics but change the protocol representation and transport behaviour.

**Project use:** supports the foundations layer. A web client is not just “making HTTP requests”; it has protocol-version behaviour that may matter for observability, compatibility, and later fingerprinting discussions.

### HTTP/2: frames, streams, and multiplexing

HTTP/2 uses frames and streams to allow multiple concurrent exchanges on the same connection.

**Project use:** useful for explaining why HTTP/2 behaviour differs from older HTTP/1.x request/connection assumptions.

### HTTP/3: HTTP over QUIC

HTTP/3 maps HTTP semantics over QUIC, with QUIC handling stream multiplexing, per-stream flow control, and low-latency connection establishment.

**Project use:** useful foundation for explaining why HTTP/3 is not simply “HTTP/2 with a new version number”. QUIC changes the transport substrate.

### Protocol fingerprinting context

These RFCs do not describe bot detection, but they help ground sources that later discuss ALPN, TLS/JA4, HTTP/2 behaviour, HTTP/3/QUIC behaviour, and protocol-level coherence.

**Project use:** cite as background only when introducing protocol-level signal families. Do not cite as evidence that protocol-level signals work for bot detection.

## Signals or techniques mentioned

- HTTP/2 frames;
- HTTP/3 frames;
- binary framing;
- streams;
- stream identifiers;
- stream concurrency;
- flow control;
- field/header compression;
- HPACK context for HTTP/2 via referenced compression model;
- QPACK context for HTTP/3 via HTTP/3 field compression references;
- SETTINGS;
- DATA;
- HEADERS;
- PUSH_PROMISE;
- PING;
- GOAWAY;
- WINDOW_UPDATE;
- CONTINUATION;
- ALPN / protocol identification context;
- `h2`;
- `h3`;
- QUIC;
- connection reuse;
- connection closure;
- error codes;
- server push;
- denial-of-service considerations;
- cross-protocol attacks;
- intermediary encapsulation attacks;
- padding and traffic analysis;
- early data;
- migration;
- privacy considerations.

## Threat types covered

These RFCs are not automated-abuse taxonomies.

Directly covered at protocol-security level:

- denial-of-service considerations;
- cross-protocol attacks;
- intermediary encapsulation attacks;
- compression-related risks;
- traffic-analysis/privacy considerations;
- early-data and migration concerns for HTTP/3.

Indirect relevance to openbotrisk:

- OAT-015 Denial of Service, where HTTP/2 or HTTP/3 connection/stream behaviour can influence resource-exhaustion patterns;
- protocol fingerprinting and client-coherence foundations;
- scraper/browser consistency, where implementation details may need to align with claimed browser identity.

Weak or no direct relevance:

- credential stuffing;
- account takeover;
- ticket bots;
- appointment-slot abuse;
- scalping;
- sniping;
- CAPTCHA bypass;
- AI agents.

## What is strong

- Primary standards-track protocol sources.
- Current HTTP/2 source superseding RFC 7540.
- Strong foundation for protocol terminology.
- Useful for accurate explanations of HTTP/2/HTTP/3 frames, streams, multiplexing, flow control, and transport differences.
- Useful background before reading sources on TLS fingerprints, HTTP/2 fingerprints, HTTP/3/QUIC behaviour, and browser/client coherence.

## What is weak or limited

- Not bot or abuse sources.
- Not detection sources.
- Not implementation surveys.
- Not traffic-measurement sources.
- They do not describe browser automation, anti-detect browsers, residential proxies, managed scraping APIs, or AI agents.
- They do not measure protocol fingerprints or evasion.
- They do not show how Chrome, Firefox, Safari, Playwright, Puppeteer, curl, requests, or proxy services behave in practice.
- RFC 9113 and RFC 9114 define protocol behaviour; real-world client fingerprinting requires implementation and traffic evidence.

## Framing distance

- **What real-world bot/abuse problem do these sources approximate?**  
  The protocol substrate on which browsers, scrapers, bots, APIs, proxies, and anti-bot systems communicate. They help explain what the observable protocol layer is.

- **What do they fail to represent?**  
  They do not represent attacker behaviour, defender detection practice, protocol fingerprinting datasets, or live traffic. They define protocol mechanics, not observed misuse.

- **What additional evidence would be needed to go further?**  
  Client-implementation studies, TLS/JA4 and HTTP/2/HTTP/3 fingerprinting papers, vendor detection docs, scraper-side capability sources, browser automation documentation, and real traffic datasets.

## What it cannot show

- It cannot show that HTTP/2 or HTTP/3 features are used by bots.
- It cannot show bot prevalence.
- It cannot show detection performance.
- It cannot show that HTTP/2 or HTTP/3 fingerprinting works.
- It cannot show that a client is human or automated.
- It cannot show specific scraper or browser-automation capability.
- It cannot replace implementation-specific sources.

## Project impact

Use this as a **combined protocol-foundation entry**.

Best uses:

- replace/demote the older RFC 7540 entry for current HTTP/2 references;
- explain HTTP/2 and HTTP/3 basics;
- support protocol-layer discussion;
- ground ALPN/protocol-version references in TLS and client-fingerprint sources;
- explain frames, streams, multiplexing, flow control, QUIC, and protocol security considerations.

Do not use it as:

- threat evidence;
- bot-detection evidence;
- scraper/bot capability evidence;
- observed-use evidence;
- vendor-performance evidence.

## Relationship to other register entries

- **RFC 7540 HTTP/2**: keep only as historical if needed; RFC 9113 is the current replacement.
- **MDN HTTP foundations**: MDN is easier for readers; RFCs are formal protocol references.
- **Jarad & Bıçakcı JA4/TLS**: RFCs provide protocol background; JA4 paper provides a bounded detection-method example.
- **Cloudflare Detection IDs / bot detection engines**: vendor sources discuss operational detection/coherence checks; RFCs provide protocol mechanics only.
- **ScrapingBee bypass guides**: scraper-side sources discuss practical capability/evasion framing; RFCs are neutral standards.
- **ASVS HTTP message validation**: ASVS turns protocol-version issues into application-security requirements; RFCs define protocol behaviour.

## Note on Chromium Design Documents

The uploaded `Design Documents.mht` should **not** be included in this RFC entry except as a source-handling note.

Recommended handling:

- merge it into the existing `chromium-multi-process-architecture` entry as a supporting index/navigation source; or
- create a very low-priority `chromium-design-documents-index` entry only if you want a register row for the index itself.

It should not be treated as evidence for HTTP/2 or HTTP/3. The Chromium index is browser-architecture navigation, not a protocol standard.

## Dual-use containment

Low dual-use. These are public protocol standards. The main risk is over-interpretation: do not infer bot-detection capability from protocol definitions alone.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `rfc-9113-9114-http2-http3-protocol-foundations` |
| Title | *HTTP/2* and *HTTP/3* |
| Organisation / authors | IETF / Thomson, Benfield, Bishop |
| Year | 2022 |
| Category | foundations |
| Evidence basis | protocol-standard / technical specification |
| Operational proximity | foundational |
| Signals / techniques | HTTP/2; HTTP/3; frames; streams; multiplexing; flow control; field compression; QUIC; ALPN; h2; h3; server push; protocol security considerations |
| Threat types | protocol-level DoS/security considerations only; indirect relevance to protocol fingerprinting and client coherence |
| Project use | Protocol foundation for HTTP/2 and HTTP/3 mechanics and later protocol-layer detection discussions |
| Main caution | Not bot-abuse, prevalence, implementation-behaviour, or detection-performance evidence |
| Entry file | `rfc-9113-9114-http2-http3-protocol-foundations.md` |
