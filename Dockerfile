# Gunakan image Python
FROM python:3.11.4-slim AS builder

# Buat folder app
RUN mkdir /app

# Set work directory di dalam container
WORKDIR /app

# Set environment variable untuk optimasi python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --upgrade pip 
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

 

# ===== Stage 2: Production stage
FROM python:3.11.4-slim

RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser /app

# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Set working directory
WORKDIR /app

# Cop aplikasi code

COPY --chown=appuser:appuser . .

# Set environment variable untuk optimasi python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Switch to non-root user
USER appuser


# Expose aplikasi port
EXPOSE 8000

# Start the application using Gunicorn
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "core.asgi:application"]
