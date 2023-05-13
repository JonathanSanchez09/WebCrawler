# 
Este código es un programa en Python que realiza un rastreo web básico (también conocido como "web crawler") en una página web proporcionada como argumento a una función llamada web_crawler(). La función utiliza la biblioteca requests para realizar una solicitud GET a la página web, y luego utiliza BeautifulSoup para analizar el contenido HTML de la págin

Después de analizar la página, la función recopila información relevante, como los enlaces internos, imágenes, encabezados, contenido de texto, metadatos y tamaño de la página. Luego, la función utiliza la biblioteca pandas para crear un DataFrame con esta información y lo imprime en la consola.

Además de la información recopilada, la función también descarga las imágenes de la página y las guarda en una carpeta llamada "images", que se crea si aún no existe. Finalmente, la función muestra en la consola los enlaces internos y las imágenes encontradas en la página, así como los metadatos de la página.

Para usar esta función, se puede llamar a web_crawler() con la URL de la página que se desea explorar. En este ejemplo, la página web https://www.chivasdecorazon.com.mx/es se proporciona como argumento a la función.
