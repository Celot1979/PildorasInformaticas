from bs4 import BeautifulSoup
import requests
miDoc = requests.get('http://python.beispiel.programmierenlernen.io/index.php')
docFinal = BeautifulSoup(miDoc.text, 'html.parser')

titulo = docFinal.select('./img/1.jpg')
print(titulo)