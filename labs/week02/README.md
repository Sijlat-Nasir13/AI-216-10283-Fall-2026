# Lab 02: Python Fundamentals for Problem Solving

## Overview
This lab covers key Python concepts used to solve everyday programming problems. Across these tasks, I worked with conditional statements (`if-elif-else`), loops (`for` and `while`), list processing, and breaking down problems into reusable functions.

---

## Tasks & Files

### 1. Personal Expense Tracker (`task01_expense_tracker.py`)
Calculates total monthly spending from a list of expenses, compares it against a target budget, and reports whether spending stayed within limits.

### 2. Internet Package Advisor (`task02_package_advisor.py`)
Takes a user's monthly data usage (in GB) and recommends the best plan (Basic, Standard, or Premium) based on predefined data tiers.

### 3. Temperature Monitor (`task03_temperature_monitor.py`)
Loops through daily temperature readings, categorizes each reading into thermal bands (Below Normal, Normal, High), and outputs total counts for each group.

### 4. Score Analysis (`task04_score_analysis.py`)
Analyzes model performance scores to calculate the overall average score and the percentage of scores meeting a minimum quality threshold.

### 5. Eligibility Checker (`task05_eligibility.py`)
Uses boolean conditions to check if an applicant meets age, score, and prerequisite requirements, displaying specific feedback if any condition fails.

### 6. Utility Functions (`task06_functions.py`)
Demonstrates modular programming by defining reusable functions (`calculate_percentage`, `is_passing`, and `count_values_above_threshold`).

### 7. Power Consumption Breakdown (`task07_decomposition.py`)
Processes daily electricity usage (kWh) readings and computes both count and percentage breakdowns for Low, Normal, and High consumption tiers.

### Optional Challenge: CLI Menu (`optional_menu.py`)
An interactive, continuous terminal menu powered by a `while` loop that lets users run calculation tools until choosing to exit.

---

## Test Cases & Verification

| Script | Test Input | Expected Output | Status |
| :--- | :--- | :--- | :---: |
| `task01_expense_tracker.py` | `[150, 450, 200]`, Budget: `1000` | Total: 800, Remaining: 200, Status: Within budget | Pass |
| `task02_package_advisor.py` | `5` GB | Recommended Package: Basic | Pass |
| `task03_temperature_monitor.py` | `[21.5, 29.0, 32.5, 18.0, 35.2, 27.8, 14.0]` | Below Normal: 1, Normal: 4, High: 2 | Pass |
| `task04_score_analysis.py` | `[0.72, 0.81, 0.88, 0.91, 0.67, 0.86, 0.79]`, Threshold: `0.85` | Avg: 0.81, Meeting Target: 42.86% | Pass |
| `task05_eligibility.py` | Age: 19, Score: 72, Prereq: True | Status: Eligible | Pass |
| `task06_functions.py` | `calculate_percentage(423, 500)` | `84.6` | Pass |
| `task07_decomposition.py` | `[3.2, 5.0, 7.5, 10.0, 12.4, 4.9, 10.1]` | Low: 2 (28.57%), Normal: 3 (42.86%), High: 2 (28.57%) | Pass |

---

## AI Collaboration Log

* **AI Tool:** Gemini
* **Where It Helped:**
  * Debugging file path issues and terminal execution errors during workspace setup.
  * Verifying control flow logic and output formatting across all tasks.
  * Formatting clean Markdown tables and summary documentation.
* **Personal Contribution:** All code was tested, verified locally in VS Code, and committed incrementally through Git.