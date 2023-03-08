# Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering

Repository for Artificial Intelligence And Open Science In Research Software Engineering subject

[![Documentation Status](https://readthedocs.org/projects/ai-open-science-research-software-engineering/badge/?version=latest)](https://ai-open-science-research-software-engineering.readthedocs.io/en/latest/?badge=latest)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

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

## Docker compose (Recomended aproach)

- All will be install and run via:

```bash
docker compose up -d --build
```

- After running he containers you can make sure the program was executed correctly using:

```bash
docker logs client
```

- **Note (clients is not consitent the firts few times is launch, please make sure to run it a few times with the followign command and see the logs produced afterwars, tends to work better using docker compose with the flasg --build)**

```bash
docker start client
```

## Server instalation for local use

```bash
docker pull lfoppiano/grobid:0.7.2
```

```bash
docker run --rm -p 8070:8070 -p 8081:8071 lfoppiano/grobid:0.7.2
```

## Client instalation (Local)

- Run clientInstallation.sh wich uses python venv to make a virtual env for the project

```bash
./clientInstalationVenv.sh
```

- tkinter is also need it for the word clouds

```bash
sudo apt install python3-tk
```

### What does the client instalation do

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

pip install -e .
```

## Running the program

- Make sure you have the client and the server properly installed

```bash
python3 __main__.py
```

## Running the test

- Make sure you have the client and the server properly installed

```bash
python3 test/test.py
