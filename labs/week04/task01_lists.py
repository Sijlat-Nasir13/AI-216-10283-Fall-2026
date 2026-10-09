# task01_lists.py - Working with Lists and List Methods

THRESHOLD = 0.85

def main():
    accuracies = [0.82, 0.91, 0.87, 0.78, 0.93, 0.85]

    
    print(f"First: {accuracies[0]}")
    print(f"Last: {accuracies[-1]}")

    
    print(f"Middle four: {accuracies[1:5]}")

    
    accuracies.append(0.89)

   
    accuracies.extend([0.84, 0.90])

    
    idx_078 = accuracies.index(0.78)
    accuracies[idx_078] = 0.80

    print(f"Updated: {accuracies}")

   
    high_score_count = sum(1 for score in accuracies if score >= THRESHOLD)
    print(f"Scores >= {THRESHOLD}: {high_score_count}")

    
    print(f"Highest: {max(accuracies)}")
    print(f"Lowest: {min(accuracies)}")

    
    sorted_accuracies = sorted(accuracies, reverse=True)
    print(f"Sorted (high to low): {sorted_accuracies}")

    
    print(f"Original order kept: {accuracies}")

if __name__ == "__main__":
    main()