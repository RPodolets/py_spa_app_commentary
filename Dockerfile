FROM python:3.11-alpine
LABEL maintainer="dev.roman.podolets@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

USER django-user
