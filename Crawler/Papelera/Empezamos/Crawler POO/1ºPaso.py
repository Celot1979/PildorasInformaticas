from bs4 import BeautifulSoup
import requests

class PostCrawled():
    def __init__(self, titulo, emoticono, contenido, imagen):
        self.titulo = titulo
        self.emoticono = emoticono
        self.contenido = contenido
        self.imagen = imagen


class PostExtractor():
    def extraeInfo(self):
        miDoc = requests.get('http://python.beispiel.programmierenlernen.io/index.php')
        docFinal = BeautifulSoup(miDoc.text, 'html.parser')
        post = []#Se almacena los objetos creados de la clase PostCrawled
        for card in docFinal.select(".card"):
            titulo=card.select(".card-title span")[1].text 
            emoticono=card.select_one(".emoji").text 
            contenido=card.select_one(".card-text").text 
            imagen=card.select_one("img").attrs["src"]
            crawler = PostCrawled(titulo, emoticono, contenido, imagen)
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


