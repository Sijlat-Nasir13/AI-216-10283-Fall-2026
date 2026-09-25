# Why might this logic later be placed inside a reusable function?
# Placing this logic inside a function allows us to easily evaluate score lists 
# across different models, cross-validation folds, or datasets without duplicating code.

scores = [0.72, 0.81, 0.88, 0.91, 0.67, 0.86, 0.79]
threshold = 0.85

if not scores:
    print("Score list is empty. No analysis to perform.")
else:
    meeting_target = 0
    below_target = 0
    total_score = 0.0

    for score in scores:
        total_score += score
        if score >= threshold:
            meeting_target += 1
        else:
            below_target += 1

    average_score = total_score / len(scores)
    percentage_meeting = (meeting_target / len(scores)) * 100

    print(f"Meeting target (>= {threshold}): {meeting_target}")
    print(f"Below target: {below_target}")
    print(f"Average score: {average_score:.2f}")
    print(f"Percentage meeting target: {percentage_meeting:.2f}%")