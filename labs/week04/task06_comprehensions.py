# task06_comprehensions.py - List, Dict, and Set Comprehensions

def main():
    # Part A: List Comprehension
    raw_scores = [78, -5, 92, 110, 67, 85]
    valid_scores = [s for s in raw_scores if 0 <= s <= 100]
    normalized_scores = [s / 100 for s in valid_scores]

    print(f"Valid: {valid_scores}")
    print(f"Normalized: {normalized_scores}")

    # Part B: Dictionary Comprehension
    student_scores = {
        "Ali": 72,
        "Sara": 91,
        "Ahmed": 45,
        "Fatima": 88
    }
    pass_status = {name: score >= 50 for name, score in student_scores.items()}
    print(f"Pass status: {pass_status}")

    # Part C: Set Comprehension
    labels = ["Spam", "HAM", "spam", "Ham", "UNKNOWN"]
    normalized_labels = {label.strip().lower() for label in labels}
    print(f"Labels: {sorted(list(normalized_labels))}")

if __name__ == "__main__":
    main()