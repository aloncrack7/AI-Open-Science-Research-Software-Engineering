# Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering

Repository for Artificial Intelligence And Open Science In Research Software Engineering subject

[![Documentation Status](https://readthedocs.org/projects/ai-open-science-research-software-engineering/badge/?version=latest)](https://ai-open-science-research-software-engineering.readthedocs.io/en/latest/?badge=latest)

## [Licence (CC0-1.0 license)](https://github.com/aloncrack7/Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering/blob/main/LICENCE.md)

[![License: CC0-1.0](https://licensebuttons.net/l/zero/1.0/80x15.png)](http://creativecommons.org/publicdomain/zero/1.0/)

## Citation

### APA

```text
García Velasco, A. Artificial Intelligence And Open Science In Research Software Engineering [Computer software]. https://github.com/aloncrack7/AI-Open-Science-Research-Software-Engineering
```

### BibTex

```text
@software{Garcia_Velasco_Artificial_Intelligence_And,
author = {García Velasco, Alonso},
license = {CC0-1.0},
title = {{Artificial Intelligence And Open Science In Research Software Engineering}},
url = {https://github.com/aloncrack7/AI-Open-Science-Research-Software-Engineering}
}
```

## Server instalation

```bash
docker pull lfoppiano/grobid:0.7.2
```

```bash
docker run --rm -p 8070:8070 -p 8081:8071 lfoppiano/grobid:0.7.2
```

## Client instalation

- Run clientInstallation.sh wich uses python venv to make a virtual env for the project

```bash
./clientInstalationVenv.sh
```

- tkinter is also need it for the word clouds

```bash
sudo apt install python3-tk
```

### What does the clien instalation do

- It creates a virtual enviroment, activates, downloads the latest version of pip and proceeds to install al requirements. After that clones the grobid client form the repository an installs it.

```bash
python3 -m venv AIOSRSE
source AIOSRSE/bin/activate
python3 -m pip install --upgrade pip
pip install -r requiremets.txt

git clone https://github.com/kermitt2/grobid_client_python
cd grobid_client_python
python3 setup.py install

cd ..
```

## Running the program

- Make sure you have the client and the server properly installed

```bash
python3 __main__.py
```
