""" En esté apartado veremos renombrar , eliminar archivos y directorios. """
""" Para pode avanzar en esté apartado vamos a crear un directorio con un par de archivos. """

import os
import io

#os.makedirs("PracticaDirectorio")
os.chdir("PracticaDirectorio")
prueba = open ("Archivo1.txt", "w")
escribir = prueba.write("Esta es una línea para el primer archvio\nNos gustará practicar")
prueba.close()

prueba2 = open("Archvio2.txt" , "w")
escribir = prueba2.write("Esta es una línea para el primer archvio\nNos gustará practicar")
prueba2.close()



#Renombrar el nombre de un archivo

# 1º IR al directorio con el método :
#os.chdir("PracticaDirectorio")

#2º USar el método os.rename (1º parametro (1º nombre del txt), 2º parametro (el nuevo nombre))
#Las dos líneas de print son meramente para ver po consola que todo a ido bien, sin más
#os.rename("Archivo a eleminar.txt", "Archivo a eliminar.txt")




#Cómo eliminar un archivo
""" Vamos a eliminar el archivo que previamente hemos cambiado el nombre
a -Archivo a eliminar """
#1º IR al directorio con el método :
os.chdir("PracticaDirectorio")

#2º USar el método os.remove("El nombre del archivo que queremos eliminar.txt")

#os.remove("Archivo a eliminar.txt")
#print(os.getcwd()) 
#print(os.listdir("./"))


#Cómo eliminar un directorio
""" Vamos a eliminar el directorio -PracticaDirectorio-  que previamente hemos creado 
1ºIr a l directorio raiz al directorio con el método:
#os.chdir("PracticaDirectorio")

#2º Eliminar los archivos qu están en su interior
os.remove("Archivo1.txt") o Archivo2.txt

3º Seria salir del directorio hacia el directorio raiz
os.chdir("../)

4º Usar el os.rmdir("PracticaDirectorio)

os.rmdir("PracticaDirectorio")"""
