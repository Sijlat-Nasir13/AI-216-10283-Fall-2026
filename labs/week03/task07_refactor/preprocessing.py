# preprocessing.py - Data cleaning utilities

def clean_scores(scores):
    if not scores:
        return []
    return [s for s in scores if 0 <= s <= 100]