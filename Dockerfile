FROM python:3.6-slim

RUN adduser --system datapunt

COPY . /app/
RUN apt-get install make && \
    pip install --no-cache-dir /app

USER datapunt

