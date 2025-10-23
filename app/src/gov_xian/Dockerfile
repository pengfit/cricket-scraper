FROM python:3.11-slim

# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies required for Playwright and headless browsers
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    libx11-xcb1 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libxtst6 \
    libgtk-3-0 \
    xdg-utils \
    libatspi2.0-0 \
    libdrm2 \
    libdbus-glib-1-2 \
    libxshmfence1 \
    && rm -rf /var/lib/apt/lists/*

# Install Playwright and its browsers
RUN pip install playwright

RUN playwright install

# Copy shared utils and the script specific to this service
COPY ../shared /usr/src/app/shared

COPY playwright-test.py /usr/src/app/

# Set the command to run the Playwright script
CMD ["python", "playwright-test.py"]
