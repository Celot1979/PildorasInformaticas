from bs4 import BeautifulSoup
import requests

mi_doc = requests.get('https://www.directoalpaladar.com')
doc_final = BeautifulSoup(mi_doc.text, 'html.parser')
lis=[]



titulo=doc_final.select('.abstract-title')
print(titulo[1].text)
lista=[]
for t in doc_final.select_one('.abstract-title'):
    lista.append(t)

for t in lista:
    print(t)