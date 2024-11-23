# Stage 1: Build Stage
FROM python:3.12-slim AS builder

# Set working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final Stage
FROM ubuntu:24.04

# Set environment variables to prevent interactive prompts during build
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies to run Flask app (python, pip, etc.)
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean

# Copy only the necessary files from the builder stage
COPY --from=builder /app /app

# Set working directory in the final image
WORKDIR /app

# Expose the port the app will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "server.py"]
