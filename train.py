# Script for training a text classification model.
#
# Copyright (C) Saul Johnson 2022
# Author: Saul Johnson <saul.a.johnson@gmail.com>
# Usage: python3 train.py
#
# Used for a 2022 guest lencture at NHL Stenden Leeuwarden.
# See requirements.txt for dependencies.

from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
# from sklearn.linear_model import SGDClassifier
# from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import plot_confusion_matrix, confusion_matrix, classification_report, accuracy_score

import matplotlib.pyplot as plt
import joblib


# Load files in data directory, taking subdirectories as classes.
dataset = load_files('./data', load_content=True, encoding='UTF-8', decode_error='replace')

# Split into testing and training data.
x_train, x_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.2) # 20% test data.

# Choose classifier (uncomment the lines below to select).
classifier = MultinomialNB() # Multinomial Naive Bayes.
# classifier = SGDClassifier() # Linear SVM.
# classifier = RandomForestClassifier() # Random forest.

# Create pipeline.
pipeline = Pipeline([('vectorizer', CountVectorizer()), # Convert to token count matrix.
                    ('tfidf', TfidfTransformer()), # TFIDF normalization.
                    ('classifier', classifier)])

# Actually train  model.
pipeline.fit(x_train, y_train)

# Put the model to the test.
y_pred = pipeline.predict(x_test)

# Confusion matrix, how many classification errors did we make?
print('CONFUSION MATRIX ===============')
print(confusion_matrix(y_test, y_pred), '\n')

# Classification report, what's our overall accuracy, support, F1 score and so on?
print('CLASSIFICATION REPORT ==========')
print(classification_report(y_test, y_pred), '\n')

# What's our overall accuracy?
print('OVERALL ACCURACY ===============')
print(accuracy_score(y_test, y_pred), '\n')

# Plot confusion matrix as image using matplotlib and show it.
plot_confusion_matrix(pipeline, x_test, y_test,
    display_labels=dataset.target_names,
    cmap=plt.cm.Greens,
    normalize='true')
plt.show()

# Pickle trained model to file for later use.
joblib.dump(pipeline, './classifier.pickle')
