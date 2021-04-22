import re
""" Usamos los RANGOS para encontrar las letras/numeros.
Desde un punto hasta otro punto."""
"""lista_terminos =["camión", "camion","niños","niñas","ejemplo"]

for nombre in lista_terminos:
    if re.findall("[p-z]",nombre):
        print(nombre)"""

#Buscar un rango entre la 1ª letra y un área de busqueda de p -z
#"^[p-z]"

#Buscar un rango entre la 1ª letra y un área de busqueda 
#son entre la p y la z, pero en mayúsculas.
#"^[P-Z]"

#Buscar un rango entre la última letra y un área de busqueda 
#son entre la l y la p.
#"[l-p]$"

lista_terminos =["Ma1", "Se1","Ma2","va1","ba1","se2","Ma3","Ma4"]

for termino in lista_terminos:
    if re.findall("Ma[1-3]",termino):
        print(termino)

#Buscar un rango donde en los elementos de la búsqueda hay numeros y letras, 
#se usa la siguiente expresión.
#"Se[0-2A-B]"