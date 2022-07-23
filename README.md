![logotipo](imagenes/inove.jpg)
# Python ChatBot
### BOT de chats para aplicaciones web (Django / Flask)

Este es un proyecto realizado por miembros de inove como un servicio para incorporar en una aplicación del estilo e-ccomerce.

# Comenzando 🚀
El objetivo de este proyecto es dar un ejemplo de aplicación de Python en la automatización a respuesta de mensajería de Chat. Este proyecto se basa en generar una lista de temas que se desea que el bot sepa responder ante la consulta de un posible cliente.

# Pre-requisitos 📋
Para poder ejecutar esta aplicación, será necesario tener instalada la versión 3.7 de Python o superior.\
Para ejecutar la aplicación se debe contar con docker instalado para lanzar tensorflow y la librería de NLP utilizada.

# Instalación y pruebas 🔧⚙️
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

# Autores ✒️
### Miembros de Inove (coding school)
:octocat: Hernán Contigiani 
:octocat: Hector Vergara

# Licencia 📄 :balance_scale:
Este proyecto está bajo la Licencia de Inove (coding school) para libre descarga y uso. Este proyecto tiene un propósito educativo y de muestra, por ello, no nos responsabilizaremos por su uso indebido. Así mismo, no existe garantía en su implementación debido a que se trata de una demostración de uso gratuito con propósitos educativos. 
### :copyright: Inove (coding school) 2021.

