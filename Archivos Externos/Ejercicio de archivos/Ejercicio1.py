from io import open

""" Vamos a crear un ejercicio donde tengamos varias líneas de 
archivo de textos y mediante un bucle for, vayamos sacando partes
de ese archivo.
Como tarea de nota, vamos a buscar palabras, o cuantas veces sale 
una palabra en el texto. """

#1º. Vamos a crear el archivo y escribir la lineas que deseamos
cancion = open("Texto de la cancion.txt", "w")

#2º. Vamos a escribir el texto que deseamos guardar en ese archivo
cancion.write("Oh, una tormenta es una amenaza\nMi vida de hoy\nSi no consigo refugio\nOh, sí, me voy a desvanecer\nGuerra, niños, es sólo un tiro de distancia\nEstá a un tiro de distancia\nOh, mira que el fuego está barriendo\nNuestra misma calle hoy\nSe quema como una alfombra roja de carbón\nMad Bull perdió su camino\nGuerra, niños, es sólo un tiro de distancia\nEstá a un tiro de distancia\Violación, asesinato\nEstá a un tiro de distancia\nEstá a un tiro de distancia")

#3º. Salimos del archivo para que no consuma recursos de la RAM
cancion.close()