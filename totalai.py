import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    classifier = get_classifier()
    predictions = predict(args.filename, classifier)

    if predictions:
        prediction_str = "prediction" if len(predictions) == 1 else "predictions"
        print(f"{len(predictions)} {prediction_str} found:")
        print(*predictions)
    else:
        print("No predictions found")

def get_classifier():
    classifier = {}
    with open("classifier.csv") as f:
        for line in f:
            items = line.strip().split(",")
            image_class = items[0]
            classifier[image_class] = items
    return classifier

def predict(image_name, classifier):
    return [image_class for image_class, examples in classifier.items()
            if any(example in image_name for example in examples)]

if __name__ == "__main__":
    main()
