FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install --no-cache-dir sqlfluff

COPY ./app /app
