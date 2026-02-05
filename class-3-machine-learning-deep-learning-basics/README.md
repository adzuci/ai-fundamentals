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

- `class-3-linear-regression-basics.ipynb`
  - A **complete Linear Regression walkthrough** (house size → house price) that mirrors the *Linear_Regression_demo1.pdf* slides:
    - Objective, imports, sample dataset, feature/target split, train/test split  
    - Train `LinearRegression`, inspect slope/intercept, make predictions, evaluate with MSE & R²  
    - Visualize the fitted line over the data and highlight key learnings  
  - A **multiple linear regression exercise** (Area, Bedrooms, Age → Price):
    - Students create a tiny DataFrame with 3 features and a price column  
    - Follow the same step structure to split, train, evaluate, and predict a new house  
    - Includes a suggested “Actual vs Predicted” scatter plot for the test set  
  - Start here before trying any of the classifier notebooks.
- `class-3-logistic-regression-basics.ipynb`
  - A **Logistic Regression (classification) walkthrough** that mirrors the *Logistic_Regression_demo1.pdf* slides:
    - Objective: classify Pass / Fail from study hours.  
    - Uses the same 10‑step pattern as the Linear Regression notebook.  
    - Includes accuracy, confusion matrix, and a simple prediction for a new student.
- `multi_reg1.ipynb` — scratch/experimental notebook for multi‑regression variants.
- Slide PDFs that go with these notebooks:
  - `Linear_Regression_demo1.pdf`  
  - `Logistic_Regression_demo1.pdf`  
  - `Decision_Tree_demo.pdf`  
  - `Random_Forest_demo.pdf`  
  - `KNN.pdf`  
  - `Supervised Learning Algorithms.pdf` (overview + common step structure)

- The notebooks are intentionally written to be **approachable for new Python users** (small datasets, clear comments) and still interesting for engineers (explicit equations, model coefficients, and evaluation metrics).

## Supervised learning roadmap (from the slides)

Class 3 and later classes will use the same pattern for a small, practical subset of supervised learning algorithms.

- **Regression algorithms** (predict values)
  - Linear Regression *(implemented here)*  
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

