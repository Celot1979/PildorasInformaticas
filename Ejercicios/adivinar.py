from random import randint
aleatorio = randint(0,100)
intentos= 0
numero = int(input("Introduce un número, por favor: "))

while aleatorio != numero:
    if aleatorio > numero:
        intentos+=1
        print("Más alto")
        numero = int(input("Introduce un número, por favor: "))
    elif aleatorio < numero:
        intentos+=1
        print("Más alto")
        numero = int(input("Introduce un número, por favor: "))
        
print("Correcto. Lo has conseguido en " + str(intentos) + " intentos")