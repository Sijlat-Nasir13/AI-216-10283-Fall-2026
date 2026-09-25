# Task 5: Debugged Code Implementation

def calculate_average(scores):
    if not scores:
        return 0.0
    total = 0
    # Fixed Bug 1: Accumulate running total with += instead of assignment =
    for score in scores:
        total += score

    return total / len(scores)


def classify(average):
    # Fixed Bug 2: Correct conditional ordering (check 85 before 50)
    if average >= 85:
        return "Excellent"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"


if __name__ == "__main__":
    scores = [60, 70, 80, 90]
    average = calculate_average(scores)
    print("Average:", average)
    print("Result:", classify(average))