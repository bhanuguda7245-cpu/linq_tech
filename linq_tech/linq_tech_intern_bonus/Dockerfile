# Dockerfile for Python app
FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install pymongo pandas matplotlib

CMD ["tail", "-f", "/dev/null"]
