import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    classifier = get_classifier()
    predictions = predict(args.filename, classifier)

    if predictions:
        print(f"{len(predictions)} predictions found:")
        print(*predictions)
    else:
        print("No predictions found")

def get_classifier():
    classifier = {}
    with open("classifier.csv") as f:
        for line in f:
            items = line.strip().split(",")
            image_class, *examples = items
            classifier[image_class] = examples
    return classifier

def predict(image_name, classifier):
    return [image_class for image_class, examples in classifier.items()
            if any(example in image_name for example in examples)]

if __name__ == "__main__":
    main()
