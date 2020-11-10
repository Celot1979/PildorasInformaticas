from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
class PostCraeled():
    def __init__(self, titulo, emoticono, contenido, imagen):
        self.titulo = titulo
        self.emoticono = emoticono
        self.contenido = contenido
        self.imagen = imagen
        
class PostExtractor():
    def extraeInfo(self):
        url_base = 'http://python.beispiel.programmierenlernen.io/index.php'
        miDoc = requests.get(url_base)
        docFinal = BeautifulSoup(miDoc.text, 'html.parser')
        post=[]
        for card in docFinal.select(".card"):
            titulo=card.select(".card-title span")[1].text 
            emoticono=card.select_one(".emoji").text 
            contenido=card.select_one(".card-text").text 
            imagen=urljoin(url_base,card.select_one("img").attrs["src"])

            crawled=PostCraeled(titulo,emoticono,contenido,imagen)
            post.append(crawled)
        return post

UnPost=PostExtractor()
listaPost=UnPost.extraeInfo()

#print(listaPost)

for post in listaPost:
    print(post.titulo)
    print(post.emoticono)
    print(post.contenido)
    print(post.imagen)


