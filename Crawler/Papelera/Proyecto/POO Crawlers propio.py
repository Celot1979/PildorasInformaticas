from bs4 import BeautifulSoup
import requests
from requests.api import post
# El 1 es los primeros pasos
# El 2 el segundo paso
from urllib.parse import urljoin # Importamos la libreria para tener urls completas
class Poster():
    def __init__(self, titulo, texto, emoticono, imagen):
        self.titulo = titulo
        self.texto = texto 
        self.emoticono = emoticono 
        self.imagen = imagen

class Encontrar():
    def extraer(self):
        """ 2. Vamos a crear una nueva variable que guarde la dirección web ( así tenemos 
        asi tenemos la url base ) """
        url_base = 'http://python.beispiel.programmierenlernen.io/index.php'
        miDoc = requests.get(url_base)

        """ 2. Se cambia la variable miDoc introducciendo la nueva variable """
        docFinal = BeautifulSoup(miDoc.text, 'html.parser')
        """ 1.Con estás dos declaraciones, pedimos al servidor la vulta de la información
        de la web. En la variable docfinal incluimos esa información en formato texto,
        para que pueda ser tratado """
        lista=[] 
        # 1 Se crea una lista donde se almacenarán los datos del objeto crawerler
        for card in docFinal.select(".card"):
             titulo = card.select(".card-title span")[1].text
             emoticono = card.select_one(".emoji").text 
             texto = card.select_one(".card-text").text
             imagen =urljoin(url_base, card.select_one("img").attrs["src"])

             crawler = Poster(titulo, texto, emoticono, imagen)
             lista.append(crawler)
        return lista
        """ 1. En el bucle for hemos ido precisando la información que buscamos en la web.
        En la primera clase la hemos contruido 4 atributos que nos interesa guardar.
        Para guardar sólola información que nos interesa creamos la lista y vamos 
        agregando la información. Por último, cramos un objeto con la clase Poster y
         la almacenamos """
UnPoster = Encontrar()
ListaPost =UnPoster.extraer()
# print(ListaPost) Si realizamos una impresión por consola nos mostraria todos los objetos
# creados en la lista


""" 1. Ahora vamos a crear un bucle (for) para que la información guardada como objeto sea
legible y almacenable. """

for post in ListaPost:
    print(post.titulo)
    print(post.texto)
    print(post.emoticono)
    print(post.imagen)

         







