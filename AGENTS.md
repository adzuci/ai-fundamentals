# Agent instructions (AGENTS.md)

Context for AI and tooling working in this repo.

## Project

- **AI Fundamentals** — Course code, notes, and Jupyter notebooks for an intro AI/ML course (Python 3.10, NumPy, Pandas, scikit-learn, Matplotlib).
- Main audience: students and instructors; notebooks should run on macOS, Windows, and in the browser (e.g. Colab).

## Repo layout

- **`class-2-machine-learning-basics/`** — Class 2 materials:
  - Jupyter notebooks: `data-preprocessing.ipynb`, `data-visualization.ipynb` (and any others listed in the folder README).
  - Each notebook: intro (title, topics, slides link), Colab badge, env-check/imports cell, then concept-labeled code cells.
  - `README.md` in this folder: install, run locally, run in Colab, run in PyCharm, Windows quickstart.
- **Root** — `README.md` (course overview, schedule, setup), `requirements.txt`, `scratch.py`, `LICENSE`, `.python-version` (pyenv).
- **`.github/workflows/`** — `notebooks.yml` runs all `class-2-machine-learning-basics/*.ipynb` with `jupyter nbconvert --execute` on Python 3.10 and 3.12.

## Conventions

- **Notebooks**: Use concept comments (e.g. `# Concept: ...`) on code cells; keep intros consistent (title, topics, slides, Colab badge).
- **Python**: Prefer Python 3.10; dependencies in root `requirements.txt` (and optional `class-2-machine-learning-basics/requirements.txt` if present).
- **Safety**: No production secrets; treat production as read-only unless the user explicitly approves changes.

## Useful commands

- Run notebooks like CI: from repo root, `pip install jupyter nbconvert && pip install -r requirements.txt`, then `cd class-2-machine-learning-basics && for f in *.ipynb; do jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=300 --stdout "$f" > /dev/null; done`
- Lint/format: use existing project tooling (e.g. `ruff`, `black`) if configured.
