# Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering

Repository for Artificial Intelligence And Open Science In Research Software Engineering subject

## [Licence](https://github.com/aloncrack7/Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering/blob/main/LICENCE.md)

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
