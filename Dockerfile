FROM python:latest

RUN pip install "poetry==1.7.1"

RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-interaction --no-ansi --no-root

COPY . .

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

CMD ["python", "src/main.py"]