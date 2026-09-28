"""
AI Fundamentals scratchpad.

Run: python scratch.py
This script demonstrates small, dependency-free examples inspired by the course topics.
"""

from __future__ import annotations

def print_header(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def ai_overview() -> None:
    print_header("AI Fundamentals - Quick Tour")
    topics = [
        "Introduction to Artificial Intelligence",
        "Core Concepts in AI",
        "Machine Learning Basics",
        "Deep Learning Basics",
        "Natural Language Processing (NLP)",
        "Computer Vision Basics",
        "Tools & Platforms for AI",
        "Ethics & Responsible AI",
        "Capstone Mini Projects",
        "Review & Assessment",
    ]
    for idx, topic in enumerate(topics, start=1):
        print(f"{idx:2d}. {topic}")


def ml_basics_demo() -> None:
    print_header("Machine Learning Basics - Tiny Linear Regression")
    # A simple dataset: hours studied vs score (toy example).
    hours = [1, 2, 3, 4, 5]
    scores = [52, 55, 61, 68, 72]

    n = len(hours)
    mean_x = sum(hours) / n
    mean_y = sum(scores) / n

    # Least squares slope and intercept (no external libraries).
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(hours, scores))
    denominator = sum((x - mean_x) ** 2 for x in hours)
    slope = numerator / denominator
    intercept = mean_y - slope * mean_x

    prediction = slope * 6 + intercept
    print(f"Model: score = {slope:.2f} * hours + {intercept:.2f}")
    print(f"Predicted score for 6 hours: {prediction:.1f}")


def nlp_demo() -> None:
    print_header("NLP Basics - Tokenization + Word Count")
    text = (
        "AI helps machines learn from data. "
        "NLP lets machines understand human language."
    )
    # Simple tokenization: lowercase and split on spaces/punctuation.
    cleaned = (
        text.lower()
        .replace(".", "")
        .replace(",", "")
        .replace("!", "")
        .replace("?", "")
    )
    tokens = cleaned.split()
    counts: dict[str, int] = {}
    for token in tokens:
        counts[token] = counts.get(token, 0) + 1

    print("Tokens:", tokens)
    print("Word counts:", counts)


def cv_demo() -> None:
    print_header("Computer Vision Basics - Simple Edge Detector")
    # 5x5 grayscale image (0-9) with a vertical edge in the middle.
    image = [
        [1, 1, 1, 8, 8],
        [1, 1, 1, 8, 8],
        [1, 1, 1, 8, 8],
        [1, 1, 1, 8, 8],
        [1, 1, 1, 8, 8],
    ]

    # Simple horizontal gradient filter (Sobel-like, minimal).
    kernel = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1],
    ]

    def apply_kernel(img: list[list[int]]) -> list[list[float]]:
        height = len(img)
        width = len(img[0])
        output = [[0.0 for _ in range(width)] for _ in range(height)]
        for r in range(1, height - 1):
            for c in range(1, width - 1):
                total = 0
                for kr in range(3):
                    for kc in range(3):
                        total += kernel[kr][kc] * img[r + kr - 1][c + kc - 1]
                output[r][c] = abs(total)
        return output

    edges = apply_kernel(image)
    for row in edges:
        print(" ".join(f"{value:4.0f}" for value in row))


def ethics_demo() -> None:
    print_header("Ethics & Responsible AI - Simple Checklist")
    checklist = [
        "Is the data representative of all users?",
        "Are privacy and consent handled properly?",
        "Can we explain how the model makes decisions?",
        "Have we tested for bias or unfair outcomes?",
        "Is there a plan for monitoring in production?",
    ]
    for item in checklist:
        print(f"- {item}")


def main() -> None:
    ai_overview()
    ml_basics_demo()
    nlp_demo()
    cv_demo()
    ethics_demo()


if __name__ == "__main__":
    main()
