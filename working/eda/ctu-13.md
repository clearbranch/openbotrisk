# EDA: CTU-13

## Access
Source: CTU-13 dataset, Czech Technical University (Stratosphere Lab) — `https://mcfp.felk.cvut.cz/publicDatasets/CTU-13-Dataset/`.

Local path: `data/CTU-13-Dataset`

File format: per-scenario `.binetflow` CSV (Argus bidirectional NetFlow export).

Date inspected: 2026-05-23.

Files on disk (13 scenarios):
- `1/capture20110810.binetflow` — 368.7 MB
- `2/capture20110811.binetflow` — 235.8 MB
- `3/capture20110812.binetflow` — 610.0 MB
- `4/capture20110815.binetflow` — 146.7 MB
- `5/capture20110815-2.binetflow` — 16.9 MB
- `6/capture20110816.binetflow` — 73.2 MB
- `7/capture20110816-2.binetflow` — 14.9 MB
- `8/capture20110816-3.binetflow` — 385.2 MB
- `9/capture20110817.binetflow` — 272.6 MB
- `10/capture20110818.binetflow` — 170.8 MB
- `11/capture20110818-2.binetflow` — 13.9 MB
- `12/capture20110819.binetflow` — 42.6 MB
- `13/capture20110815-3.binetflow` — 250.5 MB

## Structure
- 13 scenarios; each a separate Argus bidirectional netflow capture (`.binetflow` CSV).
- Record granularity: one bidirectional flow per row.
- Total rows (all scenarios concatenated): 19,976,700; columns: 16 (14 native + `scenario` tag added by loader).
- Time range across all scenarios (`StartTime` as string): 2011/08/10 09:46:53.047277 to 2011/08/19 11:45:43.647861.
- No join keys between scenarios; each capture is independent. Within a scenario, flows can be linked by `SrcAddr` / `DstAddr` / port tuples.

Per-scenario row counts:

| scenario | file | rows | size |
|---|---|---|---|
| 1 | `capture20110810.binetflow` | 2,824,636 | 368.7 MB |
| 2 | `capture20110811.binetflow` | 1,808,122 | 235.8 MB |
| 3 | `capture20110812.binetflow` | 4,710,638 | 610.0 MB |
| 4 | `capture20110815.binetflow` | 1,121,076 | 146.7 MB |
| 5 | `capture20110815-2.binetflow` | 129,832 | 16.9 MB |
| 6 | `capture20110816.binetflow` | 558,919 | 73.2 MB |
| 7 | `capture20110816-2.binetflow` | 114,077 | 14.9 MB |
| 8 | `capture20110816-3.binetflow` | 2,954,230 | 385.2 MB |
| 9 | `capture20110817.binetflow` | 2,087,508 | 272.6 MB |
| 10 | `capture20110818.binetflow` | 1,309,791 | 170.8 MB |
| 11 | `capture20110818-2.binetflow` | 107,251 | 13.9 MB |
| 12 | `capture20110819.binetflow` | 325,471 | 42.6 MB |
| 13 | `capture20110815-3.binetflow` | 1,925,149 | 250.5 MB |

## Schema
| column | dtype | example | description |
|---|---|---|---|
| `StartTime` | String | `2011/08/10 09:46:59.607825` | Flow start timestamp (string, microsecond precision) |
| `Dur` | Float64 | `1.026539` | Flow duration in seconds |
| `Proto` | String | `tcp` | L4 protocol (tcp, udp, icmp, ...) |
| `SrcAddr` | String | `94.44.127.113` | Source IP address |
| `Sport` | String | `1577` | Source port |
| `Dir` | String | `   ->` | Flow direction marker |
| `DstAddr` | String | `147.32.84.59` | Destination IP address |
| `Dport` | String | `6881` | Destination port |
| `State` | String | `S_RA` | Argus flow state (connection state code) |
| `sTos` | Int64 | `0` | Source ToS byte |
| `dTos` | Int64 | `0` | Destination ToS byte |
| `TotPkts` | Int64 | `4` | Total packets in flow |
| `TotBytes` | Int64 | `276` | Total bytes in flow |
| `SrcBytes` | Int64 | `156` | Bytes sent by source |
| `Label` | String | `flow=Background-Established-cm` | Argus label string; `flow=Background-...`, `flow=From-Botnet-...`, `flow=To-Botnet-...`, `flow=LEGITIMATE`, etc. |
| `scenario` | String | `1` | Scenario folder id (1..13) — added by loader, not native. |

All columns are real (non-anonymised) network metadata; IPs are real but from a controlled lab capture.

## Label
Label column: `Label` (free-text Argus annotation). Coarsened to three classes by string match: `Botnet` (contains "Botnet"), `Legitimate`, `Background`, else `Other`.

| label_class | count | rate |
|---|---|---|
| Background | 19,175,568 | 0.95990 |
| Botnet | 444,699 | 0.02226 |
| Other | 356,433 | 0.01784 |

Distinct raw label strings across all scenarios: 1400. Botnet traffic is heavily outnumbered by background. Background flows are unlabelled real traffic and should not be treated as confirmed-legitimate.

## Identifier inventory
Identifiers are real IP addresses and ports (no user IDs, no device fingerprints).

| column | n_unique | null_rate | role |
|---|---|---|---|
| `SrcAddr` | 2,031,491 | 0.0000 | source IP — strongest actor identifier (per-host) |
| `DstAddr` | 531,964 | 0.0000 | destination IP — actor identifier for the contacted endpoint |
| `Sport` | 118,218 | 0.0102 | source port (often ephemeral) |
| `Dport` | 108,451 | 0.0097 | destination port (service identifier) |
| `Proto` | 19 | 0.0000 | L4 protocol |

Within a scenario, the infected hosts have known IPs (documented in each scenario `README`). There is no user-level identifier; the actor unit is the host (IP) inside the captured network.

## Temporal structure
- `StartTime`: string timestamp with microsecond precision (`YYYY/MM/DD HH:MM:SS.ffffff`).
- `Dur`: float seconds duration of the flow.
- Granularity: microsecond start; flow durations span sub-second to hours.
- Each scenario is a contiguous capture window of hours; scenarios are not contemporaneous.

Per-scenario time spans:

| scenario | t_min | t_max | rows |
|---|---|---|---|
| 1 | 2011/08/10 09:46:53.047277 | 2011/08/10 15:54:07.368340 | 2,824,636 |
| 10 | 2011/08/18 09:56:29.146156 | 2011/08/18 15:04:59.744388 | 1,309,791 |
| 11 | 2011/08/18 15:39:35.087798 | 2011/08/18 15:55:46.379941 | 107,251 |
| 12 | 2011/08/19 10:02:43.748728 | 2011/08/19 11:45:43.647861 | 325,471 |
| 13 | 2011/08/15 17:13:40.449530 | 2011/08/16 09:36:00.806547 | 1,925,149 |
| 2 | 2011/08/11 09:49:35.721274 | 2011/08/11 14:01:11.264754 | 1,808,122 |
| 3 | 2011/08/12 15:24:01.105063 | 2011/08/15 10:13:26.439802 | 4,710,638 |
| 4 | 2011/08/15 10:42:52.613616 | 2011/08/15 15:11:19.149682 | 1,121,076 |
| 5 | 2011/08/15 16:43:20.931208 | 2011/08/15 17:13:26.758894 | 129,832 |
| 6 | 2011/08/16 10:01:46.972101 | 2011/08/16 12:10:56.805092 | 558,919 |
| 7 | 2011/08/16 13:51:24.049047 | 2011/08/16 14:12:41.499668 | 114,077 |
| 8 | 2011/08/16 14:18:55.889839 | 2011/08/17 09:47:11.231725 | 2,954,230 |
| 9 | 2011/08/17 11:34:49.436881 | 2011/08/17 17:12:13.867435 | 2,087,508 |

## Missing data
Overall null cells: 2,337,061 / 319,627,200 (0.73%).

Columns with >20% missingness: _none_.

Per-column nulls (all scenarios concatenated):

| column | null_count | null_rate |
|---|---|---|
| `dTos` | 1,718,011 | 0.08600 |
| `sTos` | 220,525 | 0.01104 |
| `Sport` | 203,085 | 0.01017 |
| `Dport` | 194,062 | 0.00971 |
| `State` | 1,378 | 0.00007 |
| `StartTime` | 0 | 0.00000 |
| `Dur` | 0 | 0.00000 |
| `Proto` | 0 | 0.00000 |
| `SrcAddr` | 0 | 0.00000 |
| `Dir` | 0 | 0.00000 |
| `DstAddr` | 0 | 0.00000 |
| `TotPkts` | 0 | 0.00000 |
| `TotBytes` | 0 | 0.00000 |
| `SrcBytes` | 0 | 0.00000 |
| `Label` | 0 | 0.00000 |
| `scenario` | 0 | 0.00000 |

`sTos` / `dTos` are commonly null because routers do not always set ToS. Port nulls occur for connectionless / ICMP / ARP flows.

## Quirks and observations
- 13 separate captures; each scenario uses a different botnet family (per scenario `README`). They are not a single time series.
- `Label` is a free-text Argus annotation, not a clean class column; coarsening requires substring matching.
- `Background` flows are unlabelled real traffic from the same network — they are NOT verified-legitimate.
- `Sport` / `Dport` are stored as strings (some non-numeric values like `0x*` exist), not integers.
- IPs are real and from a single university network capture; the actor unit is a host, not a user.
- Concatenating all scenarios into one frame is fine for descriptive stats but mixes captures from different dates and botnet families.

## Reproduction
Generated by `notebooks/eda/ctu-13.ipynb` which calls `openbotrisk.eda.loaders.load_ctu13_meta` (polars read of each `*.binetflow`, then vertical concat).

Run with:

```bash
jupyter nbconvert --to notebook --execute --inplace \
  notebooks/eda/ctu-13.ipynb \
  --ExecutePreprocessor.timeout=600
```

Loader runtime on this machine: 1.4s for all 13 scenarios concatenated in-memory with polars.
