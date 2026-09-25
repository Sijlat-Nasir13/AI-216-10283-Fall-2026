# Lab 03 — Functions, Modules, Exceptions, Debugging & OOP

## Concepts Practiced
- Functions and reusable modular logic
- Scope (Local vs. Global)
- Custom modules and `if __name__ == "__main__":` main guards
- Exception handling (`try`, `except`, `else`, `finally`, `raise`)
- Systematic debugging and trace analysis
- Object-Oriented Programming (Classes, instance attributes, methods, `self`)
- Structural refactoring and separation of concerns

---

## Tasks Completed

1. **Task 01 — Functions:** Written in `task01_functions.py` to calculate averages, find highest scores, threshold counts, and classify performance.
2. **Task 02 — Scope:** Written in `task02_scope.py` to demonstrate local vs. global variable isolation and refactoring with explicit parameter passing.
3. **Task 03 — Modules:** Created `task03_modules/score_utils.py` and `task03_modules/main.py` using module imports and main guards.
4. **Task 04 — Exceptions:** Implemented in `task04_exceptions.py` using `ValueError` validation for invalid percentage ranges and non-numeric inputs.
5. **Task 05 — Debugging:** Fixed accumulator assignment and condition ordering in `task05_debugging.py`.
6. **Task 06 — OOP Class:** Implemented `ScoreAnalyzer` class in `task06_oop.py` with score cleaning and summary dict return values.
7. **Task 07 — Refactoring:** Structured procedural analysis into modular files: `preprocessing.py`, `analyzer.py`, and `main.py`.

---

## Task 2 Scope & Hidden State Reflection

* **Part A Scope Explanation:** The variable `score = 90` is global. Inside `show_score()`, `score = 70` creates a local variable that exists only within the function frame. Printing outside the function accesses the global state.
* **Part B Reflection:** Explicit parameters make functions pure and independent of hidden global state, allowing them to be tested, reused, and maintained without unintended side effects.

---

## Task 3 Module Guard Question

* **`if __name__ == "__main__":` Guard:** This guard ensures that code inside it runs only when the script is executed directly (`python score_utils.py`). When imported into another script (`import score_utils`), `__name__` takes the module name, suppressing demo execution during imports.

---

## Task 4 Exception Handling Test Cases

| Case | Input (`obtained`, `total`) | Expected Result | Actual Result |
| :--- | :--- | :--- | :--- |
| **Valid** | `80`, `100` | Calculated Percentage: 80.00% | Calculated Percentage: 80.00% |
| **Negative Input** | `-5`, `100` | Validation Error: Obtained marks cannot be negative. | Validation Error: Obtained marks cannot be negative. |
| **Obtained > Total** | `120`, `100` | Validation Error: Obtained marks cannot exceed total marks. | Validation Error: Obtained marks cannot exceed total marks. |
| **Zero Division** | `80`, `0` | Validation Error: Total marks must be greater than zero. | Validation Error: Total marks must be greater than zero. |
| **Non-Numeric** | `"abc"`, `100` | Validation Error: could not convert string to float | Validation Error: could not convert string to float |

---

## Task 5 Debugging Notes

1. **Bug 1 (Accumulation Error):** In `calculate_average()`, `total = score` continuously reassigned `total` instead of adding to it (`total += score`).
2. **Bug 2 (Logic Condition Order):** In `classify()`, `average >= 50` was checked before `average >= 85`, making high scores evaluate to `"Pass"` instead of `"Excellent"`.
3. **Corrected Output:**
   * Average: `75.0`
   * Result: `Pass`

---

## Design Decisions

* **Functions vs Classes:** Standard functions were used for standalone stateless data cleaning (`preprocessing.py`). A Class (`ScoreAnalyzer`) was used when holding internal state (`self.scores`) together with multiple operating methods improved cohesion.
* **`main.py` Role:** Acts strictly as an orchestrator, connecting data cleaning with analysis without containing business logic directly.

---

## AI Engineering Relevance

Clean code structure is fundamental for AI pipelines. Data preprocessing, feature engineering, and model evaluation routines must be modularized into predictable components. Proper exception handling prevents data pipelines from crashing on corrupt inputs, while object-oriented patterns align directly with popular frameworks like PyTorch and Scikit-Learn.

---

## AI Usage Log

* **Tool Used:** Gemini
* **Prompts Asked:** Code structuring assistance, PowerShell path creation commands, debugging walkthroughs, and markdown documentation formatting.
* **Verified/Changed:** All scripts were written, executed locally, tested via PowerShell, and committed incrementally into Git.