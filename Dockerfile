# imagen base
FROM python:latest


# install requirements
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy archivos 
COPY app.py /usr/src/app/
COPY templates/newcomment2.html /usr/src/app/templates/

# puerto
EXPOSE 5000

# correr el app
CMD ["python", "/usr/src/app/app.py"]
