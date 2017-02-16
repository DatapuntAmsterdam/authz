FROM amsterdam/docker_python:latest
MAINTAINER datapunt.ois@amsterdam.nl

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN apt-get update \
    && adduser --system datapunt

COPY . /app/
RUN pip install --no-cache-dir /app[cli]

USER datapunt
