FROM amsterdam/docker_python:latest
MAINTAINER datapunt.ois@amsterdam.nl

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && adduser --system datapunt

COPY . /app/
RUN pip install --no-cache-dir /app[cli]

USER datapunt

ENTRYPOINT ["authz"]
CMD ["--help"]

