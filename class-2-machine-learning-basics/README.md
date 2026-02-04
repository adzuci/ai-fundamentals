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

- **data-preprocessing.ipynb** — DataFrame basics, missing values, categorical encoding, feature scaling
- **data-visualization.ipynb** — Plotting (scatter, histogram, pandas) plus preprocessing and scaling (imputation, encoding, StandardScaler, train/test split)

Each notebook has an **Open in Colab** button in its intro. Use that to run in the browser with no local setup.

## Run in PyCharm

1. **Open the project**: File → Open → select the `ai-fundamentals` folder (repo root). Use "Trust Project" if prompted.
2. **Set Python interpreter**: File → Settings → Project → Python Interpreter. Add or select an interpreter that has `jupyter`, `numpy`, `pandas`, `scikit-learn`, and `matplotlib` (e.g. create a venv and run: `pip install jupyter numpy pandas scikit-learn matplotlib`).
3. **Open a notebook**: In the Project tool window, go to `class-2-machine-learning-basics/` and double-click `data-preprocessing.ipynb` or `data-visualization.ipynb`.
4. **Choose kernel**: If PyCharm asks for a kernel, pick the interpreter you configured. You can change it later via the kernel selector in the notebook toolbar.
5. **Run cells**: Use the run (play) button next to a cell, or **Shift+Enter** to run the current cell and move to the next. Use **Run All** in the toolbar to run the whole notebook.

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
10. Open a notebook from `class-2-machine-learning-basics/` (e.g. `data-preprocessing.ipynb` or `data-visualization.ipynb`) in the browser tab.

## Editor Recommendations

- **Geany**: Great for simple Python scripts and beginners (Windows-friendly).
- **PyCharm**: Full Jupyter support; open `.ipynb` files and run cells with a configured interpreter (see Run in PyCharm above).
- **Cursor**: Great for notebooks, code navigation, and AI-assisted help (macOS-friendly).

## Notes

- On Windows, ensure `python` is in PATH.
- If `pip` points to a different Python, use `python -m pip install jupyter`.
