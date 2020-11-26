from io import open
archivo_externo=open("Primer_Archivo.txt", "a")

archivo_externo.write("\n Ahora vamos a usar la función -a- para añadir este texto")
archivo_externo.close()