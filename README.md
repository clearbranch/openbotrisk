# openbotrisk

A long-horizon, open, written investigation of the bot and abuse prevention category of online security — the commercial and technical territory concerned with detecting and mitigating automated adversarial activity against legitimate web-facing systems. The output is a public knowledge base: a Quarto website with supporting code, datasets where licensing permits, and reproducible analysis. The goal is to make a deliberately opaque category more legible to people trying to understand it.

- **Full scope:** [PROJECT.md](PROJECT.md)
- **Repo structure and todos:** [REPO.md](REPO.md)
- **Rendered site:** [clearbranch.github.io/openbotrisk/](https://clearbranch.github.io/openbotrisk/)

## What this project is not

- Not a vendor comparison or evaluation
- Not a product, even an open-source one
- Not a policy or advocacy project
- Not a buying guide or benchmark
- Not a quick-fix resource — readers looking for "what should I deploy this quarter" are not the audience

See [PROJECT.md §6](PROJECT.md#6-what-the-project-is-not) for the full list.

## How to navigate

| Path | What's there |
|---|---|
| `site/orientation/` | What the project is, scope, how to read |
| `site/background/` | Threat model, actors, economics, vendor landscape |
| `site/techniques/` | Technique families: detection, fingerprinting, behavioural, graph |
| `site/methodology/` | Concrete methodology investigations on public datasets |
| `site/boundaries/` | What can and cannot be replicated from public data |
| `site/reading/` | Literature register and primary sources |
| `site/open-questions/` | Gaps, disagreements, unresolved issues |
| `src/openbotrisk/` | Python package supporting the investigations |
| `notebooks/` | Exploratory work, not yet site-ready |
| `working/` | Internal documents committed but not on site |
| `data/` | Local data references — see `data/README.md` |

## Licence

- Code (`src/`, `notebooks/`, `tests/`): [MIT](LICENSE)
- Written content (`site/`, project documents): [CC BY 4.0](LICENSE)
