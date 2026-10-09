# task03_tuples.py - Tuples, Unpacking, and Hashability

def summarize_scores(scores):
    if not scores:
        return None
    return min(scores), max(scores), sum(scores) / len(scores)

def main():
    # Part A: Unpacking
    image_size = (224, 224)
    model_result = ("baseline_cnn", 0.91)

    width, height = image_size
    model_name, accuracy = model_result

    print(f"Image size: {width} x {height}")
    print(f"Model: {model_name} | Accuracy: {accuracy}")

    # Part B: Returning Tuples
    scores_data = [72, 88, 91, 67]
    summary = summarize_scores(scores_data)
    if summary is not None:
        minimum, maximum, average = summary
        print(f"Minimum: {minimum} | Maximum: {maximum} | Average: {average}")

    empty_summary = summarize_scores([])
    print(f"Empty: {empty_summary}")

    # Part C: Tuples as Dictionary Keys
    input_models = {
        (224, 224): "resnet50",
        (299, 299): "inception_v3",
        (384, 384): "vit_base"
    }

    print(f"Model for 299x299: {input_models[(299, 299)]}")

    try:
        invalid_dict = {[224, 224]: "resnet50"}
    except TypeError as e:
        print(f"TypeError: {e}")

if __name__ == "__main__":
    main()