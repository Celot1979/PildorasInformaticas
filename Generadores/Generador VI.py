""" La forma más resumida , y fácil de trabajar con generadores
sería con está estructura"""

def capitales_mundo(*ciudades):
    for capital in ciudades:
        #for letra_capital in capital:
            yield from capital
""" Usando yield from quiere decir a Python que entre
directametne en los subelementos. Por lo tanto, ahorramos
código directamente"""

capitales_devueltas = capitales_mundo("Berlin", "Roma", "Bogota", "Pekin", "Hanoi")

print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))