import requests
import os
import pandas as pd
from bs4 import BeautifulSoup

def web_crawler(url):
    try:
        # Realizar una solicitud GET a la página web
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Utilizar BeautifulSoup para analizar el contenido HTML de la página web
            soup = BeautifulSoup(response.content, 'html.parser')

            # Encontrar todos los enlaces en la página
            links = soup.find_all('a')

            # Filtrar los enlaces internos y evitar imprimirlos en la salida
            internal_links = []
            for link in links:
                href = link.get('href')
                if href is not None and href.startswith(url):
                    internal_links.append(href)

            # Encontrar todas las imágenes en la página
            images = soup.find_all('img')

            # Encontrar todos los encabezados en la página
            headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

            # Obtener el texto de la página y contar el número de palabras
            text = soup.get_text()
            word_count = len(text.split())

            # Obtener los metadatos de la página
            meta_tags = soup.find_all('meta')
            metadata = {}
            for tag in meta_tags:
                name = tag.get('name')
                content = tag.get('content')
                if name is not None and content is not None:
                    metadata[name] = content

            # Obtener el tamaño de la página
            size = len(response.content)

            # Crear un DataFrame de pandas con los datos de la página
            data = {'title': soup.title.text.strip(),
                    'internal_links': len(internal_links),
                    'images': len(images),
                    'headers': len(headers),
                    'word_count': word_count,
                    'metadata': metadata,
                    'size': size}
            df = pd.DataFrame(data, index=[url])

            path = r'C:\Users\despi\Downloads\images'

            # Crear el directorio si no existe
            if not os.path.exists(path):
                os.makedirs(path)
                
            # Imprimir el informe
            print(df)

            # Imprimir los metadatos de la página
            print("\nMetadatos de la página:")
            for name, content in metadata.items():
                print(f"- {name}: {content}")

             
            # Imprimir los enlaces encontrados en un formato legible
            print("\nEnlaces internos encontrados en la página:")
            for link in internal_links:
                print(f"- {link}")

            # Imprimir las imágenes encontradas en un formato legible
            print("\nImágenes encontradas en la página:")
            for img in images:
                src = img.get('src')
                alt = img.get('alt')
                print(f"- {alt}: {src}")

             # Descargar las imágenes y guardarlas en una carpeta llamada "images"
            for img in images:
                src = img.get('src')
                if src is not None and (src.endswith('.avg') or src.endswith('.jpg')):
                    img_url = url + src if src.startswith('/') else src
                    img_data = requests.get(img_url).content
                    filename = os.path.join(path, src.split('/')[-1])
                    with open(filename, 'wb') as handler:
                        handler.write(img_data)

    except requests.exceptions.RequestException as e:
        # Manejar excepciones y mostrar un mensaje de error
        print(f"Error al intentar acceder a la página: {e}")


# Llamar a la función web_crawler con la URL de la página que deseas explorar
web_crawler('https://www.chivasdecorazon.com.mx/es')
