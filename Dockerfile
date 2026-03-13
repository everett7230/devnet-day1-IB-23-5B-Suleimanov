FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir --progress-bar off -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]
