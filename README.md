# ModelFlow Chile in the browser

The Chile macro-fiscal model in [JupyterLite](https://jupyterlite.readthedocs.io): Python runs
inside the browser (Pyodide), so nothing has to be installed. GitHub Actions builds the site
and publishes it on <https://ibhansen.github.io/chile_lite/>.

| Notebook | Content |
|---|---|
| `chile_scenarios.ipynb` | five scenarios, one exogenous shock each (the front page) |
| `chile_widget_live.ipynb` | the same shocks as sliders in a widget |

The model, the scenarios and the sliders are explained in the book
[ModelFlow models for Chile](https://ibhansen.github.io/chile/).

## Where the files come from

Everything here is published in by `C:\deploy\publish\publish.bat chile_lite`
(manifest `C:\deploy\publish\manifests\chile.yml`); edit the masters, not the copies.

| Path | Master |
|---|---|
| `content\*.ipynb`, `content\chile_widgets.py`, `content\data\chilepens.pcim`, `content\graph\` | `C:\mfmodeller_raw\chile\pensionsmodel 2` |
| `README.md`, `jupyter-lite.json`, `overrides\index.html` | `C:\mfmodeller_raw\chile\lite` |
| scripts, `requirements.txt`, build settings, `.gitignore`, the workflow | `C:\deploy\sitecontrol\lite\shared` |

`content\data\chilepens.pcim` and `content\chile_widgets.py` are also what the live book
`chile_live` downloads (from this repo on GitHub), so this repo has to be public.

## Local test (Windows, Miniforge)

`build.cmd` builds the site into `dist\`, `serve.cmd` serves it on <http://127.0.0.1:8000/>.
The conda env `jlite` they use is made once by `setup_env.cmd`.
