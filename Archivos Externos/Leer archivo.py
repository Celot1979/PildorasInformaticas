from io import open
archivo_externo=open("Primer_Archivo.txt", "r")

informacion = archivo_externo.read()
archivo_externo.close()

print(informacion)