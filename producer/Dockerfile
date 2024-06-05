# Dockerfile for kafka Producer
FROM python:3.11 

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY producer.py producer.py

CMD ["python","producer.py"]