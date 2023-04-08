FROM python:3.11.0-alpine

WORKDIR /source

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /source