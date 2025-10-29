FROM mcr.microsoft.com/playwright/python:latest

WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application
COPY . .

# Set environment variable dynamically via Compose
ENV GOV_MODULE=${GOV_MODULE}

CMD ["bash", "run_test.sh"]