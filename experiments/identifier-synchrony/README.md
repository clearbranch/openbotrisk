# Identifier Graph And Behavioural Synchrony Experiment

Synthetic experiment supporting the Methodology page:

- `site/methodology/identifier-graph-and-synchrony.qmd`

Run the scripts from the repository root in this order:

```bash
python experiments/identifier-synchrony/generate_data.py
python experiments/identifier-synchrony/method1_identifier_graph.py
python experiments/identifier-synchrony/method2_synchrony.py
python experiments/identifier-synchrony/method2_bucket_sweep.py
```

Generated CSVs are written to `experiments/identifier-synchrony/generated/`.
Figures are written to `site/methodology/images/` so the website page updates
when the experiment is rerun.
