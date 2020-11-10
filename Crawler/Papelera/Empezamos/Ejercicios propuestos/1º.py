from bs4 import BeautifulSoup
import requests

miDoc = requests.get("http://python.beispiel.programmierenlernen.io/index.php")
docFinal = BeautifulSoup(miDoc.text, "html.parser")
iconos = docFinal.select(".emoji")
titulo = docFinal.select(".card-title span")
# print(titulo)
primer_titulo= titulo[1].text

print(primer_titulo)

