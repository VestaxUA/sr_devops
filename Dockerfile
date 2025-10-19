FROM python:3.11-slim

WORKDIR /app

COPY . .

CMD ["python", "sr1/main.py"]