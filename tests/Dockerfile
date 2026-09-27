FROM python:3.11-slim

WORKDIR /tests

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    pytest \
    pytest-html \
    pytest-json-report \
    requests \
    selenium \
    webdriver-manager

# Create reports directory
RUN mkdir -p /reports

CMD ["sleep", "infinity"]