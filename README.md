# Total AI

Total AI aims to be a deterministic, always accurate classifier. This is a work in
progress, currently only single digit classification is supported. The classifier uses a
version of NLP to determine what the given image file shows.

## Usage

To classify the image `filename`, do

```sh
python3 totalai.py filename
```

Both relative and absolute paths can be used. Any image file format can be used.

For example, to classify `1.png` in `examples/`, do

```sh
python3 totalai.py examples/1.png
```

## Contribute

Contributions are very welcome! Open an issue if you have any questions 🙃 The main work
is extending the `classifier.csv` file with examples for the different image classes.
Currently the classifier is extremely biased, it only works with english images. Any
contributions for other languages are very welcome!
