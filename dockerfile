FROM tensorflow/tensorflow:2.5.1

RUN  apt-get update \
    && apt-get install wget -y \
    && apt-get install zip -y


ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR /opt/bot

# Descargar el diccionario de lematizacion en español (lookuptable)
COPY lema_download.py .
RUN python3 lema_download.py

COPY app.py .

CMD python3 ./app.py