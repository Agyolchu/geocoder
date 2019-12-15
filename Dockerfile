FROM python:3.7-slim-buster

ADD /app/requirements.txt /app/requirements.txt

WORKDIR /app/

RUN apt-get update && apt-get install gcc libc-dev libgeos-dev

RUN pip install -r requirements.txt

RUN adduser --disabled-password --gecos '' app