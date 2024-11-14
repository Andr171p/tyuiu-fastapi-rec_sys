FROM python:3.11

WORKDIR /rec-sys-api

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-k uvicorn.workers.UvicornWorker", "-w 3", "main:app"]