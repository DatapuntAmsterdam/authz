FROM amsterdam/docker_python:latest
MAINTAINER datapunt@amsterdam.nl

ENV PYTHONUNBUFFERED 1

RUN adduser --system datapunt

COPY . /app/
RUN pip install --no-cache-dir /app[cli]

USER datapunt

