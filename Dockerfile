FROM ghcr.io/astral-sh/uv:python3.11-bookworm

WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies (no dev)
RUN uv sync --no-dev --no-install-project

# Copy application code
COPY app/ app/
COPY payment_service.py ./

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH=/app
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
