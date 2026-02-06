# Class 2 - Machine Learning Basics

Hands-on ML with **NumPy**, **Pandas**, and **scikit-learn**: from raw data to model-ready features. Whether you're new to Python or an experienced engineer, you'll see the same pipeline that powers production ML—data prep, feature engineering, scaling, and train/test splits—with minimal jargon and runnable notebooks.

## The ML workflow (what we cover)

Real-world ML follows a clear path. The diagram below is the same mental model used from startups to big infra; Class 2 focuses on the first two steps so your data is ready for training.

```mermaid
flowchart LR
  subgraph one["1. Data Preparation & Acquisition"]
    A[Define goal] --> B[Collect data]
  end
  subgraph two["2. Feature Engineering"]
    B --> C[Clean & transform]
    C --> D[Select features]
  end
  subgraph three["3. Model Selection & Training"]
    D --> E[Choose algorithm]
    E --> F[Train model]
  end
  subgraph four["4. Evaluation & Validation"]
    F --> G[Metrics & tests]
  end
  subgraph five["5. Deployment & Monitoring"]
    G --> H[Production]
    H --> I[Monitor]
  end
  one --> two --> three --> four --> five
```

| Step | What it means | Notebook(s) in this class |
|------|----------------|---------------------------|
| **1. Data Preparation & Acquisition** | Define the goal and collect high-quality data. | Setup and small-dataset examples in both notebooks. |
| **2. Feature Engineering** | Clean, transform, and select the most relevant features for the model. | **data-preprocessing.ipynb** (core); **scaling-data.ipynb** (visualization + scaling). |
| **3. Model Selection & Training** | Choose an algorithm and train on prepared data. | Touched in Class 2 (train/test split); full modeling in later classes. |
| **4. Evaluation & Validation** | Test the model with appropriate metrics. | Later classes. |
| **5. Deployment & Monitoring** | Put the model in production and monitor it. | Later classes. |

**Start here:** Do **data-preprocessing.ipynb** first (DataFrames, missing values, encoding, scaling). Then **scaling-data.ipynb** (plots + scaling with the same dataset). Each notebook has an **Open in Colab** link so you can run everything in the browser with no local setup.

---

## Slides

- **[Machine Learning (Class 2) — PDF on GitHub](https://github.com/adzuci/ai-fundamentals/blob/main/class-2-machine-learning-basics/Machine%20Learning.pdf)** — Deck as PDF (view or download).

---

## Notebooks

| Notebook | What it covers |
|----------|----------------|
| **data-preprocessing.ipynb** | DataFrame basics, missing values, categorical encoding, feature scaling, train/test split. *Do this one first.* |
| **scaling-data.ipynb** | Data visualization (scatter, histogram, pandas `.plot()`), then preprocessing and scaling on the same dataset. Start here only after the preprocessing notebook. |

Each notebook has an **Open in Colab** button in the intro for no-install runs in the browser.
