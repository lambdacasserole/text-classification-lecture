# Script for querying a trained text classification model.
#
# Copyright (C) Saul Johnson 2022
# Author: Saul Johnson <saul.a.johnson@gmail.com>
# Usage: python3 interact.py
#
# Used for a 2022 guest lencture at NHL Stenden Leeuwarden.
# See requirements.txt for dependencies.

import os

from joblib import load


# List directories to get classes. Filter dotfiles and sort in alphabetical order.
classes = list(filter(lambda file: not file.startswith('.'), os.listdir('./data')))
classes.sort()

# Load trained model.
pipeline = load('./classifier.pickle')

# Interact with classifier.
print('Query the trained text classification model interactively (CTRL+C to exit):')
while True:
    result = pipeline.predict([input('input> ').strip()])
    print(classes[result[0]])
