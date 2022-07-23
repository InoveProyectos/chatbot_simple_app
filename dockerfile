FROM tensorflow/tensorflow:2.5.1

RUN  apt-get update \
    && apt-get install wget -y \
    && apt-get install zip -y

# Descargar el diccionario en español de Stanza
RUN wget https://raw.githubusercontent.com/stanfordnlp/stanza-resources/main/resources_1.2.2.json -P /root/stanza_resources
RUN wget http://nlp.stanford.edu/software/stanza/1.2.2/es/default.zip -P /root/stanza_resources/es
RUN unzip /root/stanza_resources/es/default.zip -d /root/stanza_resources/es/
RUN rm /root/stanza_resources/es/default.zip
RUN mv /root/stanza_resources/resources_1.2.2.json /root/stanza_resources/resources.json

RUN apt-get clean

COPY requirements.txt .
RUN python -m pip install -r requirements.txt
# Flask es necesario instalarlo con python3
RUN python3 -m pip install flask

WORKDIR /opt/bot

COPY app.py .

CMD python3 ./app.py