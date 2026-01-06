FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# deps
COPY services/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# code
COPY services /app/services
COPY frontend /app/frontend

EXPOSE 8000

CMD ["uvicorn", "services.main:app", "--host", "0.0.0.0", "--port", "8000"]
