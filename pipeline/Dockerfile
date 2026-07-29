FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml uv.lock ./
RUN uv sync --locked

COPY ingest_tables.py ingest_zone.py ingest_taxi_data.py ./

ENTRYPOINT ["python", "ingest_tables.py"]



