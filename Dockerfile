FROM python:latest

WORKDIR /app

ENV FLASK_APP app.py

ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt .

RUN pip3 install -r requirements.txt

CMD ["python", "app.py"]
