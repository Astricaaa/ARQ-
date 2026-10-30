FROM python:3.12-slim

WORKDIR /app

COPY ["Pagina Web/requirements.txt", "./requirements.txt"]
RUN pip install --no-cache-dir -r requirements.txt

COPY ["Pagina Web/app", "./app"]
COPY ["assets", "./assets"]
COPY ["Pitch Inglés.mp4", "./Pitch Inglés.mp4"]

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
