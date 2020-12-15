import os
from io import open
""" Vamos a crea un directorio usando la liberia os y con sus métodos """
#os.makedirs("PruebaDirectorio")
os.chdir("PruebaDirectorio")
nuevo = open ("ArchivoDirectorios.txt", "w")
escribir = nuevo.write("Es un ejemplo de como se debe de hacer para crear un archivo en un directorio")
nuevo.close()

""" Para saber en que directorio nos encontramos, usaremos otro método """

#print(os.getcwd())


""" Una vez que comprobamos la línea anterior, y nos dice por consola
en que directorio nos encontramos, si queremos irnos al directorio creado, o mejor aún
crear uno y irnos a él debemos realizar los siguientes pasos:

En la línea 3 hemos creado el directorio, pues justo debajo de esa línea de código usaremos
el método chdir() """


""" NOTA: La creación del archivo y escrbir en él, tan solo ha sido un ejercicio que
nos ha propuesto el profesor.
HEmos de entender que una vez creado el directorio, movido a él; se puede crar un
archivo de texto y trabajar con él con normalidad. """

#Aqui vamos a realizar dos tareas, 1º mostrarnos lo que hay en el directorio.
# "º que nos imprima cada cosa que hay en él por consola"
#print(os.listdir("./"))

os.rmdir("PruebaDirectorio")