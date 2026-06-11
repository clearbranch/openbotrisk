# Choi et al. (2020) - Understanding the Proxy Ecosystem

## Extraction run metadata

- **Extraction date**: 2026-06-07
- **Extraction agent**: ChatGPT
- **Model name + version, if known**: GPT-5.5 Thinking
- **Source access**: uploaded PDF `SRC-089-choi-2020-understanding-proxy-ecosystem.pdf`.
- **Prompt version**: newer register/source-extraction pattern used in this conversation, including evidence basis, operational proximity, framing distance, limits, project impact, and dual-use containment.

## Bibliographic

- **Citation**: Choi, J., Abuhamad, M., Abusnaina, A., Anwar, A., Alshamrani, S., Park, J., Nyang, D., & Mohaisen, D. (2020). *Understanding the Proxy Ecosystem: A Comparative Analysis of Residential and Open Proxies on the Internet*. IEEE Access. https://doi.org/10.1109/ACCESS.2020.3000959
- **Source URL or path**: uploaded PDF `SRC-089-choi-2020-understanding-proxy-ecosystem.pdf`.
- **Publication status**: accepted IEEE Access article; PDF text notes it had been accepted for publication and not fully edited at capture.
- **Category**: academic
- **Evidence basis**: empirical-measurement / infrastructure-analysis
- **Operational proximity**: measured — analyses large open-proxy and residential-proxy datasets and blacklist overlap; not direct evidence of a specific web-abuse campaign.
- **Tags**: proxies, residential-proxies, open-proxies, proxy-ecosystem, blacklists, IP-reputation, geolocation, ASN, spam, malicious-activity, attack-source, censorship, internet-freedom, proxy-infrastructure, evasion-infrastructure

## What it claims

- Proxies are dual-use infrastructure: they can support privacy, censorship circumvention, caching, and access to restricted information, but can also help adversaries hide identity and launch attacks.
- Open proxies and residential proxies pursue similar functional goals but have different operational characteristics.
- Open proxies are publicly accessible and often easy to blacklist.
- Residential proxies use IP addresses assigned by general ISPs, making requests appear more like ordinary residential-user traffic.
- Residential proxies are usually operated in a closed/paid-access fashion.
- Residential and open proxies have distinct geographic, city-level, ASN-level, and blacklist profiles, so they should be analysed separately.
- Proxy locality correlates with broader country-level characteristics such as Internet censorship, Internet freedom, political stability, Internet speed, and GDP.

## What evidence it provides

The paper provides a comparative empirical analysis of open and residential proxy datasets.

### Dataset scale

| Dataset | Size |
|---|---:|
| Open proxies | 1,045,468 unique IP addresses |
| Residential proxies | 6,419,987 IP addresses |
| Combined proxy total | 7,465,455 IP addresses |
| Residential dataset source period | July 2017 to March 2018 |
| Open-proxy collection period | around November 2019 |
| Blacklist services used | 27 |

Open proxies were collected from IP2Proxy and public open-proxy-list sources. Residential proxies were obtained from the earlier Mi et al. residential-proxy dataset.

### Geospatial and ASN analysis

The paper analyses:

- country-level proxy distribution;
- city-level proxy distribution;
- autonomous-system-level distribution;
- overlap between open-proxy and residential-proxy datasets;
- country-level correlations with censorship, Internet freedom, political stability, Internet speed, and GDP.

Important reported examples:

- China and the United States together account for about 28.7% of open proxies.
- Turkey and India are the top two countries for residential proxies in the dataset.
- Turkey contains 528,032 residential proxies but only 5,040 open proxies.
- The top 10 countries account for nearly 70% of open proxies but only 46.8% of residential proxies, implying residential proxies are more geographically dispersed.
- Istanbul and Ankara together dominate Turkey’s residential-proxy distribution in the dataset.
- Some ASNs contain substantial concentrations of proxies.

### Blacklist and malicious-behaviour analysis

The paper uses 27 blacklist services to classify proxies as blacklisted and to identify spam, attack, and vulnerability-related categories.

Headline results:

| Measure | Open proxies | Residential proxies |
|---|---:|---:|
| Blacklisted | 827,106 / 79.11% | 5,700,244 / 86.04% |
| Spam | 295,152 / 28.23% | 1,081,779 / 16.85% |
| Attack | 72,914 / 6.97% | 17,596 / 0.27% |
| Vulnerable | 21,035 / 2.01% | 165,328 / 2.58% |

The paper reports that 79.11% of open proxies and 86.04% of residential proxies were present on at least one blacklist. It also reports that 28.23% of open proxies and 16.85% of residential proxies were used for spam, while 6.97% of open proxies and 0.27% of residential proxies were associated with verified attacks.

## Signals or techniques mentioned

- open proxies;
- residential proxies;
- ISP-assigned residential IP addresses;
- data-centre IP addresses;
- public open-proxy lists;
- proxy IP collection;
- IP geolocation;
- city-level distribution;
- country-level distribution;
- autonomous-system-number distribution;
- blacklists / DNSBL-style services;
- spam classification;
- attack-source classification;
- vulnerability/exploitable-host classification;
- IP-reputation;
- proxy blacklisting;
- AUTH attacks / credential reuse attempts;
- dynamic IP address reassignment;
- censorship circumvention;
- anonymity / IP masking.

## Threat types covered

Directly covered:

- proxy-assisted anonymity / identity hiding;
- spam infrastructure;
- malicious proxy behaviour;
- attack-source blacklisting;
- AUTH attacks / credential-reuse attempts as described by blacklist service categories;
- vulnerable or exploitable proxy hosts;
- proxy use in censorship circumvention and regional bypass.

Indirect OAT mappings:

- OAT-008 Credential Stuffing — proxies can support distributed login attempts, but this paper only touches AUTH/credential reuse through blacklist categories.
- OAT-011 Scraping — proxies are relevant infrastructure, but scraping is not directly measured.
- OAT-019 Account Creation — proxies are relevant infrastructure, not directly measured.
- OAT-005 Scalping / OAT-013 Sniping — proxies are relevant infrastructure, not directly measured.
- OAT-015 Denial of Service — proxies may support attacks, but this paper does not model application-layer DoS workflows.
- OAT-017 Spamming — strongest direct mapping.

## What is strong

- Strong academic infrastructure source for the proxy ecosystem.
- Useful for distinguishing open proxies from residential proxies.
- Useful empirical support for why residential proxies are harder to reason about than data-centre/open proxies: they use ISP/residential address space and are more dispersed.
- Strong quantitative source for blacklist overlap by proxy type.
- Useful bridge between simple IP-address foundations and current anti-bot sources that discuss IP reputation, residential proxies, and proxy rotation.
- Good source for explaining why IP-based defences are partial: proxies are widespread, geographically distributed, and not all proxy categories behave the same.
- Useful because it includes multiple levels: country, city, ASN, blacklist category.

## What is weak or limited

- Data is not current: residential data comes from 2017–2018, open-proxy and blacklist analysis from around 2019.
- The paper does not measure current commercial proxy providers, mobile proxies, modern residential proxy networks, browser automation, anti-detect browsers, or AI-agent traffic.
- Blacklist presence is an imperfect proxy for malicious behaviour.
- The residential-proxy blacklist analysis has a timing mismatch: residential IPs were observed in 2017–2018, while blacklist checks were performed later. An IP may have changed role by the time it was blacklisted.
- The paper does not directly observe abuse workflows such as scraping, credential stuffing, ticket bots, or slot sniping.
- It does not measure success rates against anti-bot systems.
- It does not provide real-time proxy detection methodology for defenders.
- It treats blacklist categories as indicators, not ground-truth labels.

## Framing distance

- **What real-world bot/abuse problem does this source approximate?**  
  The proxy infrastructure layer that can support automated abuse by masking or varying apparent client IP origin. It is closest to infrastructure availability, IP reputation, and geospatial/ASN distribution.

- **What does it fail to represent?**  
  It does not represent a complete bot campaign, an attacker business model, or a protected-site evasion test. It does not show how proxies are combined with browser automation, CAPTCHA solving, credential stuffing, scraping APIs, or anti-detect browsers.

- **What additional evidence would be needed to go further?**  
  Current proxy-provider documentation, vendor telemetry on proxy-origin bot traffic, abuse-case reports, residential-proxy measurement updates, law-enforcement/legal cases, and controlled tests of proxy networks against anti-bot systems.

## What it cannot show

- It cannot show current residential-proxy market structure.
- It cannot show current proxy prevalence in bot attacks.
- It cannot show that a given proxy provider is malicious.
- It cannot show that proxy use equals bot abuse.
- It cannot show that blacklisted IPs were malicious at the same time they acted as proxies.
- It cannot show scraping, scalping, sniping, credential-stuffing, or account-creation workflows directly.
- It cannot show anti-bot detection effectiveness.

## Project impact

Use this as a **proxy-ecosystem infrastructure source**.

Best uses:

- explain the difference between open proxies and residential proxies;
- support the claim that proxy infrastructure is widespread and geographically/ASN distributed;
- support the idea that residential IP origin complicates simple IP-based blocking;
- provide empirical context for IP reputation and blacklist-based defences;
- connect proxy infrastructure to spam and malicious activity indicators;
- bridge older academic proxy measurement to modern vendor/scraper-side sources.

Do not use it as:

- observed evidence of scraping or credential-stuffing campaigns;
- current market evidence for 2026 proxy providers;
- proof that residential proxy use is inherently malicious;
- proof that blacklists are accurate;
- detection-performance evidence.

## Relationship to other register entries

- **MDN IP/HTTP foundations if added**: this paper gives empirical proxy context beyond basic IP definitions.
- **Cloudflare/HUMAN/DataDome**: vendor sources may discuss residential proxies and IP reputation in current defensive systems; this paper provides older academic measurement context.
- **ScrapingBee/Bright Data/Oxylabs proxy-service entries if added**: those are commercial capability/market sources; this is academic measurement.
- **OWASP OAT / Handbook**: proxies are infrastructure used across OAT categories, not an OAT category by themselves.
- **PortSwigger credential-stuffing/authentication sources**: proxies help explain why IP-based login controls are limited, but this paper does not measure credential stuffing.
- **Jarad JA4/TLS**: proxies change apparent IP origin; TLS/protocol fingerprints can add another signal family when IP alone is weak.

## Dual-use containment

Moderate dual-use. The paper discusses proxy sources, geolocation, blacklists, and malicious classifications. In project use, keep it at the infrastructure and measurement level. Avoid converting it into a guide for sourcing, selecting, or operationalising proxies.

## Suggested register row

| Field | Value |
|---|---|
| Register id | `choi-2020-understanding-proxy-ecosystem` |
| Title | *Understanding the Proxy Ecosystem: A Comparative Analysis of Residential and Open Proxies on the Internet* |
| Authors | Jinchun Choi; Mohammed Abuhamad; Ahmed Abusnaina; Afsah Anwar; Sultan Alshamrani; Jeman Park; Daehun Nyang; David Mohaisen |
| Year | 2020 |
| Category | academic |
| Evidence basis | empirical-measurement / infrastructure-analysis |
| Operational proximity | measured |
| Signals / techniques | open proxies; residential proxies; proxy IPs; geolocation; ASN; blacklists; spam; attack-source; IP reputation |
| Threat types | proxy-assisted abuse infrastructure; spam; indirect support for scraping, credential stuffing, account creation, scalping/sniping |
| Project use | Academic proxy-ecosystem source for IP origin, residential proxies, blacklisting, and infrastructure distribution |
| Main caution | Older datasets and blacklist labels; not direct evidence of current bot abuse or anti-bot evasion effectiveness |
| Entry file | `choi-2020-understanding-proxy-ecosystem.md` |
