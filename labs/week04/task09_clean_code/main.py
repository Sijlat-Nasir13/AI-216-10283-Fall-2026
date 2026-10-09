from preprocessing import filter_by_confidence, split_complete_records, normalize_labels
from analysis import (
    count_by_label,
    get_unique_labels,
    find_unexpected_labels,
    average_confidence,
    top_predictions,
)

MIN_CONFIDENCE = 0.80
ALLOWED_LABELS = {"spam", "ham", "promotion"}
REQUIRED_FIELDS = ("id", "label", "confidence")
TOP_COUNT = 3

initial_predictions = [
    {"id": 1, "label": "spam", "confidence": 0.94},
    {"id": 2, "label": "ham", "confidence": 0.72},
    {"id": 3, "label": "promotion", "confidence": 0.41},
    {"id": 4, "label": "spam", "confidence": 0.89},
    {"id": 5, "label": "ham", "confidence": 0.97},
    {"id": 6, "label": "promotion", "confidence": 0.83},
    {"id": 7, "label": "ham", "confidence": 0.58},
]

new_batch = [
    {"id": 8, "label": "Spam", "confidence": 0.91},
    {"id": 9, "label": "ham"},
    {"id": 10, "label": "unknown", "confidence": 0.86},
    {"id": 11, "label": " HAM ", "confidence": 0.66},
]

def main():
    combined_batch = initial_predictions + new_batch

    valid_records, skipped_ids = split_complete_records(combined_batch, REQUIRED_FIELDS)
    normalized_valid = normalize_labels(valid_records)

    high_conf = filter_by_confidence(normalized_valid, MIN_CONFIDENCE)
    label_counts = count_by_label(normalized_valid)
    all_labels = get_unique_labels(normalized_valid)
    unexpected = find_unexpected_labels(normalized_valid, ALLOWED_LABELS)
    avg_conf = average_confidence(normalized_valid)
    top_ids = top_predictions(normalized_valid, TOP_COUNT)

    summary = {
        "total_records": len(combined_batch),
        "valid_records": len(normalized_valid),
        "skipped_ids": skipped_ids,
        "labels": all_labels,
        "label_counts": label_counts,
        "high_confidence_count": len(high_conf),
        "unexpected_labels": unexpected,
        "average_confidence": round(avg_conf, 3) if avg_conf else 0.0,
        "top_ids": top_ids,
    }

    print("=== Prediction Report ===")
    print(f"Total records:          {summary['total_records']}")
    print(f"Valid records:          {summary['valid_records']}")
    print(f"Skipped (missing data): {summary['skipped_ids']}")
    print(f"Labels:                 {summary['labels']}")
    print(f"Label counts:           {summary['label_counts']}")
    print(f"High confidence (>= 0.8): {summary['high_confidence_count']}")
    print(f"Unexpected labels:      {summary['unexpected_labels']}")
    print(f"Average confidence:     {summary['average_confidence']}")
    print(f"Top {TOP_COUNT} by confidence:   {summary['top_ids']}\n")

    print(f"Raw label of record 8 in new_batch: '{new_batch[0]['label']}' (Unchanged)")

if __name__ == "__main__":
    main()