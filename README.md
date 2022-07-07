# Bert Celery Triton

###### created by Weber Huang 

## Description

This repo is a template of building a text classification training task using Pytorch, Transformer BERT, celery worker and deploying with TIS (Triton Inference Sever).

Noted that this repo doesn't contain client code, you can refer to [triton-inference-server client docs](https://github.com/triton-inference-server/client) to setup your client machine or using celery cluster to develop inference client, in this way you have to bind the same massage broker.

## Usage

+ Clone the repo

```bash
$ git clone <this repo>

$ cd <this repo>
```

+ create a `.env` file with

```bash
# set LEVEL to info if you dont wanna log with verbose mode
# change the redis localhost to your ip
LEVEL=debug
REDIS=redis://localhost:6379/0
```

+ run service, this will setup
  + celery_server: for model training and validation
  + redis: message broker and backend for celery_worker
  + triton server: for inference usage, model deployment 

```bash
$ docker-compose -f docker/docker-compose.yml --env-file .env up
```

