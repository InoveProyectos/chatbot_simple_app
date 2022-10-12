'''
API BOT Machine Learning
---------------------------
Descripcion:
Se utiliza Flask para crear un WebServer que levanta un
modelo de inteligencia artificial con machine learning
y realizar predicciones.
'''
import json
import string
import random 
import pickle
import requests
import re

from flask import Flask, request, Response, jsonify
import tensorflow as tf

# Flask
app = Flask(__name__)

# Cargar la tabla de lametizacion
with open("lematizacion-es.pickle",'rb') as fi:
    lemma_lookupTable = pickle.load(fi)

# Cargar el vocabulario de palabras y las clases del modelo
vocab = pickle.load(open('model/vocab.pkl','rb'))
responses = pickle.load(open('model/responses.pkl','rb'))

# Load Model
model = tf.keras.models.load_model("model/bot.h5")

# ---------------------------------------------------------------
#
# Preprocesamiento de texto (datos de entrada)
#
# ---------------------------------------------------------------
def preprocess_clean_text(text):
    # pasar a minúsculas
    text = text.lower()
    # quitar números
    pattern = r'[0-9\n]'
    text = re.sub(pattern, '', text)
    # quitar caracteres de puntiación
    text = ''.join([c for c in text if c not in (string.punctuation+"¡"+"¿")])
    # quitar caracteres con acento
    text = re.sub(r'[àáâä]', "a", text)
    text = re.sub(r'[éèêë]', "e", text)
    text = re.sub(r'[íìîï]', "i", text)
    text = re.sub(r'[òóôö]', "o", text)
    text = re.sub(r'[úùûü]', "u", text)
    return text

# ---------------------------------------------------------------
#
# Endpoint (API)
#
# ---------------------------------------------------------------
@app.route('/v1/models/chatbot:predict',methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            # Leer el mensaje a responder (la pregunta)
            instances_form = request.form.get('instances')
            if instances_form is None and request.json is None:
                return Response(status=400)

            message = ""
            if instances_form is not None:
                message = instances_form

            if request.json is not None:
                message = request.json['instances'][0][0]

            # preprocesamiento + lematizacion
            # ------------------------------------------
            # Transformar la pregunta (input) en tokens y lematizar
            lemma_words = []
            tokens = preprocess_clean_text(message).split(" ")
            for token in tokens:
                lemma = lemma_lookupTable.get(token)
                if lemma is not None:
                    lemma_words.append(lemma)

            # Transformar los tokens en "Bag of words" (arrays de 1 y 0)
            bow = []
            for word in vocab:
                bow.append(1) if word in lemma_words else bow.append(0)
            # ------------------------------------------

            probs = model.predict([bow])
            score = probs.max()
            if score > 0.4:  # threshold 0.4        
                index = probs.argmax(axis=1)[0]
                result = random.choice(responses[index])
                json_data = {"predictions": [result]}
            else:
                json_data = {"predictions": ["Perdón, no pude entenderte"]}

            return jsonify(json_data)
        
    except Exception as e:
        print(e)
        return Response(status=400)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8501, debug=True)