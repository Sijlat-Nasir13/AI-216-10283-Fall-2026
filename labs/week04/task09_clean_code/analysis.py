def count_by_label(predictions):
    """Count occurrences of each label."""
    counts = {}
    for record in predictions:
        label = record["label"]
        counts[label] = counts.get(label, 0) + 1
    return counts

def get_unique_labels(predictions):
    """Return sorted unique labels."""
    return sorted(list({record["label"] for record in predictions if "label" in record}))

def find_unexpected_labels(predictions, allowed_labels):
    """Find labels present in predictions that are not in allowed_labels."""
    found_labels = {record["label"] for record in predictions if "label" in record}
    return sorted(list(found_labels - set(allowed_labels)))

def average_confidence(predictions):
    """Calculate average confidence. Return None if empty."""
    confidences = [p["confidence"] for p in predictions if "confidence" in p]
    if not confidences:
        return None
    return sum(confidences) / len(confidences)

def top_predictions(predictions, count):
    """Return IDs of top N predictions by confidence."""
    sorted_records = sorted(
        [p for p in predictions if "confidence" in p],
        key=lambda x: x["confidence"],
        reverse=True
    )
    return [p["id"] for p in sorted_records[:count]]