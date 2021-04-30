mi_lista=[(11,5),(15,7),(2,4),(15,19),(8,4)]
""" Sumar los valores internos de cada tuplan
es decir, del 1º sería 16, del 2º sería 17, del 3º sería 
22, etc""" 

#Funcion normal 

"""def ordenar_lista(t):
    return t[0] + t[1]

#Ahora ordenamos la lista 
mi_lista.sort(key=ordenar_lista)
print(mi_lista)"""

#Funcion lambda 

mi_lista.sort(key=lambda t: t[0]+t[1])
print(mi_lista)