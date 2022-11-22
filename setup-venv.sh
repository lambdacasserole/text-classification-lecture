#!/bin/bash

# Delete any existing virtual environment.
if [ -d "./venv" ]; then
	rm -rf venv
fi

# Provision fresh venv and enter it.
python3 -m venv venv
. venv/bin/activate

# Upgrade pip, install dependencies and exit venv.
pip install --upgrade pip # Upgrade pip first.
pip install -r requirements.txt
deactivate
