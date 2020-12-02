from io import open
archivo = open("archivo.txt", "w")
archivo.write("Primera línea, apertura y método write")
archivo = open("archivo.txt", "a")
archivo.write ("\nSegunda línea con el método a")
archivo.write("\nEstamos manipulando el texto para la siguiente lección.")
archivo.write("\nEstá nueva lección va sobre como manejar el cursor en los archivos de texto.")
archivo.close()

""" Ahora vamos a leeer el archivo para y practicando """

archivo = open("archivo.txt", "r")
leer = archivo.read()
#print(leer)
archivo.close()

""" Si comentamos la última parte de la líneas de códogo que están justo debajo de este 
comentario, se podrá leer el texto del archivo original. Al quitar el código,se podrá leer como 
incluimos una segunda línea en la posición marcada en el enunciado el profesor """

archivo = open("archivo.txt", "r+")
texto = archivo.readlines()
""" texto[1]="Está linea es la que realizará el cambio en la segunda línea preescrita anteriormente"
archivo.seek(0)
archivo.writelines(texto)
archivo.close()  """
#print(texto[1])
texto[1]="\nEstá linea es la que realizará el cambio\n"
archivo.seek(0)
archivo.writelines(texto)
archivo.close()



