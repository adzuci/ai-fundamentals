# Class 2 - Machine Learning Basics (Jupyter Setup)

This class uses Jupyter Notebook for hands-on exercises.

## Install

```bash
pip install jupyter
```

Optional (recommended for data work):

```bash
pip install numpy pandas
```

## Launch

```bash
python -m notebook
```

## Notebooks

- **scaling-data.ipynb** — ML preprocessing: missing values, encoding, scaling, train/test split
- **data-visualization.ipynb** — Plotting with Matplotlib

## Run in the Browser

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adzuci/ai-fundamentals/blob/main/class-2-machine-learning-basics/scaling-data.ipynb)

## Windows Quickstart (Step-by-Step)

1. Open **Command Prompt** (Start menu -> type "cmd" -> Enter).
2. Check Python is installed:
   ```bash
   python --version
   ```
3. Create a project folder (example):
   ```bash
   mkdir ai-fundamentals
   cd ai-fundamentals
   ```
4. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
5. Activate the virtual environment:
   ```bash
   .venv\Scripts\activate
   ```
6. Upgrade pip (recommended):
   ```bash
   python -m pip install --upgrade pip
   ```
7. Install Jupyter:
   ```bash
   python -m pip install jupyter
   ```
8. (Optional) Install data libraries:
   ```bash
   python -m pip install numpy pandas
   ```
9. Launch Jupyter:
   ```bash
   python -m notebook
   ```
10. Open `class-2-machine-learning-basics/scaling-data.ipynb` from the browser tab.

## Editor Recommendations

- **Geany**: Great for simple Python scripts and beginners (Windows-friendly).
- **Cursor**: Great for notebooks, code navigation, and AI-assisted help (macOS-friendly).

## Notes

- On Windows, ensure `python` is in PATH.
- If `pip` points to a different Python, use `python -m pip install jupyter`.
