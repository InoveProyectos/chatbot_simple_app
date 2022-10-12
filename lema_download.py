import os
import zipfile
import gdown

url = 'https://drive.google.com/uc?id=16leuM9PuFXAkmw34XeQy-84h8WGAYxJw&export=download'
output = 'lematizacion-es.zip'
gdown.download(url, output, quiet=False)

with zipfile.ZipFile(output, 'r') as zip_ref:
    zip_ref.extractall()