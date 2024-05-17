#!/bin/bash

# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

# Download NLTK data
python -m nltk.downloader punkt stopwords

echo "Setup is complete. To activate the virtual environment, run 'source env/bin/activate'"
