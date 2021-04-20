import re
cadena ="Estoy trabajando con Python el Martes y Semana Santa"
print(re.search("Estoy", cadena))
busqueda ="Martes"
if re.search(busqueda,cadena) is not None:
    print("Se encontro el término",busqueda)
else:
    print("No se encontro el término")
