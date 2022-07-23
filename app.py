'''
API BOT Machine Learning
---------------------------
Descripcion:
Se utiliza Flask para crear un WebServer que levanta un
modelo de inteligencia artificial con machine learning
y realizar predicciones o clasificaciones
Ejecución: Lanzar el programa y abrir en un navegador la siguiente dirección URL
http://127.0.0.1:5000/

'''
import json
import string
import random 
import numpy as np
import pickle
import requests
import re
import unicodedata
import traceback

import numpy as np
from flask import Flask, request, Response, jsonify
import tensorflow as tf

# Flask
app = Flask(__name__)

# Cargar el vocabulario de palabras y las clases del modelo
words = pickle.load(open('model/words.pkl','rb'))
classes = pickle.load(open('model/classes.pkl','rb'))

# Load dataset
dataset = json.load(open('model/dataset.json'))

# Load Model
model = tf.keras.models.load_model("model/bot.h5")

# Cargar el diccionario
import stanza
import spacy_stanza
nlp = spacy_stanza.load_pipeline("es")

# ---------------------------------------------------------------
#
# Preprocesamiento de texto (datos de entrada)
#
# ---------------------------------------------------------------
def preprocess_clean_text(text):
    ''' Preprocesamiento de texto'''
    # Quitar los tildes
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    # Quitar caracteres especiales
    pattern = r'[^a-zA-z0-9.,!?/:;\"\'\s]' 
    text = re.sub(pattern, '', text)
    pattern = r'[^a-zA-z.,!?/:;\"\'\s]' 
    # Quitar números
    text = re.sub(pattern, '', text)
    # Quitar signos de puntuación
    text = ''.join([c for c in text if c not in string.punctuation])
    return text

def text_to_tokens(text):
    ''' Llevar las palabras a su "base" (lematizacion) '''
    lemma_tokens = []
    tokens = nlp(preprocess_clean_text(text.lower()))
    for token in tokens:
        lemma_tokens.append(token.lemma_)

    return lemma_tokens


def bag_of_words(text, vocab):
    ''' Transformar las palabras en oneHotEncoding '''
    tokens = text_to_tokens(text)
    bow = [0] * len(vocab)
    for w in tokens: 
        for idx, word in enumerate(vocab):
            if word == w: 
                bow[idx] = 1

    return np.array(bow)


def pred_class(text, vocab, labels):
    ''' Predecir el resultado, inferencia del modelo '''
    bow = bag_of_words(text, vocab)
    words_recognized = sum(bow)

    return_list = []
    if words_recognized > 0:
        result = model.predict(np.array([bow]))[0]
        thresh = 0.2
        y_pred = [[idx, res] for idx, res in enumerate(result) if res > thresh]
        y_pred.sort(key=lambda x: x[1], reverse=True)

        # Obtener la primera mejor respuesta
        r = y_pred[0] 
        return_list.append({"tag": labels[r[0]], "score": r[1]})    

    return return_list


def get_response(tag, intents_json):
    ''' Transformar la inferencia del modelo (tag)
        en una respueta (texto)'''
    for intent in intents_json["intents"]: 
        if intent["tag"] == tag:
            result = random.choice(intent["responses"])
            break
    return result

# ---------------------------------------------------------------
#
# Preprocesamiento de texto (datos de entrada)
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

            # Realizar la predicción del modelo
            intents = pred_class(message, words, classes)

            if len(intents) > 0:
                # Transformar la predicción en una respuesta
                # Solo tomar como válida la primera mejor respuesta
                intent = intents[0]
                result = get_response(intent["tag"], dataset)
                json_data = {"predictions": [result]}
            else:
                json_data = {"predictions": ["Perdón, no pude entenderte"]}
            
            return jsonify(json_data)
        
    except Exception as e:
        print(e)
        return Response(status=400)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8501, debug=True)