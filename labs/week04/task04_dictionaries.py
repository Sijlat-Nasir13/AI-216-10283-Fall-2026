# task04_dictionaries.py - Structured Dictionaries and Nested Access

def main():
    # Part A: Dictionary Operations
    model_info = {
        "name": "spam_classifier",
        "version": 2,
        "accuracy": 0.92,
        "threshold": 0.80,
        "status": "evaluated"
    }

    print(f"Model Name: {model_info['name']}")

    model_info["accuracy"] = 0.94
    model_info["owner"] = "AI-216 Team"

    gpu_setting = model_info.get("gpu_enabled", False)
    print(f"GPU Enabled (defaulted): {gpu_setting}")

    print("\nModel Details:")
    for key, value in model_info.items():
        print(f"  {key}: {value}")

    # Part B: Nested Dictionary
    model_info["metrics"] = {
        "accuracy": 0.94,
        "precision": 0.91,
        "recall": 0.89
    }

    print(f"\nPrecision: {model_info['metrics']['precision']}")
    print(f"Recall: {model_info['metrics']['recall']}")

if __name__ == "__main__":
    main()