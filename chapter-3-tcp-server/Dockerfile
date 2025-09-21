FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY tcp.server.py .

EXPOSE 9998

CMD ["python", "tcp.server.py"]
