from io import open
archivo_externo=open("Primer_Archivo.txt", "r")

toda_informacion = archivo_externo.readlines()
archivo_externo.close()

print(toda_informacion)