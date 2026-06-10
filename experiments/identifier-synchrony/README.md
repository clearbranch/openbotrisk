# Identifier Graph And Behavioural Synchrony Experiment

Synthetic experiment supporting the Methodology page:

- `site/methodology/identifier-graph-and-synchrony.qmd`

Run the scripts from the repository root in this order:

```bash
python src/openbotrisk/experiments/identifier_synchrony/generate_data.py
python src/openbotrisk/experiments/identifier_synchrony/method1_identifier_graph.py
python src/openbotrisk/experiments/identifier_synchrony/method2_synchrony.py
python src/openbotrisk/experiments/identifier_synchrony/method2_bucket_sweep.py
```

Generated CSVs are written to `experiments/identifier-synchrony/generated/`.
Figures are written to `site/methodology/images/` so the website page updates
when the experiment is rerun.

## Script Roles

The Python source lives in `src/openbotrisk/experiments/identifier_synchrony/`.

| Script | Purpose |
|---|---|
| `generate_data.py` | Creates synthetic users and timestamped events, including benign identifier sharing and coordinated campaign waves. |
| `method1_identifier_graph.py` | Builds the shared-identifier graph, prunes high-degree identifiers, projects to user-user edges, scores clusters, and writes the Method 1 figure. |
| `method2_synchrony.py` | Builds behavioural tokens, computes candidate pair similarities, creates synchrony clusters, compares Method 1 and Method 2 coverage, and writes the Method 2 figure. |
| `method2_bucket_sweep.py` | Reruns the synchrony detector across several time-bucket widths and writes the sensitivity figure. |

The generated CSVs are ignored by Git because they are deterministic rebuild
artifacts. The generated figures are kept under `site/methodology/images/`
because the rendered site depends on them.
