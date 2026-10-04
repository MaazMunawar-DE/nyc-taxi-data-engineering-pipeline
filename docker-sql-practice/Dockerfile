# Base image: lightweight Linux environment with Python
FROM python:3.14-slim

# Copy uv binary from the official uv image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set the working directory inside the container
WORKDIR /code

# Add the virtual environment binaries to PATH
ENV PATH="/code/.venv/bin:$PATH"

# Copy dependency files first for better Docker layer caching
COPY pyproject.toml uv.lock ./

# Create the virtual environment and install locked dependencies
RUN uv sync --locked --no-install-project

# Copy the ingestion script into the working directory
COPY ingest_data.py .

# Run the ingestion script when the container starts
ENTRYPOINT ["python", "ingest_data.py"]