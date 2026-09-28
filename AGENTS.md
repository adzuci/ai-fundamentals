# Agent instructions (AGENTS.md)

Context for AI and tooling working in this repo.

## Project

- **AI Fundamentals** — Course code, notes, and Jupyter notebooks for an intro AI/ML course (Python 3.10, NumPy, Pandas, scikit-learn, Matplotlib).
- Main audience: students and instructors; notebooks should run on macOS, Windows, and in the browser (e.g. Colab).

## Repo layout

- **`ai-fundamentals-class/`** — Unique System Skills AI Fundamentals materials:
  - `class-2-machine-learning-basics/` through `class-8-bias-and-ethics/` (notebooks, slides, class READMEs).
  - Class 2 notebooks: `data-preprocessing.ipynb`, `scaling-data.ipynb`. Each notebook: intro (title, topics, slides link), Colab badge, env-check/imports cell, then concept-labeled code cells.
  - `docs/ml-fundamentals/` — supervised-learning notes.
  - `scratch.py`, `AI-900_PREP_PLAN.md`.
- **`building-with-the-claude-api/`** — Course code for [Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api). `claude_chat.py` loads `ANTHROPIC_API_KEY` from the repo-root `.env` via python-dotenv. Use the repo-root `.venv-claude` (`source .venv-claude/bin/activate`).
- **Root** — `README.md` (overview, schedule, setup), `requirements.txt`, `LICENSE`, `.python-version` (pyenv), `AGENTS.md`.
- **`.github/workflows/`** — `notebooks.yml` runs all `ai-fundamentals-class/class-2-machine-learning-basics/*.ipynb` with `jupyter nbconvert --execute` on Python 3.10 and 3.12.

## Conventions

- **Notebooks**: Use concept comments (e.g. `# Concept: ...`) on code cells; keep intros consistent (title, topics, slides, Colab badge).
- **Python**: Prefer Python 3.10; dependencies in root `requirements.txt`.
- **Safety**: No production secrets; treat production as read-only unless the user explicitly approves changes.

## Useful commands

- Run notebooks like CI: from repo root, `pip install jupyter nbconvert && pip install -r requirements.txt`, then `cd ai-fundamentals-class/class-2-machine-learning-basics && for f in *.ipynb; do jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=300 --stdout "$f" > /dev/null; done`
- Lint/format: use existing project tooling (e.g. `ruff`, `black`) if configured.
