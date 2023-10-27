FROM python:3.11-slim-bookworm as requirements-stage

RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock /
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --without=dev

FROM python:3.11-slim-bookworm

COPY --from=requirements-stage /requirements.txt /requirements.txt
COPY ./app /app

RUN python3 -m pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 8000

ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app.main:app"]
