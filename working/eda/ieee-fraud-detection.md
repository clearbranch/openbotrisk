# EDA: IEEE-CIS Fraud Detection

## Access
Source: Kaggle competition `ieee-fraud-detection` (via `kaggle competitions download`).

Local path: `/home/tsispace/Documents/GitHub/openbotrisk/data/ieee-fraud-detection`

File format: CSV.

Date inspected: 2026-05-23.

Files on disk:
- `sample_submission.csv` — 5.8 MB
- `test_identity.csv` — 24.6 MB
- `test_transaction.csv` — 584.8 MB
- `train_identity.csv` — 25.3 MB
- `train_transaction.csv` — 651.7 MB

## Structure
- `train_transaction.csv`: 590,540 rows x 394 cols. One row = one transaction.
- `train_identity.csv`: 144,233 rows x 41 cols. Identity / device features attached to a subset of transactions.
- Join key: `TransactionID` (left join transaction <- identity). Identity available for 144,233 / 590,540 transactions (24.4%).
- Temporal coverage: `TransactionDT` ranges from 86,400 to 15,811,131 seconds (~182.0 days) from an unspecified reference time.

## Schema
### `train_transaction (showing non-V columns + V1..V20 of 339 V cols)` (75 columns)

| column | dtype | example | description |
|---|---|---|---|
| `TransactionID` | int64 | `2987000` | Unique transaction id |
| `isFraud` | int64 | `0` | Target: 1 = fraudulent, 0 = legitimate |
| `TransactionDT` | int64 | `86400` | Time-delta from reference, in seconds |
| `TransactionAmt` | float64 | `68.5` | Transaction amount (USD) |
| `ProductCD` | object | `W` | Product code (categorical) |
| `card1` | int64 | `13926` | payment card attribute (anonymised) |
| `card2` | float64 | `` | payment card attribute (anonymised) |
| `card3` | float64 | `150.0` | payment card attribute (anonymised) |
| `card4` | object | `discover` | payment card attribute (anonymised) |
| `card5` | float64 | `142.0` | payment card attribute (anonymised) |
| `card6` | object | `credit` | payment card attribute (anonymised) |
| `addr1` | float64 | `315.0` | address attribute (anonymised) |
| `addr2` | float64 | `87.0` | address attribute (anonymised) |
| `dist1` | float64 | `19.0` | distance feature (anonymised) |
| `dist2` | float64 | `` | distance feature (anonymised) |
| `P_emaildomain` | object | `` | Purchaser email domain |
| `R_emaildomain` | object | `` | Recipient email domain |
| `C1` | float64 | `1.0` | count-type feature (anonymised) |
| `C2` | float64 | `1.0` | count-type feature (anonymised) |
| `C3` | float64 | `0.0` | count-type feature (anonymised) |
| `C4` | float64 | `0.0` | count-type feature (anonymised) |
| `C5` | float64 | `0.0` | count-type feature (anonymised) |
| `C6` | float64 | `1.0` | count-type feature (anonymised) |
| `C7` | float64 | `0.0` | count-type feature (anonymised) |
| `C8` | float64 | `0.0` | count-type feature (anonymised) |
| `C9` | float64 | `1.0` | count-type feature (anonymised) |
| `C10` | float64 | `0.0` | count-type feature (anonymised) |
| `C11` | float64 | `2.0` | count-type feature (anonymised) |
| `C12` | float64 | `0.0` | count-type feature (anonymised) |
| `C13` | float64 | `1.0` | count-type feature (anonymised) |
| `C14` | float64 | `1.0` | count-type feature (anonymised) |
| `D1` | float64 | `14.0` | time-delta-type feature in days (anonymised) |
| `D2` | float64 | `` | time-delta-type feature in days (anonymised) |
| `D3` | float64 | `13.0` | time-delta-type feature in days (anonymised) |
| `D4` | float64 | `` | time-delta-type feature in days (anonymised) |
| `D5` | float64 | `` | time-delta-type feature in days (anonymised) |
| `D6` | float64 | `` | time-delta-type feature in days (anonymised) |
| `D7` | float64 | `` | time-delta-type feature in days (anonymised) |
| `D8` | float64 | `` | time-delta-type feature in days (anonymised) |
| `D9` | float64 | `` | time-delta-type feature in days (anonymised) |
| `D10` | float64 | `13.0` | time-delta-type feature in days (anonymised) |
| `D11` | float64 | `13.0` | time-delta-type feature in days (anonymised) |
| `D12` | float64 | `` | time-delta-type feature in days (anonymised) |
| `D13` | float64 | `` | time-delta-type feature in days (anonymised) |
| `D14` | float64 | `` | time-delta-type feature in days (anonymised) |
| `D15` | float64 | `0.0` | time-delta-type feature in days (anonymised) |
| `M1` | object | `T` | match-type categorical (T/F) (anonymised) |
| `M2` | object | `T` | match-type categorical (T/F) (anonymised) |
| `M3` | object | `T` | match-type categorical (T/F) (anonymised) |
| `M4` | object | `M2` | match-type categorical (T/F) (anonymised) |
| `M5` | object | `F` | match-type categorical (T/F) (anonymised) |
| `M6` | object | `T` | match-type categorical (T/F) (anonymised) |
| `M7` | object | `` | match-type categorical (T/F) (anonymised) |
| `M8` | object | `` | match-type categorical (T/F) (anonymised) |
| `M9` | object | `` | match-type categorical (T/F) (anonymised) |
| `V1` | float64 | `1.0` | Vesta-engineered numeric feature (anonymised) |
| `V2` | float64 | `1.0` | Vesta-engineered numeric feature (anonymised) |
| `V3` | float64 | `1.0` | Vesta-engineered numeric feature (anonymised) |
| `V4` | float64 | `1.0` | Vesta-engineered numeric feature (anonymised) |
| `V5` | float64 | `1.0` | Vesta-engineered numeric feature (anonymised) |
| `V6` | float64 | `1.0` | Vesta-engineered numeric feature (anonymised) |
| `V7` | float64 | `1.0` | Vesta-engineered numeric feature (anonymised) |
| `V8` | float64 | `1.0` | Vesta-engineered numeric feature (anonymised) |
| `V9` | float64 | `1.0` | Vesta-engineered numeric feature (anonymised) |
| `V10` | float64 | `0.0` | Vesta-engineered numeric feature (anonymised) |
| `V11` | float64 | `0.0` | Vesta-engineered numeric feature (anonymised) |
| `V12` | float64 | `1.0` | Vesta-engineered numeric feature (anonymised) |
| `V13` | float64 | `1.0` | Vesta-engineered numeric feature (anonymised) |
| `V14` | float64 | `1.0` | Vesta-engineered numeric feature (anonymised) |
| `V15` | float64 | `0.0` | Vesta-engineered numeric feature (anonymised) |
| `V16` | float64 | `0.0` | Vesta-engineered numeric feature (anonymised) |
| `V17` | float64 | `0.0` | Vesta-engineered numeric feature (anonymised) |
| `V18` | float64 | `0.0` | Vesta-engineered numeric feature (anonymised) |
| `V19` | float64 | `1.0` | Vesta-engineered numeric feature (anonymised) |
| `V20` | float64 | `1.0` | Vesta-engineered numeric feature (anonymised) |

Full V-column range: V1..V339 (339 columns).

### `train_identity` (41 columns)

| column | dtype | example | description |
|---|---|---|---|
| `TransactionID` | int64 | `2987004` | Join key to train_transaction |
| `id_01` | float64 | `0.0` | identity feature (anonymised) |
| `id_02` | float64 | `70787.0` | identity feature (anonymised) |
| `id_03` | float64 | `` | identity feature (anonymised) |
| `id_04` | float64 | `` | identity feature (anonymised) |
| `id_05` | float64 | `` | identity feature (anonymised) |
| `id_06` | float64 | `` | identity feature (anonymised) |
| `id_07` | float64 | `` | identity feature (anonymised) |
| `id_08` | float64 | `` | identity feature (anonymised) |
| `id_09` | float64 | `` | identity feature (anonymised) |
| `id_10` | float64 | `` | identity feature (anonymised) |
| `id_11` | float64 | `100.0` | identity feature (anonymised) |
| `id_12` | object | `NotFound` | identity feature (anonymised) |
| `id_13` | float64 | `` | identity feature (anonymised) |
| `id_14` | float64 | `-480.0` | identity feature (anonymised) |
| `id_15` | object | `New` | identity feature (anonymised) |
| `id_16` | object | `NotFound` | identity feature (anonymised) |
| `id_17` | float64 | `166.0` | identity feature (anonymised) |
| `id_18` | float64 | `` | identity feature (anonymised) |
| `id_19` | float64 | `542.0` | identity feature (anonymised) |
| `id_20` | float64 | `144.0` | identity feature (anonymised) |
| `id_21` | float64 | `` | identity feature (anonymised) |
| `id_22` | float64 | `` | identity feature (anonymised) |
| `id_23` | object | `` | identity feature (anonymised) |
| `id_24` | float64 | `` | identity feature (anonymised) |
| `id_25` | float64 | `` | identity feature (anonymised) |
| `id_26` | float64 | `` | identity feature (anonymised) |
| `id_27` | object | `` | identity feature (anonymised) |
| `id_28` | object | `New` | identity feature (anonymised) |
| `id_29` | object | `NotFound` | identity feature (anonymised) |
| `id_30` | object | `Android 7.0` | identity feature (anonymised) |
| `id_31` | object | `samsung browser 6.2` | identity feature (anonymised) |
| `id_32` | float64 | `32.0` | identity feature (anonymised) |
| `id_33` | object | `2220x1080` | identity feature (anonymised) |
| `id_34` | object | `match_status:2` | identity feature (anonymised) |
| `id_35` | object | `T` | identity feature (anonymised) |
| `id_36` | object | `F` | identity feature (anonymised) |
| `id_37` | object | `T` | identity feature (anonymised) |
| `id_38` | object | `T` | identity feature (anonymised) |
| `DeviceType` | object | `mobile` | Device class (desktop / mobile) |
| `DeviceInfo` | object | `SAMSUNG SM-G892A Build/NRD90M` | Device info string (browser/UA-derived) |

Most columns (V*, C*, D*, M*, id_*, card*, addr*, dist*) are anonymised by Vesta with no public mapping.

## Label
Label column: `isFraud` in `train_transaction.csv` (1 = fraudulent).

| isFraud | count | rate |
|---|---|---|
| 0 | 569,877 | 0.96501 |
| 1 | 20,663 | 0.03499 |

Per Kaggle: a fraud label is propagated to all transactions in a card/account/email/etc. chain after the first reported fraud; so the label is partly a chain-propagated proxy rather than a per-transaction confirmation.

## Identifier inventory
No explicit user ID. Weak actor identifiers come from card hashes, email domains, and (when joined) device/browser strings.

| column | n_unique | null_rate | role |
|---|---|---|---|
| `TransactionID` | 590,540 | 0.0000 | transaction primary key |
| `card1` | 13,553 | 0.0000 | card hash (weak account identifier) |
| `card2` | 500 | 0.0151 | card attribute |
| `card3` | 114 | 0.0027 | card attribute |
| `card4` | 4 | 0.0027 | card network (visa/mc/etc.) |
| `card5` | 119 | 0.0072 | card attribute |
| `card6` | 4 | 0.0027 | card type (debit/credit) |
| `addr1` | 332 | 0.1113 | billing address region |
| `addr2` | 74 | 0.1113 | billing country |
| `P_emaildomain` | 59 | 0.1599 | purchaser email domain (weak actor signal) |
| `R_emaildomain` | 60 | 0.7675 | recipient email domain |
| `DeviceType` | 2 | 0.0237 | device class |
| `DeviceInfo` | 1,786 | 0.1773 | device fingerprint string |
| `id_30` | 75 | 0.4622 | OS string |
| `id_31` | 130 | 0.0274 | browser string |
| `id_33` | 260 | 0.4919 | screen resolution |

## Temporal structure
- `TransactionDT`: integer seconds from a reference time (reference not disclosed).
- Range: 86,400 to 15,811,131 seconds (182.0 days of activity).
- Granularity: 1 second. No wall-clock timestamps; no timezone.
- D1..D15 are documented as time-delta features in days relative to prior events on the same card / account.
- Diurnal patterns are inferable modulo the unknown reference time; not plotted here.

## Missing data
- `train_transaction`: 95,566,686 null cells overall (41.07% of cells). 212 of 394 columns have >20% missingness.
- `train_identity`: 2,104,107 null cells overall (35.58%). 19 of 41 columns have >20% missingness.
- Identity rows themselves are missing for ~76% of transactions (no identity file row for that TransactionID).

Top 15 most-null columns in `train_transaction`:

| column | null_rate |
|---|---|
| `dist2` | 0.9363 |
| `D7` | 0.9341 |
| `D13` | 0.8951 |
| `D14` | 0.8947 |
| `D12` | 0.8904 |
| `D6` | 0.8761 |
| `D9` | 0.8731 |
| `D8` | 0.8731 |
| `V153` | 0.8612 |
| `V149` | 0.8612 |
| `V141` | 0.8612 |
| `V146` | 0.8612 |
| `V154` | 0.8612 |
| `V162` | 0.8612 |
| `V142` | 0.8612 |

Top 15 most-null columns in `train_identity`:

| column | null_rate |
|---|---|
| `id_24` | 0.9671 |
| `id_25` | 0.9644 |
| `id_07` | 0.9643 |
| `id_08` | 0.9643 |
| `id_21` | 0.9642 |
| `id_26` | 0.9642 |
| `id_23` | 0.9642 |
| `id_27` | 0.9642 |
| `id_22` | 0.9642 |
| `id_18` | 0.6872 |
| `id_04` | 0.5402 |
| `id_03` | 0.5402 |
| `id_33` | 0.4919 |
| `id_10` | 0.4805 |
| `id_09` | 0.4805 |

## Quirks and observations
- Two-file structure (transaction + identity) joined on `TransactionID`; only 24% of transactions have identity rows.
- V*/C*/D*/M*/id_* columns are anonymised; no public mapping. Treat them as opaque features.
- `TransactionDT` is seconds from an unstated reference time; cannot anchor to calendar dates.
- Labels are chain-propagated (per Kaggle): once a card/account is flagged, related transactions inherit the positive label, which inflates positives and complicates per-row interpretation.
- High missingness is concentrated in long blocks of V/D/id_ columns — typical of features only defined for certain product codes or device classes.

## Reproduction
Generated by `notebooks/eda/ieee-fraud-detection.ipynb` which calls `openbotrisk.eda.loaders.load_ieee_meta` (pandas full-read).

Run with:

```bash
jupyter nbconvert --to notebook --execute --inplace \
  notebooks/eda/ieee-fraud-detection.ipynb \
  --ExecutePreprocessor.timeout=600
```

Loader runtime on this machine: 14.0s. Both train CSVs fit in memory; no chunking needed.
