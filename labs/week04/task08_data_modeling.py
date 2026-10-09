# Task 8 — Data Structure Selection & Modeling

# Scenario A: Store model names in the exact order they were evaluated
evaluated_models = ["baseline_cnn", "resnet50", "vit_base"]

# Scenario B: Store a fixed image size (224 x 224)
image_size = (224, 224)

# Scenario C: Store model configuration parameters with field names
model_config = {
    "name": "spam_classifier",
    "threshold": 0.80,
    "version": "2.1.0",
    "debug": False
}

# Scenario D: Store all unique class labels
unique_labels = {"spam", "ham", "promotion"}

# Scenario E: Store many prediction records
prediction_records = [
    {"id": 1, "label": "spam", "confidence": 0.94},
    {"id": 2, "label": "ham", "confidence": 0.72}
]

# Scenario F: Compare allowed labels against received labels
allowed_labels = {"spam", "ham", "promotion"}
received_labels = {"spam", "ham", "unknown"}
unexpected = received_labels - allowed_labels

if __name__ == "__main__":
    print(f"Scenario A (List): {evaluated_models}")
    print(f"Scenario B (Tuple): {image_size}")
    print(f"Scenario C (Dict): {model_config}")
    print(f"Scenario D (Set): {sorted(unique_labels)}")
    print(f"Scenario E (List of Dicts): {prediction_records}")
    print(f"Scenario F (Set Difference): Unexpected labels = {sorted(unexpected)}")