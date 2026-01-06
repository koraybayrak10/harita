FROM python:3.11-slim

# Ortam değişkenleri
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Sistem bağımlılıkları (gerekirse)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
  && rm -rf /var/lib/apt/lists/*

# Python bağımlılıkları
COPY services/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Projeyi kopyala
COPY services /app/services
COPY frontend /app/frontend

# Port
EXPOSE 8000

# FastAPI başlat
CMD ["uvicorn", "services.main:app", "--host", "0.0.0.0", "--port", "8000"]
