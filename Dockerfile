FROM mcr.microsoft.com/playwright/python:latest

WORKDIR /app

# Copy requirements first
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Optional: ensure playwright browsers are installed
RUN playwright install --with-deps

# Allow GOV_MODULE to be set dynamically at runtime
ENV GOV_MODULE=""

# Default command
CMD ["bash", "run_test.sh"]
