FROM python:3.11-buster as builder

ARG POETRY_VERSION=1.7.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=${POETRY_VERSION} \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off

RUN apt-get update \
&& apt-get autoremove \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* \
&& pip install poetry==$POETRY_VERSION

# Add poetry to path
ENV PATH "/root/.local/bin:${PATH}"

COPY poetry.lock pyproject.toml /
RUN     poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR \
        && poetry export --without dev --without-hashes -f requirements.txt -o requirements.txt\
        && python -m venv /app/.venv \
        && /app/.venv/bin/python -m pip install -r requirements.txt \
        && /app/.venv/bin/python -m pip freeze --all


# first dot tells docker to copy all the files and subdirectorties
# from this Dockerfile to a directory in the containers file system. In this case we name this directory "app"
COPY  . /app

# Production Stage.
# We use the NUnit python 3.11 image as base so we can run the FastAPI app behind NUnit
FROM unit:python3.11 as production

#The application directory and the virtual environment from the build stage are copied into production stage 
COPY --from=builder /app /app
RUN cp /app/nginx_unit_config.json /docker-entrypoint.d/config.json

WORKDIR /app

EXPOSE 80
