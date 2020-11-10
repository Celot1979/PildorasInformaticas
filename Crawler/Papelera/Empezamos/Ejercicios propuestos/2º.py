from bs4 import BeautifulSoup
import requests
miDoc = requests.get('http://python.beispiel.programmierenlernen.io/index.php')
docFinal = BeautifulSoup(miDoc.text, 'html.parser')

""" #iconos=docFinal.select('.emoji')
texto=docFinal.select('.card-text')
#print(iconos[0].text)
print(texto[0].text)
Esto sería para seleccionar un único texto 
"""
for texto in docFinal.select(".card-text"):
    print(texto.text)
    print("")

""" Aquí sería para ver todos los textos de la web """
