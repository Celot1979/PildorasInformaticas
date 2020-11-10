from bs4 import BeautifulSoup
import requests
miDoc = requests.get('http://python.beispiel.programmierenlernen.io/index.php')
docFinal = BeautifulSoup(miDoc.text, 'html.parser')

for c in docFinal.select(".card-text"):
    print(c.text)
    print("")