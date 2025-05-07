FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "fastapi", "dev", "app/main.py", "--port", "8000", "--host", "0.0.0.0" ]