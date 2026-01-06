FROM python:3.11-slim

WORKDIR /app

RUN pip install fastapi uvicorn

COPY services /app/services
COPY frontend /app/frontend

EXPOSE 8000

CMD ["uvicorn", "services.main:app", "--host", "0.0.0.0", "--port", "8000"]
