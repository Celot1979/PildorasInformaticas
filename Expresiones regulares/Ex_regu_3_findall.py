import re
# Metodo findall
""" Sirve para buscar la cantidad de coincidencias
que existe en la cade/texto que estoy buscando """
cadena ="Estoy trabajando con Python el Martes. El prox Martes no trabajaré en esto.Trabajaré el prox Martes 19"
#print(re.search("Estoy", cadena))
busqueda ="Martes"
texto_encontrado =len(re.findall(busqueda, cadena))
print(texto_encontrado)