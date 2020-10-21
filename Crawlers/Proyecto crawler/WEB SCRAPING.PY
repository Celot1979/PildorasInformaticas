#1º Usaremos 3 librerias
#--- Beatiful Soup
#--- Pandas
#--- Request
from bs4 import BeautifulSoup
import requests


# 2º Vamos a bajar el HTML de la página web. Usaremos el modulo request

url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'

# 3º El siguiente paso, una vez que tenemos una variante que tenga
#la dirección web es bajar el HTML

page = requests.get(url)

# 4º USaremos Beatiful Soup para poder identificar diferentes elementos de HTML
# y poder buscar por elementos.

soup = BeautifulSoup(page.content, 'html.parser')


# Ahora vamos a extraer parte de la información que deseamos:
#Equipos

eq = soup.find_all('span', class_='nombre-equipo')

# 5º Todo el contenido antes descargado de la etiqueta span, lo vamos a
# agregar a una lista.

equipos = list()

# Con una iteración de un bucle for iremos sacando elemento por elemento 
# Pero solamente la parte de texto que nos interesa.
count=0
for i in eq:
    if count < 20:#Aquí es donde limitamos la búsqueda de elementos
        equipos.append(i.text)
    else:
        break
    count+= 1
        
'''NOTA: Puede succeder que el scraping busque en toda la página la etiqueta
que le hemos mandado, por tanto, saldrán repetidas información que nos interesa
En este caso, vamos a limitar, pues sabemos la cantidad de equipos de fútbol
que hay en 1ª División.'''



'''Para tener un ejemplo más completo, vamos también a realizar el mismo ejemplo
con los puntos de los equipos de 1ª División.'''

# Puntos

pt = soup.find_all('td', class_='destacado')

puntos = list()

count=0
for i in pt:
    if count < 20:
        puntos.append(i.text)
    else:
        break
    count+= 1

print(puntos)

'''Finalmente, para tener almacenada está ( en modo prueba) o otra información,
vamos a crear un fichero CSV y almacenar ahí la información'''

