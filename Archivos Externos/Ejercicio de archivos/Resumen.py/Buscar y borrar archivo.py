import os
import io

# Buscar y borrar un archivo especifico

listaArchivos = os.listdir("./")
for archivo in listaArchivos:
    if archivo == "tirar.py":
        os.remove(archivo)