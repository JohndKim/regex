# python version for base image
FROM python:3.12-slim

# env variable to prevent buffering from stdout
ENV PYTHONUNBUFFERED=1

# names the working directory in docker to put everything
WORKDIR /backend

# install libraries
COPY requirements.txt .

RUN pip install -r requirements.txt

# copy all files over
COPY . .

# opens this port to requests
EXPOSE 8000