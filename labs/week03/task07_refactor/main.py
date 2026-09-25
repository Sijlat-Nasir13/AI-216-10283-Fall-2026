# main.py - High-level coordination script

import sys
from pathlib import Path

# Ensure task07_refactor directory is in the Python import path
sys.path.append(str(Path(__file__).parent))

from preprocessing import clean_scores
from analyzer import ScoreAnalyzer


def main():
    raw_scores = [78, -5, 92, 110, 67, 88]

    # 1. Preprocess / Clean Data
    cleaned_scores = clean_scores(raw_scores)

    # 2. Instantiate Analyzer with Cleaned Data
    analyzer = ScoreAnalyzer(cleaned_scores)

    # 3. Output Workflow Summary
    print("Task 07 Refactored Workflow Summary")
    print("Raw Data:", raw_scores)
    print("Cleaned Data:", cleaned_scores)
    print(
        "Average Score:",
        (
            round(analyzer.average(), 2)
            if analyzer.average() is not None
            else "N/A"
        ),
    )
    print("Qualified (>= 70):", analyzer.count_above(70))
    print("Highest Score:", analyzer.highest())
    print("Lowest Score:", analyzer.lowest())


if __name__ == "__main__":
    main()