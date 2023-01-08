# Introduction to Machine Learning for Text Classification
Source code for my 2022 text classification guest lecture at NHL Stenden Leeuwarden.

![Applied Text Classification: Lecture by Saul Johnson](header.png)

## Prerequisites
To run this project, you'll need:

* Python 3.6 or later with pip and virtual environments

## Setup
Setup will vary depending on whether you're using Windows or Mac/Linux. A script is included for each OS that will do the following for you:

* Delete any existing virtual environment for this project
* Provision fresh virtual environment
* Install all dependencies for this project in that virtual environment

### Windows
On Windows, execute `setup-venv.bat` via your command prompt from the root directory of the repository:

```
./setup-venv.bat
```

### On Mac/Linux
On Mac/Linux, execute `setup-venv.sh` via your terminal from the root directory of the repository. Make sure to invoke it using `bash`:

```
bash ./setup-venv.sh
```

## Training a Model
First, prep your data. Do this like so:

1. Place each of your documents into a separate plain text (`*.txt`) file (check out `split_csv.py` for a starting point to do this programmatically)
2. Create a folder called `data` in the repository root directory
3. Within this `data` directory, make subfolders corresponding to your classes
4. Place your documents (text files) in the appropriate subfolder according to their class

Next, make sure you're in the virtual environment we set up earlier:

* **On Windows** - Run `./venv/Scripts/activate` in your command prompt from the repo root directory
* **On Mac/Linux** - Tun `. venv/bin/activate` in your terminal from the repo root directory

Now, go ahead and run `train.py` like so:

```
python3 ./train.py
```

The program will train the model and print its confusion matrix, classification report and overall accuracy to the command line and plot/show the confusion matrix using matplotlib.

Your trained model will be picked to disk at `./classifier.pickle` ready to load and use from your own programs.

## Querying the Model
Now, you can run `interact.py` which will start a program that will accept typed input, run it through your trained classifier and display the classification.

Alternatively, you can load and use the model programmatically:

```python
from joblib import load

# Load trained model.
pipeline = load('./classifier.pickle')

# Use your trained model here...
# pipeline.predict(['<My input>'])
```

## Limitations
This example code has some limitations:

* `train.py` will only train models on unigrams out-of-the-box. Check out the `ngram_range` parameter of `CountVectorizer` if you're interested in training on ngrams!
* Stopwords will not be removed for you. Take a look at the `stop_words` parameter of `CountVectorizer` if you're interested in stopword removal!

This article on [Practical Data Science](https://practicaldatascience.co.uk/machine-learning/how-to-use-count-vectorization-for-n-gram-analysis) will point you in the right direction when it comes to the above.

Cross-validation, minimization of bias etc. are very important. Wield AI/ML responsibly.
