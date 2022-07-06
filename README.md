# Bert Celery Triton

###### created by Weber Huang

## Description

This repo is a template of building a text classification training task using Pytorch, Transformer BERT and deploying with TIS (Triton Inference Sever).

## Usage

```bash
$ git clone <this repo>

$ cd <this repo>

$ touch .env

$ vim .env

# set LEVEL to info if you dont wanna run in verbose mode
LEVEL=debug
REDIS=redis://localhost:6379/0

$ docker build -t ychuang/bert_celery_worker --no-cache .

$ docker run --name bert_celery_worker_1 --env-file .env ychuang/bert_celery_worker
```

