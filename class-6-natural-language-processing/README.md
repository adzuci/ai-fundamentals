# Class 6 – Natural Language Processing (NLP)

This class introduces **Natural Language Processing (NLP)**: how we turn raw text into numeric features, extract meaning, and build simple models for tasks like **classification**, **information extraction**, and **topic exploration**. We build directly on earlier classes by applying familiar ML ideas (features, vectors, models) to text.

## How this fits the course

Classes 2–5 focused on **tabular data** and **numeric features** (columns like `Age`, `Salary`, `Hours Studied`). Class 6 shows how to handle **unstructured text** (sentences, documents) by:

- Cleaning and tokenizing text into **tokens** (words / n-grams)
- Turning text into **vectors** (e.g., TF–IDF) that models can use
- Training simple **classifiers** on those vectors (e.g., sentiment / topic labels)
- Introducing concepts like **named entities**, **POS tags**, and **word sense**

```mermaid
flowchart LR
  subgraph earlier["Classes 2–5: Structured & Deep Learning"]
    A[Tabular data] --> B[Classical ML]
    B --> C[Clustering]
    C --> D[Deep learning]
  end
  subgraph nlp["Class 6 – NLP"]
    E[Text pre-processing] --> F[Vectorization (TF–IDF)]
    F --> G[Classification & topics]
  end
  earlier --> nlp
```

| Topic | What you get |
|-------|----------------|
| **NLP overview** | What NLP is, where it’s used (QA, info extraction, translation, sentiment). |
| **Text pre-processing** | Tokenization, stopwords, stemming vs lemmatization (conceptually), named entities. |
| **Vectorization** | Bag-of-words and **TF–IDF** to turn text into numeric features. |
| **Classification** | Tiny text classification example using scikit‑learn + TF–IDF. |
| **Topics & context (concepts)** | High-level view of topic models and context handling. |

**Start here:** Use `01_class_6_nlp_basics.ipynb` for an end-to-end walk from raw text → tokens → TF–IDF vectors → a simple classifier.

---

## Notebooks

| Notebook | What it covers |
|----------|----------------|
| **01_class_6_nlp_basics.ipynb** | End-to-end NLP mini‑pipeline: basic pre-processing (tokenization, lowercasing, stopwords), TF–IDF vectorization, and a tiny text classification example (e.g., positive vs negative phrases) using scikit‑learn. Connects back to the deck’s concepts: tokenization, stopwords, TF–IDF, classification, and context. *Start here.* |

All notebooks follow a clear, beginner-friendly structure:
1. Define the objective
2. Install/import libraries
3. Create or load a small text dataset
4. Pre-process text (tokens, cleaning, stopwords)
5. Vectorize with TF–IDF
6. Train a simple classifier
7. Make predictions
8. Interpret results and relate back to NLP concepts

Each notebook includes an **Open in Colab** button in the intro for no-install runs in the browser.

---

## Run locally

From the repo root:

```bash
pip install -r requirements.txt
cd class-6-natural-language-processing
jupyter notebook  # or jupyter lab
```

See the [main README](../README.md) for full setup and course schedule.
