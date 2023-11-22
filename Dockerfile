ARG PYTHON_VERSION=3.10.5
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /ecommerce

ARG UID=10001

#RUN adduser \
#    --disabled-password \
#    --gecos "" \
#    --home "/nonexistent" \
#    --shell "/sbin/nologin" \
#    --no-create-home \
#    --uid "${UID}" \
#    appuser

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirement.txt,target=requirement.txt \
    python -m pip install -r requirement.txt
#RUN chmod 777 /ecommerce/db.sqlite3

#USER appuser

COPY . /ecommerce/

EXPOSE 8000