FROM ubuntu:latest
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt update && apt install -y python3-dev wget

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir root/.conda \
    && sh Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

COPY . /mle-training
RUN /bin/bash -c "cd mle-training \
    && conda env create \
    --name mle-training \
    -f env.yml \ 
    && source activate mle-training \ 
    && python3 -m pip install --user -U virtualenv \ 
    && python3 -m virtualenv my_env \
    && source my_env/bin/activate \ 
    && pip install -r requirements.txt"
