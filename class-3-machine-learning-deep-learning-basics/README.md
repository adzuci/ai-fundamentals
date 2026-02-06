# Class 3 – Machine Learning Basics & Deep Learning Basics

This class builds directly on **Class 2 – Machine Learning Basics**. In Class 2 you prepared data for modeling (DataFrames, missing values, categorical encoding, scaling, and train/test splits). Class 3 assumes you are comfortable with those ideas and focuses on **training and evaluating models**, including a first look at **deep learning**.

## How this extends Class 2

- Reuses the same ideas and patterns from `class-2-machine-learning-basics/` (especially `data-preprocessing.ipynb` and `scaling-data.ipynb`).
- Moves from “ready-for-ML features” to “train and evaluate simple models”.
- Introduces common supervised learning workflows end‑to‑end using the same **common step structure** (from the Class 3 supervised‑learning slides):
  1. Define the objective  
  2. Install/import libraries  
  3. Load or create a dataset  
  4. Separate features and target  
  5. Train/test split  
  6. Create and train the model  
  7. Make predictions  
  8. Evaluate model  
  9. Predict new data  
  10. (Optional) Visualize and iterate  
- Adds a gentle introduction to **deep learning basics** (e.g., simple feed‑forward networks) on top of the same pipeline.

## What’s in this folder now

- `01_class_3_linear_regression_basics.ipynb`
  - A **complete Linear Regression walkthrough** (house size → house price) that mirrors the *Linear_Regression_demo1.pdf* slides:
    - Objective, imports, sample dataset, feature/target split, train/test split  
    - Train `LinearRegression`, inspect slope/intercept, make predictions, evaluate with MSE & R²  
    - Visualize the fitted line over the data and highlight key learnings  
  - A **multiple linear regression exercise** (Area, Bedrooms, Age → Price):
    - Students create a tiny DataFrame with 3 features and a price column  
    - Follow the same step structure to split, train, evaluate, and predict a new house  
    - Includes a suggested “Actual vs Predicted” scatter plot for the test set  
  - Start here before trying any of the classifier notebooks.
- `02_class_3_logistic_regression_basics.ipynb`
  - A **Logistic Regression (classification) walkthrough** that mirrors the *Logistic_Regression_demo1.pdf* slides:
    - Objective: classify Pass / Fail from study hours.  
    - Uses the same 10‑step pattern as the Linear Regression notebook.  
    - Includes accuracy, confusion matrix, and a simple prediction for a new student.
- `multi_reg1.ipynb` — scratch/experimental notebook for multi‑regression variants.
- **Practice notebooks (moved here from `notebooks/`)** — all follow the same 10‑step supervised‑learning pattern plus an explicit “Visualization” step:
  - `03_class_3_multi_linear_regression.ipynb`
    - Multiple features (`Area`, `Bedroom`, `Age`) → `Price` using `LinearRegression`.  
    - Mirrors the **multi‑feature house‑price** example and reinforces the Class 3 multiple‑regression exercise.
  - `04_class_3_knn_classifier.ipynb`
    - K‑Nearest Neighbors classifier (`KNeighborsClassifier`) using `Age` + `Salary` → `Buy`.  
    - Focuses on intuition for KNN, distance in feature space, and how `n_neighbors` affects decision boundaries.
  - `05_class_3_decision_tree_classifier.ipynb`
    - Decision Tree classifier (`DecisionTreeClassifier`) on the same `Age`/`Salary` → `Buy` setup.  
    - Highlights interpretability (tree structure) and overfitting risks.
  - `06_class_3_random_forest_classifier.ipynb`
    - Random Forest classifier (`RandomForestClassifier`) ensemble over many trees on `Age`/`Salary` → `Buy`.  
    - Introduces feature importance and compares against the single‑tree notebook.
- Slide PDFs that go with these notebooks:
  - `Linear_Regression_demo1.pdf`  
  - `Logistic_Regression_demo1.pdf`  
  - `Decision_Tree_demo.pdf`  
  - `Random_Forest_demo.pdf`  
  - `KNN.pdf`  
  - `Supervised Learning Algorithms.pdf` (overview + common step structure)

- The notebooks are intentionally written to be **approachable for new Python users** (small datasets, clear comments, fill‑in‑the‑blank TODO cells, “check yourself” prompts) and still interesting for engineers (explicit equations, model coefficients, evaluation metrics, and smoke‑test style sanity checks).

## Supervised learning roadmap (from the slides)

Class 3 and later classes will use the same pattern for a small, practical subset of supervised learning algorithms.

- **Regression algorithms** (predict values)
  - Linear Regression *(implemented here, including a multi‑feature variant in `03_class_3_multi_linear_regression.ipynb`)*  
  - Polynomial Regression, Ridge, Lasso, Elastic Net *(later / advanced material)*  
  - Decision Tree Regressor, Random Forest Regressor  
  - Support Vector Regression (SVR)  
- **Classification algorithms** (predict categories)
  - Logistic Regression  
  - K‑Nearest Neighbors (KNN)  
  - Decision Tree Classifier  
  - Random Forest Classifier  
  - Support Vector Machine (SVM)  
  - Naive Bayes  
  - Gradient Boosting / XGBoost  

Future notebooks in this folder will add these algorithms one by one, always following the same **common step structure** and reusing the preprocessing ideas from Class 2.

