def filter_by_confidence(predictions, min_confidence):
    """Filter predictions with confidence >= min_confidence."""
    return [p for p in predictions if p.get("confidence", 0) >= min_confidence]

def split_complete_records(predictions, required_fields):
    """Separate predictions into complete and incomplete records based on required keys."""
    complete = []
    incomplete_ids = []
    for record in predictions:
        if all(field in record for field in required_fields):
            complete.append(record)
        else:
            incomplete_ids.append(record.get("id", "Unknown"))
    return complete, incomplete_ids

def normalize_labels(predictions):
    """Return a new list with stripped and lowercased labels without mutating inputs."""
    normalized = []
    for record in predictions:
        new_record = record.copy()
        if "label" in new_record and isinstance(new_record["label"], str):
            new_record["label"] = new_record["label"].strip().lower()
        normalized.append(new_record)
    return normalized