# Lab 04 — Python Data Structures & Clean Code

## Concepts Practiced
- Lists, Tuples, Dictionaries, and Sets
- Aliasing, Shallow Copying vs. Deep Copying
- Dictionary Hashability and Keys
- List, Dictionary, and Set Comprehensions
- Iteration utilities (`enumerate()`, `zip()`)
- Clean code refactoring and file modularity

## Tasks Completed
1. Task 1 — Working with Lists (`task01_lists.py`)
2. Task 2 — Aliasing vs Copying (`task02_copying.py`)
3. Task 3 — Tuples for Fixed Data (`task03_tuples.py`)
4. Task 4 — Dictionaries for Structured Records (`task04_dictionaries.py`)
5. Task 5 — Sets for Unique Labels & Validation (`task05_sets.py`)
6. Task 6 — Comprehensions (`task06_comprehensions.py`)
7. Task 7 — `enumerate()` & `zip()` (`task07_iteration_tools.py`)
8. Task 8 — Data Structure Selection (`task08_data_modeling.py`)
9. Task 9 — Prediction Analysis (`task09_clean_code/`)

## Data Structure Decisions (Task 8)
- **Scenario A (Ordered Models): `list`** — Retains evaluation sequence order.
- **Scenario B (Fixed Image Size): `tuple`** — Represents immutable dimensions `(224, 224)`.
- **Scenario C (Model Parameters): `dictionary`** — Enables key-value lookup for explicit field names.
- **Scenario D (Unique Class Labels): `set`** — Automatically removes duplicate class labels.
- **Scenario E (Multiple Prediction Records): `list` of `dictionaries`** — Stores structured records sequentially.
- **Scenario F (Label Validation): `set`** — Facilitates fast set difference (`-`) operations for validation.

## Aliasing vs Copying (Task 2)
In Part A, assigning `processed_scores = original_scores` created an alias pointing to the same list in memory. `.copy()` resolved this in Part B by creating a new shallow copy. However, in Part C, `.copy()` was insufficient because nested dictionaries were still referenced by both lists; `copy.deepcopy()` was required to recursively duplicate the nested structures.

## Hashability (Task 3 Part C)
Dictionary keys in Python must be hashable, meaning their hash value remains constant throughout their lifetime. Immutable types like tuples are hashable, whereas mutable types like lists cannot be hashed and raise a `TypeError`.

## Sets vs Lists for Validation (Task 5)
Sets are preferred over lists for label validation because set difference operators (`-`) express set operations directly. Furthermore, set lookups operate in $O(1)$ average time complexity compared to $O(N)$ for linear list searches.

## Clean-Code Refactoring (Task 9)
1. **Original Code Shortcomings:** Used non-descriptive single-letter variable names (`x`, `y`, `z`, `d`), lacked modularity, and mixed filtering and counting logic.
2. **Behavior Verification:** Tested outputs against original values (`Selected IDs: [1, 4, 5, 6]`).
3. **Incomplete Records:** Missing fields are reported explicitly rather than silently dropped to ensure data auditability.

## Edge Cases Tested
1. Empty inputs to `average_confidence([])` return `None`.
2. Confidence score equal to the boundary `0.80` is included (`>=`).
3. Label normalization preserves the original raw record structures intact.