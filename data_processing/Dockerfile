# syntax=docker/dockerfile:1

FROM python:3.12-slim

# Avoids Python buffering stdout/stderr (better logs)
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install build deps only if needed by some pip packages
# (you can remove these if not required)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

# Copy dependency files first for better Docker layer caching
# If you have requirements.txt, this will work:
COPY data_processing/requirements*.txt /app/ 2>/dev/null || true

# Install deps (adjust if you use poetry/pdm)
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Copy application code
COPY data_processing/ /app/

# Set a default command:
# CHANGE THIS to whatever starts your job/service.
# Examples:
# CMD ["python", "-m", "data_processing"]
# CMD ["python", "main.py"]
CMD ["python", "main.py"]
