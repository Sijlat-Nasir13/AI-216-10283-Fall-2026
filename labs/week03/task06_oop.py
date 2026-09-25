# Task 6: Object-Oriented Score Analyzer

class ScoreAnalyzer:
    def __init__(self, scores):
        self.scores = list(scores) if scores else []

    def clean(self):
        self.scores = [s for s in self.scores if 0 <= s <= 100]

    def average(self):
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)

    def count_above(self, threshold):
        return sum(1 for s in self.scores if s >= threshold)

    def summary(self):
        if not self.scores:
            return {
                "count": 0,
                "average": None,
                "highest": None,
                "lowest": None
            }
        return {
            "count": len(self.scores),
            "average": round(self.average(), 2),
            "highest": max(self.scores),
            "lowest": min(self.scores)
        }


if __name__ == "__main__":
    raw_scores = [78, -5, 110, 67, 90, 88]
    
    analyzer = ScoreAnalyzer(raw_scores)
    print("Initial Scores:", analyzer.scores)
    
    analyzer.clean()
    print("Cleaned Scores:", analyzer.scores)
    print("Average:", analyzer.average())
    print("Count >= 80:", analyzer.count_above(80))
    print("Summary Dict:", analyzer.summary())