import requests
import json

data = {"instances": "Muchas gracias!"}
json_response = requests.post('http://127.0.0.1:8051/predict', data=data)
result = json.loads(json_response.text)['predictions']
print(result)


'''
La predicción del bot está compuesta de los siguientes campos:

predictions: {
    label: ..., # tipo de respuesta (tag)
    score: ..., # Valor 0 a 1 que indica la precisión de esa respuesta
    messsage: ... # Mensaje del bot como respuesta (texto)
}
'''
