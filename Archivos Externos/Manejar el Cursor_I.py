from io import open
archivo_externo=open("Primer_Archivo.txt", "r") #Es un archivo
#Es un archivo creado con aterioridad, y como hemos visto podemos
#modificarlo cambiando la -r- read por -a- de modificar.

#informacion = archivo_externo.readline()

#Voy a agregar una línea más en le archivo.

#archivo_externo.write("\nEstamos manipulando el texto para la siguiente lección.")
#archivo_externo.write("\nEstá nueva lección va sobre como manejar el cursor en los archivos de texto.")

#archivo_externo.close()

#print(informacion)

""" Una vez modificado las líneas y añadido dos línas más como hemos hecho antes.
Vamos hacer una doble lectura del texto. Para eso, vamos a comentar las l´neas 
que ya no nos interesan que continuen en acción. """

#print(archivo_externo.read())
#archivo_externo.seek(0)
""" Así conseguimos que vuelva a leer desde el principio el texto.
El motivo es que con el metdo -seek- podemos indicar al cursor 
donde posicionarse """
#print(archivo_externo.read())

""" Si hicieramos la misma operación con el método read().Es decir, introducir
un número como parámetro, hará el efecto contrario.
Leerá desde el 0 hasta el número del parámentro. """
#-------------------------------------------------------------------
""" Supongamos que queremos sólo imprimir la mitad del texto del
archivo, se haría de la sigueinte forma: """
archivo_externo.seek(len(archivo_externo.read())/2)
print(archivo_externo.read())

#-------------------------------------------------------------------