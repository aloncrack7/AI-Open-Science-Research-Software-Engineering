FROM ubuntu:22.04

RUN apt update
RUN apt install -y python3.10
RUN apt install -y python3-pip
RUN apt install -y python3.10-venv
RUN apt install -y git

SHELL ["/bin/bash", "-c"]

ENV ENV_PREFIX=AIOSRSE

RUN mkdir -p /home/root/project
WORKDIR /home/root/project
COPY . /home/root/project

RUN python3 -m venv ${ENV_PREFIX} && \
    source ${ENV_PREFIX}/bin/activate && \
    python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt && \
    git clone https://github.com/kermitt2/grobid_client_python && \
    cd grobid_client_python && \
    python3 setup.py install && \
    cd ..

# COPY entrypoint.sh /home/root/
# ENTRYPOINT ["/home/root/entrypoint.sh"]
