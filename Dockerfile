FROM python:3.10-slim
RUN apt-get update && apt-get install -y \ 
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY .env .
# CMD [ "flask", "run", "--host=0.0.0.0" ]
CMD ["python", "main.py"]
