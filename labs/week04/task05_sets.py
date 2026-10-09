# task05_sets.py - Set Operations and Data Validation

def main():
    training_labels = ["spam", "ham", "spam", "promotion", "ham"]
    test_labels = ["spam", "ham", "unknown", "promotion"]

    train_set = set(training_labels)
    test_set = set(test_labels)

    print(f"Unique training labels: {sorted(list(train_set))}")
    print(f"In both: {sorted(list(train_set & test_set))}")
    print(f"Only in test: {sorted(list(test_set - train_set))}")
    print(f"In either: {sorted(list(train_set | test_set))}")

if __name__ == "__main__":
    main()