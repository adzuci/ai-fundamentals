# ML Fundamentals Notebooks

This folder indexes the supervised-learning practice notebooks in `notebooks/`.

## Notebook Index

1. `notebooks/01_multi_linear_regression.ipynb`
2. `notebooks/02_knn_classifier.ipynb`
3. `notebooks/03_decision_tree_classifier.ipynb`
4. `notebooks/04_random_forest_classifier.ipynb`

## How to run

### Local

```bash
pip install -r requirements.txt
jupyter notebook
```

### Execute like CI

```bash
for f in notebooks/*.ipynb; do
  jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=300 --stdout "$f" > /dev/null
done
```

## Learning flow used in every notebook

1. Objective
2. Install libraries
3. Imports
4. Load / Create dataset
5. Separate features and target
6. Train-test split
7. Create model
8. Train model
9. Make predictions
10. Evaluate model
11. Predict new data
12. Visualization

## Further reading

- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
