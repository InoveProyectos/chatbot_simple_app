![logotipo](imagenes/inove.jpg)
# Python ChatBot
### BOT de chats para aplicaciones web (Django / Flask)

Este es un proyecto realizado por miembros de inove como un servicio para incorporar en una aplicaci贸n del estilo e-ccomerce.

# Comenzando 馃殌
El objetivo de este proyecto es dar un ejemplo de aplicaci贸n de Python en la automatizaci贸n a respuesta de mensajer铆a de Chat. Este proyecto se basa en generar una lista de temas que se desea que el bot sepa responder ante la consulta de un posible cliente.

# Pre-requisitos 馃搵
Para poder ejecutar esta aplicaci贸n, ser谩 necesario tener instalada la versi贸n 3.7 de Python o superior.\
Para ejecutar la aplicaci贸n se debe contar con docker instalado para lanzar tensorflow y la librer铆a de NLP utilizada.

# Instalaci贸n y pruebas 馃敡鈿欙笍
Descargue el repositorio en su pc, luego lanzar el servicio de Docker con el siguiente comando:
```
docker build -t inove_chatbot .
docker run -d -p 8501:8501 -v $(pwd)/model:/opt/bot/model inove_chatbot
```
Or desde el docker-compose
```
docker-compose build
docker-compose up
```

Una vez levantado el container puede ensayar la API con el script "test.py"

# Autores 鉁掞笍
### Miembros de Inove (coding school)
:octocat: Hern谩n Contigiani 
:octocat: Hector Vergara

# Licencia 馃搫 :balance_scale:
Este proyecto est谩 bajo la Licencia de Inove (coding school) para libre descarga y uso. Este proyecto tiene un prop贸sito educativo y de muestra, por ello, no nos responsabilizaremos por su uso indebido. As铆 mismo, no existe garant铆a en su implementaci贸n debido a que se trata de una demostraci贸n de uso gratuito con prop贸sitos educativos. 
### :copyright: Inove (coding school) 2021.

