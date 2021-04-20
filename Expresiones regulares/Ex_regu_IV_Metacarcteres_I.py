import re
# Metacaracteres
print("Metacaracter para iniciar una busqueda ^")
lista_nombre=["Antonio Banderas", "Salma Hayek","Tomas Cruceros","Antonio Resines","Friedrich Hayek"]
for nombre in lista_nombre:
    if re.findall("^Antonio",nombre):
        print(nombre)

print("----------------------------------------------------------------")
print("Metacaracter para buscar en el final de la busqueda $")
# Entendiendo el final de la búsqueda como el apellido
lista_nombre=["Antonio Banderas", "Salma Hayek","Tomas Cruceros","Antonio Resines","Friedrich Hayek"]
for nombre in lista_nombre:
    if re.findall("Hayek$",nombre):
        print(nombre)


print("----------------------------------------------------------------")
print("Metacaracter para basar la búsqueda en caracteres diferentes.Por ejemplo acentos, la ñ , etc . []")

lista_terminos =["camión", "camion","niños","niñas","ejemplo"]
for nombre in lista_terminos:
    if re.findall("cami[oó]n",nombre):
        print(nombre)

print("----------------------------------------------------------------")
