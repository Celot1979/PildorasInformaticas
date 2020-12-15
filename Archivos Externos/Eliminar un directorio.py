import os
import io
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

os.chdir("PracticaDirectorio")
os.remove("Archivo1.txt")
os.remove("Archivo2.txt")
os.chdir("../")
os.rmdir("PracticaDirectorio")