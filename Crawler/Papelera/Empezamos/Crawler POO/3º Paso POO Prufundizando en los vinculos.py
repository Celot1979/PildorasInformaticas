from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin 
import time 
""" En este capitulo vamos a ir profundizando en los niveles de la información se señala con un 3"""

class PostCrawled():
    def __init__(self, titulo, emoticono, contenido, imagen):
        self.titulo = titulo
        self.emoticono = emoticono
        self.contenido = contenido
        self.imagen = imagen


class PostExtractor():
    def extraeInfo(self):
        urlBase='http://python.beispiel.programmierenlernen.io/index.php'
        post = []
        """ Vamos a crear un bucle while para que vaya profundizando en las páginas
        hasta llegar a la sexta. """
        # 3 Mientras encuentres una dirección sigue, si no para
        while urlBase!="":
            miDoc = requests.get(urlBase)
            docFinal = BeautifulSoup(miDoc.text, 'html.parser')
            time.sleep(2)#3
            for card in docFinal.select(".card"):
                titulo=card.select(".card-title span")[1].text
                emoticono=card.select_one(".emoji").text 
                contenido=card.select_one(".card-text").text 
                imagen=urljoin(urlBase, card.select_one("img").attrs["src"])
                crawler = PostCrawled(titulo, emoticono, contenido, imagen)
                post.append(crawler)

            boton_siguiente=docFinal.select_one(".navigation .btn")# Botón de la página 3
            if boton_siguiente:
                rutas_absolutas = urljoin(urlBase, boton_siguiente.attrs["href"])
                urlBase = rutas_absolutas
                print(rutas_absolutas)
            else:
                urlBase = ""
            #Parte de la ruta de la 2ª pagina
            #Si ponemos el atributo urljoin(tendremos la ruta obsoluta)
            

             #3
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


