FROM python:3.10-alpine AS base

RUN pip3 install pipenv

COPY Pipfile Pipfile.lock ./

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base AS test

COPY --from=base /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

WORKDIR /app
COPY src/ ./src/
COPY tests/ ./tests/

ENTRYPOINT [ "pytest" , "--cov-fail-under=70", "--cov=src", "tests/" ]

FROM base AS runtime

COPY --from=base /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

WORKDIR /app
COPY src/ ./src/

EXPOSE 3001
ENTRYPOINT [ "uvicorn", "src.main:app" ]
CMD [ "--host", "0.0.0.0", "--port", "3000" ]
