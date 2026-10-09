# task02_copying.py - Aliasing, Shallow Copy, and Deep Copy

import copy

def part_a_aliasing():
    print("--- Part A: Aliasing Demo ---")
    original_scores = [70, 80, 90]
    processed_scores = original_scores
    processed_scores.append(100)
    print("Original:", original_scores)
    print("Processed:", processed_scores)

def part_b_shallow_fix():
    print("\n--- Part B: Fixing Aliasing with .copy() ---")
    original_scores = [70, 80, 90]
    processed_scores = original_scores.copy()
    processed_scores.append(100)
    print("Original:", original_scores)
    print("Processed:", processed_scores)

def part_c_nested_copying():
    print("\n--- Part C: Shallow Copy vs Deep Copy ---")
    # Shallow Copy Test
    raw_predictions = [
        {"id": 1, "label": "Spam"},
        {"id": 2, "label": "HAM"}
    ]
    shallow_copy = raw_predictions.copy()
    shallow_copy[0]["label"] = "spam"
    print("Raw after shallow copy edit:", raw_predictions)

    # Deep Copy Test
    raw_predictions = [
        {"id": 1, "label": "Spam"},
        {"id": 2, "label": "HAM"}
    ]
    deep_copied = copy.deepcopy(raw_predictions)
    deep_copied[0]["label"] = "spam"
    print("Raw after deep copy edit:", raw_predictions)
    print("Deep copy:", deep_copied)

if __name__ == "__main__":
    part_a_aliasing()
    part_b_shallow_fix()
    part_c_nested_copying()