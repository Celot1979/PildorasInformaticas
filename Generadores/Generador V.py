""" Para conseguir realizar un ciclo for, sobre otro ciclo for
es decir (anidar bucles); y poder trabajar con los ementos
que están dentro de otros elementos, Se realiza la siguiente 
operación"""

def capitales_mundo(*ciudades):
    for capital in ciudades:
        for letra_capital in capital:
            yield letra_capital

capitales_devueltas = capitales_mundo("Berlin", "Roma", "Bogota", "Pekin", "Hanoi")

print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))