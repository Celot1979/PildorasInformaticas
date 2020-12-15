from io import open
cancion = open("Texto de la cancion.txt", "r")
busqueda = str(input("Busca la palabra que deseas: "))
informacion= cancion.readlines()
print(informacion)
frases = []
cantidad = 0
for linea in informacion:
    cantidad += 1
    print(cantidad)
    #print(linea) 
    linea =linea.strip()
    separador = linea.split()
    print(separador)
    if busqueda in separador:
        print(cantidad + "-" + separador)
    else:
        print("error")

print(str(cantidad) + frases)
