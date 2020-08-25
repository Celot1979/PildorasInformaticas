import random
intentos=5
pregunta = str(input(" Quieres jugar: "))
maquina= random.randint(1,100)
#print(maquina)

while pregunta != 0:
    intentos = intentos - 1
    numero = int(input("Introduzca su número: "))
    if numero > maquina:
        print("El número es mayor que el de la máquina")
    elif numero < maquina:
        print(" El numero es menor que el aleatorio")
    elif numero == maquina and intentos != 0:
        print("El numero es : " + str(numero) + "el número aleatorio es : " + str(maquina) + " y lo has hecho en : " + str(intentos))
    if intentos == 0:
        break


if intentos == 0:
    print("No lo has conseguido. El número era: " + str(maquina))




