ARG PYTHON_VERSION=3.10.5
FROM python:${PYTHON_VERSION}-alpine as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /ecommerce

#ARG UID=10001

#RUN adduser \
#    --disabled-password \
#    --gecos "" \
#    --home "/nonexistent" \
#    --shell "/sbin/nologin" \
#    --no-create-home \
#    --uid "${UID}" \
#    appuser

COPY requirement.txt requirement.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN python -m pip install -r requirement.txt
RUN apk del .tmp-build-deps
#RUN chmod 777 /ecommerce/db.sqlite3

#USER appuser

COPY . /ecommerce/

EXPOSE 8000