#!/bin/bash

python3 -m venv AIOSRSE
source AIOSRSE/bin/activate
python3 -m pip install --upgrade pip
pip install -r requiremets.txt

git clone https://github.com/kermitt2/grobid_client_python
cd grobid_client_python
python3 setup.py install

cd ..