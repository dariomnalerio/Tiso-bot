FROM python:3.11.2-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk update && \
    apk add --no-cache gcc musl-dev && \
    apk add --no-cache libpq && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev

# Copy only the necessary files and folders
COPY commands/ ./commands/
COPY api/ ./api/
COPY database/ ./database/
COPY models/ ./models/
COPY services/ ./services/
COPY tests/ ./tests/
COPY main.py .
COPY create_tables.py .
COPY requirements.txt .
COPY .env .



ENV DOTENV_PATH=/app/.env
