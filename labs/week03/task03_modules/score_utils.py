# score_utils.py - Module for score calculation functions

def calculate_average(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)


def is_passing(score, passing_score=50):
    return score >= passing_score


def count_above_threshold(scores, threshold):
    if not scores:
        return 0
    return sum(1 for s in scores if s >= threshold)


if __name__ == "__main__":
    print("--- Running score_utils.py directly (Demo Mode) ---")
    demo_scores = [10, 50, 90]
    print("Demo Average:", calculate_average(demo_scores))
    print("Demo Pass (50):", is_passing(50))
    print("Demo Count >= 40:", count_above_threshold(demo_scores, 40))