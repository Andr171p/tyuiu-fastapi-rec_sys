FROM python:3.11

WORKDIR /rec-sys-api

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-w", "3", "--bind", ":8000", "main:app"]