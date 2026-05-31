# EDA: Web Robot Sessions

## Access
Source: Figshare dataset 3477932 (web robot detection, session-level features + raw HTTP logs).

Underlying logs are from the Aristotle University of Thessaloniki library OPAC (`search.lib.auth.gr`), captured in early 2018 (per timestamps in `public_v2.json`).

Local path: `/home/tsispace/Documents/GitHub/openbotrisk/data/web-robot-sessions`

File formats: CSV (engineered session features) + JSON (raw per-request log).

Date inspected: 2026-05-23.

Files on disk:
- `public_v2.json` — 3.0 GB
- `semantic_features.csv` — 4.1 MB
- `simple_features.csv` — 15.2 MB

## Structure
- `simple_features.csv`: 67,352 rows x 32 cols. One row = one web session. HTTP/behavioural features + binary `ROBOT` label.
- `semantic_features.csv`: 67,352 rows x 7 cols. One row = one web session. Page-topic/semantic features + binary `ROBOT` label.
- `public_v2.json`: ~3.0 GB. Raw per-request log as a single JSON object keyed by request ID (Elasticsearch-style). Each value is a dict with HTTP request fields. Not loaded fully; only the first 100 entries were stream-parsed for schema inspection.
- Join key: `ID` links `simple_features` and `semantic_features` (67,352 / 67,352 session IDs overlap = 100%). The session `ID` is the parent key under which raw requests are grouped in the source logs; raw JSON uses request-level IDs (not session IDs) so direct session<->raw-request join would require an external mapping not included here.

## Schema
### `simple_features` (32 columns)

| column | dtype | example | description |
|---|---|---|---|
| `ID` | object | `obSnwGoBCue8G08E_WCX` | Session id (join key) |
| `NUMBER_OF_REQUESTS` | int64 | `79` | Number of HTTP requests in session |
| `TOTAL_DURATION` | int64 | `592` | Session duration (seconds) |
| `AVERAGE_TIME` | float64 | `7.5897436` | Mean inter-request interval (s) |
| `STANDARD_DEVIATION` | float64 | `1.8005404` | Std of inter-request interval (s) |
| `REPEATED_REQUESTS` | float64 | `0.0` | Fraction of repeated resource requests |
| `HTTP_RESPONSE_2XX` | float64 | `0.8734177215189873` | Fraction of 2xx responses |
| `HTTP_RESPONSE_3XX` | float64 | `0.1265822784810126` | Fraction of 3xx responses |
| `HTTP_RESPONSE_4XX` | float64 | `0.0` | Fraction of 4xx responses |
| `HTTP_RESPONSE_5XX` | float64 | `0.0` | Fraction of 5xx responses |
| `GET_METHOD` | float64 | `1.0` | Fraction of GET requests |
| `POST_METHOD` | float64 | `0.0` | Fraction of POST requests |
| `HEAD_METHOD` | float64 | `0.0` | Fraction of HEAD requests |
| `OTHER_METHOD` | float64 | `0.0` | Fraction of other HTTP methods |
| `NIGHT` | float64 | `0.0` | Fraction of requests during night hours |
| `UNASSIGNED` | float64 | `1.0` | Fraction of requests with unassigned referrer |
| `IMAGES` | float64 | `0.1012658227848101` | Fraction of image resources |
| `TOTAL_HTML` | float64 | `0.8987341772151899` | Fraction of HTML resources |
| `HTML_TO_IMAGE` | float64 | `0.1126760563380281` | HTML-to-image request ratio |
| `HTML_TO_CSS` | float64 | `0.0` | HTML-to-CSS request ratio |
| `HTML_TO_JS` | float64 | `0.0` | HTML-to-JS request ratio |
| `WIDTH` | float64 | `44.0` | Session navigation graph width |
| `DEPTH` | float64 | `4.0` | Session navigation graph depth |
| `STD_DEPTH` | float64 | `0.4940410898973671` | Std of navigation depth |
| `CONSECUTIVE` | float64 | `0.1012658227848101` | Fraction of consecutive sequential requests |
| `DATA` | float64 | `1555089.0` | Total bytes transferred |
| `PPI` | float64 | `27183337.30379747` | Pages-per-interval (request rate proxy) |
| `SF_REFERRER` | float64 | `0.0` | Same-frame referrer fraction |
| `SF_FILETYPE` | float64 | `0.2051282051282051` | Same-frame filetype fraction |
| `MAX_BARRAGE` | int64 | `1` | Max burst size (consecutive rapid requests) |
| `PENALTY` | int64 | `0` | Heuristic penalty score |
| `ROBOT` | int64 | `1` | Target: 1 = bot, 0 = human |

### `semantic_features` (7 columns)

| column | dtype | example | description |
|---|---|---|---|
| `ID` | object | `obSnwGoBCue8G08E_WCX` | Session id (join key) |
| `TOTAL_TOPICS` | int64 | `242` | Total page topics visited |
| `UNIQUE_TOPICS` | int64 | `500` | Distinct page topics visited |
| `PAGE_SIMILARITY` | float64 | `2.066115702479338` | Mean pairwise page-content similarity |
| `PAGE_VARIANCE` | float64 | `92.25955555555548` | Variance of page-content vectors |
| `BOOLEAN_PAGE_VARIANCE` | float64 | `0.1654136515742342` | Binary indicator of nontrivial page variance |
| `ROBOT` | int64 | `1` | Target: 1 = bot, 0 = human |

### `public_v2.json` (per-entry schema, from first 100 entries)

| field | type | example | description |
|---|---|---|---|
| `referrer` | str | `http://search.lib.auth.gr/Record/68b03dbc211ecdf15867f1d0c91` | HTTP Referer header (URL or `-`) |
| `request` | str | `search.lib.auth.gr:80 66.249.34457 - - [01/Mar/2018:00:00:01` | Full raw access-log request line |
| `method` | str | `GET` | HTTP method (GET/POST/HEAD/...) |
| `resource` | str | `/AJAX/d780f3cf8bf4e286eb6dec2f372f6d7870b6b08cb1e8e85885b70a` | Requested URL path |
| `bytes` | str | `491` | Response size in bytes (string) |
| `response` | str | `200` | HTTP status code (string) |
| `ip` | str | `66.249.34457` | Client IP (obfuscated to last octet jumbled in source) |
| `useragent` | str | `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.c` | Client User-Agent string |
| `timestamp` | str | `2018-02-28T22:00:01.000Z` | ISO-8601 UTC timestamp of request |

Example raw entry (formatted):

```json
"-7RfsmoBCue8G08E1FyY": {'referrer': 'http://search.lib.auth.gr/Record/68b03dbc211ecdf15867f1d0c91519a420f1d8eb301ffd8ac67b262a27acaa1c', 'request': 'search.lib.auth.gr:80 66.249.34457 - - [01/Mar/2018:00:00:01 +0200] GET /AJAX/d780f3cf8bf4e286eb6dec2f372f6d7870b6b08cb1e8e85885b70a3f4db98d9e HTTP/1.1 200 491 http://search.lib.auth.gr/Record/68b03dbc211ecdf15867f1d0c91519a420f1d8eb301ffd8ac67b262a27acaa1c Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 'method': 'GET', 'resource': '/AJAX/d780f3cf8bf4e286eb6dec2f372f6d7870b6b08cb1e8e85885b70a3f4db98d9e', 'bytes': '491', 'response': '200', 'ip
```

## Label
Label column: `ROBOT` in both `simple_features.csv` and `semantic_features.csv` (1 = bot, 0 = human).

| ROBOT | count | rate |
|---|---|---|
| 0 | 53,858 | 0.79965 |
| 1 | 13,494 | 0.20035 |

Label agreement between the two CSVs on shared `ID`: 1.0000 (labels are derived from the same ground-truth session classification).

Class imbalance: roughly 4:1 human:bot. Labels were assigned in the source dataset via heuristic + manual review of session user-agents and behaviour (per the Figshare/paper description); they are session-level rather than request-level.

## Identifier inventory
The CSVs expose only the session `ID` as an identifier; per-session demographic / actor attributes are not present. Actor-level signals (IP, User-Agent) live in the raw `public_v2.json` log at the request level.

| column | source | n_unique (in scope) | role |
|---|---|---|---|
| `ID` | both CSVs | 67,352 | session primary key (Elasticsearch-style id) |
| `ip` | `public_v2.json` (per request) | 9 (in 100-sample) | client IP (obfuscated, weak actor id) |
| `useragent` | `public_v2.json` (per request) | 7 (in 100-sample) | UA string (weak actor/bot signal) |
| `referrer` | `public_v2.json` (per request) | n/a | referring URL |

Example IPs from the JSON sample: `94.66.32960, 79.103.40554, 66.249.34457` (note the source obfuscates the final octet of each IPv4 address by digit-jumbling).
Example User-Agents (truncated): Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36; BUbiNG (+http://law.di.unimi.it/BUbiNG.html); ICC-Crawler/2.0 (Mozilla-compatible; ; http://ucri.nict.go.j.

## Temporal structure
The CSVs contain only aggregated session-level temporal *features* (`TOTAL_DURATION`, `AVERAGE_TIME`, `STANDARD_DEVIATION`, `NIGHT`, `MAX_BARRAGE`); no wall-clock session start/end timestamps are exposed.

Wall-clock timestamps live only in `public_v2.json` at the per-request level.

- Format: ISO-8601 UTC string, e.g. `2018-02-28T22:00:01.000Z` (millisecond precision, `Z` suffix).
- Sample range (100 requests from the head of the file): 2018-02-28 22:00:01+00:00 to 2018-02-28 22:00:25+00:00.
- The raw access-log line inside `request` also contains the original local timestamp with `+0200` offset (Athens local time), confirming the source is European.
- Full file temporal range cannot be reported without scanning the 3 GB JSON, which is out of scope for this bounded EDA.

## Missing data
- `simple_features`: 43,221 null cells overall (2.0054% of cells). 3 of 32 columns have any nulls.
- `semantic_features`: 26,328 null cells overall (5.5843%). 3 of 7 columns have any nulls.
- `public_v2.json`: per-entry schema is dense in the 100-row sample; `referrer` is encoded as the literal string `-` when absent (not JSON null), so a full-file null check would have to look for `-` sentinels rather than missing keys.

Columns with any nulls in `simple_features`:

| column | null_rate |
|---|---|
| `STANDARD_DEVIATION` | 0.213906 |
| `SF_FILETYPE` | 0.213906 |
| `SF_REFERRER` | 0.213906 |

Columns with any nulls in `semantic_features`:

| column | null_rate |
|---|---|
| `BOOLEAN_PAGE_VARIANCE` | 0.130301 |
| `PAGE_VARIANCE` | 0.130301 |
| `PAGE_SIMILARITY` | 0.130301 |

## Quirks and observations
- Three-file layout: two session-feature CSVs (engineered) + one 3 GB raw JSON log. The CSVs are pre-computed features; modelling can use them directly without touching the raw log.
- Both CSVs have identical row counts and a 100% overlap on `ID`; they are effectively two feature blocks for the same session table and can be inner-joined on `ID`.
- The raw JSON is a single top-level object (one outer `{...}`) rather than NDJSON. Streaming parse is feasible because each entry happens to be written on its own line as `"<id>":{...},`, but this layout is fragile - any reformatter would break naive line-parsers.
- Raw-log IDs are per-*request*, not per-*session*; the CSV `ID` is per-session. There is no in-file mapping from session ID to its constituent request IDs.
- Client IPs in the raw log are partially obfuscated (the final octet is digit-shuffled, e.g. `66.249.34457`), so they cannot be geolocated or joined to external IP lists.
- The `referrer` field uses `"-"` for missing values (Apache-log convention) instead of JSON null.
- `PENALTY` in `simple_features` looks like a heuristic bot-score; if it was used to derive `ROBOT` it would leak the label. Verify before using as a feature.
- Class balance ~80/20 human/bot - mild imbalance, manageable without resampling.
- Source host (`search.lib.auth.gr`) is a single library OPAC, so traffic patterns and bot mix are domain-specific (academic search crawlers like Googlebot, ICC-Crawler dominate the bot class).

## Reproduction
Generated by `notebooks/eda/web-robot-sessions.ipynb` which calls `openbotrisk.eda.loaders.load_web_robot_meta` (pandas full-read for the two CSVs; manual line-streaming for the first 100 entries of `public_v2.json`).

Run with:

```bash
jupyter nbconvert --to notebook --execute --inplace \
  notebooks/eda/web-robot-sessions.ipynb \
  --ExecutePreprocessor.timeout=300
```

Loader runtime on this machine: 0.2s. The two CSVs (67,352 rows each) fit in memory; the 3 GB JSON is never fully materialised - only the first 100 entries are read.
