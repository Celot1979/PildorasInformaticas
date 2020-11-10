from bs4 import BeautifulSoup
import requests
miDoc = requests.get('http://python.beispiel.programmierenlernen.io/index.php')
docFinal = BeautifulSoup(miDoc.text, 'html.parser')

for imagen in docFinal.select(".card-block img"):
    print(imagen.attrs["src"]) 

