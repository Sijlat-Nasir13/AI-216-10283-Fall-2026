# main.py - Main execution script using score_utils module

import sys
from pathlib import Path

# Ensure task03_modules directory is on Python search path
sys.path.append(str(Path(__file__).parent))

from score_utils import calculate_average, is_passing, count_above_threshold


def main():
    scores = [72, 88, 45, 91, 67]

    avg = calculate_average(scores)
    first_passing = is_passing(scores[0])
    count_80 = count_above_threshold(scores, 80)

    print("--- Task 03 Module Output ---")
    print(f"Scores: {scores}")
    print(f"Average Score: {avg:.2f}")
    print(f"Is First Score ({scores[0]}) Passing?: {first_passing}")
    print(f"Number of Scores >= 80: {count_80}")


if __name__ == "__main__":
    main()