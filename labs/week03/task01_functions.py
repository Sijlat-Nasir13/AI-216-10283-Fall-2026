# Task 1: Function Design & Reuse

def calculate_average(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)


def find_highest(scores):
    if not scores:
        return None
    return max(scores)


def count_above_threshold(scores, threshold):
    if not scores:
        return 0
    count = 0
    for score in scores:
        if score >= threshold:
            count += 1
    return count


def classify_average(average):
    if average is None:
        return "No valid data"
    elif average >= 85:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 50:
        return "Satisfactory"
    else:
        return "Needs Improvement"


if __name__ == "__main__":
    scores = [78, 85, 92, 67, 88]
    
    avg = calculate_average(scores)
    highest = find_highest(scores)
    above_80 = count_above_threshold(scores, 80)
    classification = classify_average(avg)
    
    print("Student Performance Summary")
    print(f"Scores: {scores}")
    print(f"Average Score: {avg:.2f}" if avg is not None else "Average Score: N/A")
    print(f"Highest Score: {highest}")
    print(f"Scores >= 80: {above_80}")
    print(f"Overall Classification: {classification}")