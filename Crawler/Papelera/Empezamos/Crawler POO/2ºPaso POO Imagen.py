from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin 
""" Para conseguir que el enlace a la imagenes tenga una ruta absoluta se crea una variable
y  luego se modifica una sentencia. Se aplicará 1 en los sitios que se ha modificado """

class PostCrawled():
    def __init__(self, titulo, emoticono, contenido, imagen):
        self.titulo = titulo
        self.emoticono = emoticono
        self.contenido = contenido
        self.imagen = imagen


class PostExtractor():
    def extraeInfo(self):
        urlBase='http://python.beispiel.programmierenlernen.io/index.php'
        miDoc = requests.get(urlBase)#1
        docFinal = BeautifulSoup(miDoc.text, 'html.parser')
        post = []#Se almacena los objetos creados de la clase PostCrawled
        for card in docFinal.select(".card"):
            titulo=card.select(".card-title span")[1].text 
            emoticono=card.select_one(".emoji").text 
            contenido=card.select_one(".card-text").text 
            imagen=urljoin(urlBase, card.select_one("img").attrs["src"])
            crawler = PostCrawled(titulo, emoticono, contenido, imagen)#1
            post.append(crawler)

        return post

unPost = PostExtractor()
listaPost = unPost.extraeInfo()
# print(listaPost)

for elPost in listaPost:
    print(elPost.emoticono)
    print(elPost.titulo)
    print(elPost.contenido)
    print (elPost.imagen)
    print("")


