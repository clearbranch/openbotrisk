# How visitor recognition becomes bot detection

## Plain explanation

Bot detection is not usually a perfect yes/no decision.

It is usually a risk judgement based on many signals.

The question is not only:

> Is this a bot?

It is often more like:

> What kind of traffic is this, how risky is it, and what should the site do with it?

## Four broad traffic categories

A website may want to separate traffic into rough categories:

1. **Normal human users**  
   People browsing, logging in, buying, reading, or using the site normally.

2. **Good bots**  
   Search engines, monitoring tools, accessibility tools, partner crawlers, or verified agents that the site wants to allow.

3. **Unknown automation**  
   Scripts, crawlers, browser automation, scraping tools, or agents whose purpose is unclear.

4. **Bad bots / abusive automation**  
   Credential stuffing, scraping, fake account creation, scalping, carding, inventory hoarding, spam, fraud, or account takeover.

## Common signal groups

Bot systems may use:

- IP and network reputation
- ASN, datacentre, residential, mobile, VPN, or proxy classification
- request headers
- cookies and session history
- browser/device fingerprints
- TLS or protocol fingerprints
- JavaScript challenge results
- mouse/keyboard/touch behaviour
- request timing and rate
- account history
- endpoint context, such as login versus public page
- known good bot verification
- known bad fingerprints or detection IDs

## From signal to action

A bot system may respond in different ways:

- allow
- block
- rate limit
- challenge
- ask for stronger authentication
- log only
- serve different content
- skip protection for verified bots
- send a risk score to the origin application

This matters because “bot detection” is not just detection. It is also response policy.

## Why false positives matter

A false positive means a real user is treated as a bot.

That can block customers, break login, stop purchases, or damage trust.

This is why many systems use risk scores and graduated responses instead of always blocking.

## Why false negatives matter

A false negative means abusive automation is allowed through.

That can lead to scraping, account takeover, fake accounts, payment fraud, scalping, or inflated infrastructure cost.

## Why attackers adapt

If a website blocks obvious scripts, attackers may move to:

- realistic headers
- browser automation
- stealth plugins
- undetected drivers
- residential proxies
- CAPTCHA solvers
- cloud browsers
- persistent profiles
- AI browser agents

That is why the project needs a simple-to-complex automation taxonomy.

## Project use

This page should introduce the advanced evidence set:

- Cloudflare bot scores and detection IDs
- DataDome intent-based detection
- HUMAN cyberfraud and agentic traffic
- Kasada proof-of-execution and retooling
- Arkose dynamic challenges
- academic behavioural and fingerprinting studies
- automation supply-side sources
