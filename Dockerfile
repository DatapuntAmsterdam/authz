FROM amsterdam/python
MAINTAINER datapunt@amsterdam.nl

ENV PYTHONUNBUFFERED 1

RUN adduser --system datapunt

COPY . /app/
RUN pip install --no-cache-dir /app

USER datapunt

