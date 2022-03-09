FROM python:latest

WORKDIR /app

ENV FLASK_APP app.py

ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY app.py /usr/src/app/
COPY templates/newcomment2.html /usr/src/app/templates/


EXPOSE 5001

CMD ["python", "/usr/src/app/app.py"]
