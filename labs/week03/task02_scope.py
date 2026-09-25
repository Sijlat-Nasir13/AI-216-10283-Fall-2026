# Task 2: Scope & Hidden State

# Part A — Scope Observation
score = 90

def show_score():
    score = 70
    print("Inside function:", score)

print("--- Part A: Scope Demonstration ---")
show_score()
print("Outside function:", score)


# Part B — Explicit Parameter Refactoring
def is_qualified(score, threshold):
    return score >= threshold


if __name__ == "__main__":
    print("\n--- Part B: Explicit Threshold Testing ---")
    test_threshold = 0.85
    test_scores = [0.72, 0.85, 0.91]
    
    for s in test_scores:
        result = is_qualified(s, test_threshold)
        print(f"Score: {s}, Threshold: {test_threshold} -> Qualified: {result}")