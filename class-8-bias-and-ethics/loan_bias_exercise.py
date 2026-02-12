"""
Class 8 Exercise: Bias in Loan Approval

Scenario: A bank has an AI system that approves loans. There is a suspicion
that it favors one specific group. As an ethical AI engineer, you investigate
by generating a biased dataset, training a model, and evaluating it.

Features: income / credit_score / gender
Label: approved

HOW TO RUN:
  From the repo root:
    pip install -r requirements.txt
    python class-8-bias-and-ethics/loan_bias_exercise.py

  Or from this directory:
    pip install numpy pandas scikit-learn
    python loan_bias_exercise.py
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# =============================================================================
# STEP 1: Create loan dataset with bias by income
# =============================================================================

np.random.seed(42)

loandata = pd.DataFrame({
    "income": np.random.randint(30, 150, 100) * 1000,  # 30k–150k
    "credit_score": np.random.randint(300, 850, 100),
    "gender": np.random.choice(["Male", "Female"], 100),
})

# Merit-based approval: income > 50k and credit_score > 600
loandata["approved"] = (
    (loandata["income"] > 50000) & (loandata["credit_score"] > 600)
).astype(int)

# Introduce bias by income: high-income applicants get 70% approval
# regardless of credit score (simulates favoritism toward wealthier applicants)
loandata.loc[loandata["income"] > 80000, "approved"] = np.where(
    np.random.rand(len(loandata[loandata["income"] > 80000])) > 0.3, 1, 0
)

print("Loan data (first 10 rows):")
print(loandata.head(10))
print()

# =============================================================================
# STEP 2: Encode categorical features, prepare X and y
# =============================================================================

# Only encode gender; income and credit_score are already numeric
le = LabelEncoder()
loandata["gender"] = le.fit_transform(loandata["gender"])

X = loandata[["income", "credit_score", "gender"]]
y = loandata["approved"]

# =============================================================================
# STEP 3: Train model and evaluate
# =============================================================================

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Classification report (model WITH income as feature):")
print(classification_report(y_test, y_pred))
print()

# =============================================================================
# STEP 4: Compare with model trained WITHOUT income (investigate bias)
# =============================================================================

print("---------Remove income (investigate income bias)---------")
X_no_income = loandata[["credit_score", "gender"]]

X_train, X_test, y_train, y_test = train_test_split(X_no_income, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Classification report (model WITHOUT income):")
print(classification_report(y_test, y_pred))
