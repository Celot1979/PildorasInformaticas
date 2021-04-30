""" 

Frases para ordenar:

Los lunes son los mejores días para programar
Python es moderno
Veremos Inteligencia Artificial más adelante
Lambda simplifica el código"""

lista= ["Los lunes son los mejores días para programar","Python es moderno",
"Veremos Inteligencia Artificial más adelante","Lambda simplifica el código"]
#print(lista)
"""def ordena(m):
    return len(m.split())

lista.sort(key=ordena, reverse=True)
print(lista)"""

lista.sort(key=lambda f: len(f.split()), reverse=True)
print(lista)
