""" Aquí es donde vamos a manipular el archivo """

cancion = open("Texto de la cancion.txt", "r")

informacion= cancion.readlines()#Leer todas las líneas. No es necesario para buscar palabras en e texto
busqueda = str(input("Que palabra busca: "))#Palabra que deseamos buscar en el texto
lineas_escribir=[]#Donde se guardarán las lineas que contengan las palabras que queremos
numero_linea=0#Variable que va contando la líneas
for linea in informacion:
    numero_linea += 1#Contador
    linea = linea.rstrip()#Saca por consola todas las líneas del archvio de texto
    separado = linea.split(" ")
    print(separado)#1º Crea una lista de cada frase.2ºSepara las palabras de cada frase
    if busqueda in separado:
        #Contrasta la palabra escrita para ver si está en el archivo de texto
        lineas_escribir.append(str(numero_linea) + "-" + linea)
        #1º Describe donde está la frase- posición-,2º la separación.3º La frase donde está la palabra buscada

print(lineas_escribir)
    
