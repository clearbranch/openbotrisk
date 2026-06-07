# RFC 7540 - Hypertext Transfer Protocol Version 2 (HTTP/2)

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded MHT capture of the RFC Editor page `RFC 7540_ Hypertext Transfer Protocol Version 2 (HTTP_2) _ RFC Editor.mht`; official RFC Editor pages for RFC 7540 and RFC 9113 checked for current status.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.

## Bibliographic

- **Citation**: Belshe, M., Peon, R., & Thomson, M. (Ed.). (2015). *Hypertext Transfer Protocol Version 2 (HTTP/2)*. RFC 7540. Internet Engineering Task Force. https://doi.org/10.17487/RFC7540
- **Source URL or path**: uploaded MHT capture of RFC Editor page; canonical RFC Editor URL: `https://www.rfc-editor.org/rfc/rfc7540.html`
- **Publication date**: May 2015.
- **Current status note**: RFC 7540 has been obsoleted by RFC 9113. Treat RFC 7540 as a historical/foundation source unless specifically discussing the original HTTP/2 specification. For current HTTP/2 specification wording, use RFC 9113.
- **Category**: foundations
- **Evidence basis**: protocol-standard / technical specification
- **Operational proximity**: foundational — defines protocol mechanics and terminology; not observed abuse evidence, not bot-detection evidence, and not control-effectiveness evidence.
- **Tags**: RFC7540, HTTP/2, IETF, RFC, protocol-standard, binary-framing, streams, multiplexing, flow-control, HPACK, header-compression, ALPN, h2, h2c, server-push, request-response, HTTP-semantics, protocol-foundations

## What it claims

- HTTP/2 is an optimized expression of HTTP semantics.
- HTTP/2 aims to make more efficient use of network resources and reduce perceived latency.
- It introduces header field compression and allows multiple concurrent exchanges on the same connection.
- It introduces unsolicited server push of representations from servers to clients.
- HTTP semantics remain largely unchanged; HTTP/2 changes how those semantics are represented over a connection.
- HTTP/2 uses binary message framing rather than the textual message syntax associated with HTTP/1.x.
- HTTP/2 keeps compatibility with the same `http` and `https` URI schemes and default ports used by HTTP/1.1.
- The original RFC defines protocol identifiers:
  - `h2` for HTTP/2 over TLS using ALPN;
  - `h2c` for cleartext HTTP/2.
- RFC 7540’s original priority scheme later proved problematic and was deprecated by RFC 9113.

## What evidence it provides

This is a **primary protocol specification**, not a research or telemetry source.

It provides:

- definitions of HTTP/2 frames, streams, connections, endpoints, stream errors, and connection errors;
- starting mechanisms for HTTP/2, including ALPN and upgrade/prior-knowledge paths in RFC 7540;
- frame format and frame types;
- stream multiplexing model;
- flow control and prioritisation model as originally defined;
- HTTP header field handling and compression framing;
- server push model;
- HTTP/2 error handling;
- security and privacy considerations.

It does **not** provide:

- bot-detection methodology;
- anti-bot controls;
- abuse prevalence;
- traffic measurements;
- evidence of scraper or bot capability;
- fingerprinting taxonomy;
- TLS or HTTP/2 fingerprinting detection methods;
- modern HTTP/2 implementation behaviour across browsers, proxies, scrapers, or anti-bot products.

## Details most relevant to openbotrisk

### Protocol layer matters

HTTP/2 changes the wire representation of ordinary HTTP interactions. The method/status/header/body semantics remain HTTP, but the transport representation uses frames and streams.

**Project use:** this supports the foundations layer: a bot detector or scraper does not only interact with “HTTP” in the abstract. The protocol version and framing layer can matter.

### Multiplexing and streams

HTTP/2 associates each request/response exchange with a stream. Multiple streams can share one connection, so blocked or stalled work on one stream does not necessarily block progress on other streams.

**Project use:** useful for explaining why HTTP/2 traffic is not just “one request equals one connection”. Concurrency can occur inside a single connection.

### Header compression

HTTP/2 compresses header-containing frames. RFC 7540 references header compression/decompression, while HPACK is separately specified in RFC 7541.

**Project use:** useful background for why HTTP/2 can expose different protocol-level behaviour from HTTP/1.1. However, this RFC alone should not be used to claim specific fingerprinting or bot-detection methods.

### ALPN and protocol identifiers

RFC 7540 defines the `h2` identifier for HTTP/2 over TLS, used in the TLS Application-Layer Protocol Negotiation extension. It also defines `h2c` for cleartext HTTP/2.

**Project use:** relevant to TLS/JA4 and protocol-fingerprint entries, because ALPN appears in TLS handshake and fingerprinting sources. The RFC explains the protocol identifier, not the detection technique.

### Security considerations

RFC 7540 includes security considerations such as server authority, cross-protocol attacks, intermediary encapsulation attacks, cacheability of pushed responses, denial-of-service considerations, compression, padding, and privacy.

**Project use:** useful background for HTTP/2 security, especially DoS/resource-exhaustion framing. It is not enough on its own for modern HTTP/2 abuse or bot-detection claims.

## Current-status caveat

This source should be handled carefully because RFC 9113 now obsoletes RFC 7540 and RFC 8740.

Important updates in RFC 9113 include:

- deprecation of the RFC 7540 priority signalling scheme;
- removal/obsolescence of the HTTP/1.1 Upgrade path and `h2c` upgrade token;
- narrower and more precise validation rules for field names and values;
- clearer treatment of connection-specific header fields;
- clarification that `Host` and `:authority` must not disagree.

For final register use, consider either:

1. keep this as `rfc-7540-http2` with a clear “historical / obsoleted” caveat; or
2. replace/add `rfc-9113-http2` as the current HTTP/2 standard source.

## Signals or techniques mentioned

- HTTP/2 frames;
- binary framing;
- stream multiplexing;
- stream identifiers;
- stream concurrency;
- flow control;
- priority signalling, as originally defined;
- SETTINGS frames;
- HEADERS frames;
- DATA frames;
- PUSH_PROMISE frames;
- PING;
- GOAWAY;
- WINDOW_UPDATE;
- CONTINUATION;
- header compression;
- ALPN `h2`;
- cleartext `h2c`;
- HTTP2-Settings header field;
- server push;
- connection reuse;
- TLS requirements;
- denial-of-service considerations;
- padding and privacy considerations.

## Threat types covered

RFC 7540 is not an automated-abuse taxonomy.

Directly covered at protocol-security level:

- denial-of-service considerations;
- cross-protocol attacks;
- intermediary encapsulation attacks;
- compression-related risks;
- privacy considerations.

Indirect relevance to openbotrisk:

- OAT-015 Denial of Service, where HTTP/2 connection/stream/header behaviour can influence resource-exhaustion patterns;
- protocol fingerprinting and bot-detection foundations, where HTTP/2 behaviour can be part of a client fingerprint;
- scraper/browser consistency, where HTTP/2 implementation details may need to align with claimed browser identity.

Weak or no direct relevance:

- credential stuffing;
- scraping as a business process;
- account takeover;
- ticket bots;
- slot sniping;
- CAPTCHA bypass;
- AI agents.

## What is strong

- Primary technical standard.
- Authoritative source for original HTTP/2 terminology and mechanisms.
- Useful for foundations pages explaining frames, streams, multiplexing, ALPN, and header compression.
- Useful for grounding protocol-level discussion before introducing TLS/HTTP/2 fingerprinting sources.
- Useful for explaining why HTTP/2 traffic differs structurally from HTTP/1.1 traffic.

## What is weak or limited

- Obsoleted by RFC 9113.
- Not a bot or abuse source.
- Not a detection source.
- Not current enough to be the only HTTP/2 standard citation.
- Does not discuss commercial bot-management systems.
- Does not discuss browser automation, residential proxies, anti-detect browsers, or AI agents.
- Does not show how HTTP/2 is implemented by real browsers or scrapers.
- Does not measure HTTP/2 fingerprinting or evasion.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  The protocol substrate on which web clients, browsers, scrapers, and bots may communicate. It helps explain what HTTP/2 is and why protocol-level behaviour can be observable.

- **What does it fail to represent?**  
  It does not represent attacker behaviour, defender detection practice, protocol fingerprinting datasets, or real traffic. It defines protocol mechanics rather than observed misuse.

- **What additional evidence would be needed to go further?**  
  RFC 9113 for current HTTP/2; RFC 7541/HPACK and later compression/security material for header compression; TLS/JA4 and HTTP/2 fingerprinting papers for detection; vendor docs for operational detection; scraper-side sources for public evasion/capability claims; real traffic datasets for empirical evidence.

## What it cannot show

- It cannot show that HTTP/2 features are used by bots.
- It cannot show bot prevalence.
- It cannot show detection performance.
- It cannot show that HTTP/2 fingerprinting works.
- It cannot show that a client is human or automated.
- It cannot show current HTTP/2 behaviour after RFC 9113 changes.
- It cannot replace RFC 9113 for current specification wording.

## Project impact

Use this as a **protocol-foundation entry**, with the obsolescence caveat clearly visible.

Best uses:

- explain HTTP/2 basics;
- support protocol-layer discussion;
- explain ALPN `h2` in TLS fingerprinting context;
- explain why HTTP/2 has frames, streams, multiplexing, and header compression;
- provide historical context for HTTP/2 mechanisms that later appear in fingerprinting and bot-detection sources.

Do not use it as:

- threat evidence;
- bot-detection evidence;
- current HTTP/2 authority without checking RFC 9113;
- evidence of scraper or bot capability;
- evidence of production deployment or prevalence.

## Relationship to other register entries

- **MDN HTTP foundations**: MDN is better for approachable explanation; RFC 7540 is the formal original standard.
- **RFC 9113**: current HTTP/2 specification and should be preferred for current normative claims.
- **Jarad & Bıçakcı JA4/TLS entry**: ALPN/protocol features in TLS fingerprints connect to HTTP/2, but RFC 7540 itself does not perform detection.
- **Cloudflare Detection IDs / bot detection engines**: vendor sources show operational coherence checks; RFC 7540 provides protocol background only.
- **ScrapingBee PerimeterX/HUMAN bypass guide**: attacker-side sources mention HTTP header/TLS coherence; RFC 7540 provides formal background, not evasion detail.

## Dual-use containment

Low dual-use. This is a public protocol specification. The main risk is over-interpretation, not operational harm. Keep it as protocol background and do not infer bot-detection capability from the specification alone.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `rfc-7540-http2` |
| Title | *Hypertext Transfer Protocol Version 2 (HTTP/2)* |
| Organisation / authors | IETF / Belshe, Peon, Thomson |
| Year | 2015 |
| Category | foundations |
| Evidence basis | protocol-standard / technical specification |
| Operational proximity | foundational |
| Signals / techniques | HTTP/2 frames; streams; multiplexing; flow control; ALPN h2; h2c; header compression; server push |
| Threat types | protocol-level DoS/security considerations only; indirect relevance to protocol fingerprinting |
| Project use | Protocol foundation for HTTP/2 mechanics and protocol-layer detection discussions |
| Main caution | Obsoleted by RFC 9113; not bot-abuse, prevalence, or detection-performance evidence |
| Entry file | `rfc-7540-http2.md` |
