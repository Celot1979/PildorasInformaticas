import os
import io
""" 1º Hemos ido por los directorios hasta llegar al directorio de trabajo
    2º A continuación hemos creado el Directorio de pruebas, donde iremos probando los diferentes métedos que hemos ido 
    aprendiendo.
    3º Vamos a crear un archivo de texto, en realidad 3 para poder practicar. """


os.chdir("Ejercicio de archivos")
#print(os.listdir("./"))
#os.makedirs("Directorio Resumen")
os.chdir("Directorio Resumen")
#---------------------------------------------------------------------------------------------------
#Creación de los archivos
""" Creación de un archivo de texto, pero crearemos 2 más 
archivo1= open("archivo1.txt", "w")
nuevo1 = archivo1.write("1ª Línea de texto\n2º Línea de texto\n3ª Línea de texto\n4º Línea de texto")
archivo1.close()
archivo2= open("archivo2.txt", "w")
nuevo1 = archivo2.write("1ª Línea de texto\n2º Línea de texto\n3ª Línea de texto\n4º Línea de texto")
archivo2.close()
archivo3= open("archivo3.txt", "w")
nuevo1 = archivo3.write("1ª Línea de texto\n2º Línea de texto\n3ª Línea de texto\n4º Línea de texto")
archivo3.close()"""
#----------------------------------------------------------------------------------------------------
#Modificar los archivos.
"""Lo que está haciendo es modificar, es decir, dejar lo escrito y añadir las líneas de texto
archivo1= open("archivo1.txt", "a")
nuevo1 = archivo1.write("1ª Línea de texto\n2º Línea de texto\nAquí cambio la líneas")
archivo1.close()"""

#----------------------------------------------------------------------------------------------------
# Cambio de contenido de los archivos.
""" archivo2= open("archivo2.txt", "r+")
texto= archivo2.readlines()

texto[1]="Cambiamos está línea"
texto[2]="3ª Línea de texto"
texto[3]="4ª Línea de texto"

archivo2.seek(0)
archivo2.writelines(texto)
print(texto) """

#----------------------------------------------------------------------------------------------------
# Borrar un archivo de un directorio
""" Para borrar un archivo de texto debemos ir al directorio en cuestión. 
Luego usaremos el método os.remove("archivo.txt") """
#os.remove("archivo3.txt")

#----------------------------------------------------------------------------------------------------
# Eliminar un directorio
""" Para eliminar un directorio 1º hay que elimnar los archivos que contengay luego
eliminarlo """

#os.remove("archivo1.txt")

""" os.remove("archivo2.txt")"""

print(os.listdir("./"))
os.chdir("../")
os.rmdir("Directorio Resumen")