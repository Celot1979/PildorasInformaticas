"""edad=int(input("Introducce tu edad: "))

while edad < 0 or edad > 100:
    print("Has introduccido una edad negativa, no validad")
    edad=int(input("Introducce tu edad: "))
print("Gracias puedes pasar")
print("Edad del usuario: " + str(edad))"""
#---------------------------------------------------------------------
import math
print("Este programa halla la raíz cuadra de un valor númerico")

numero=int(input("Introduce un número: "))

intentos=1

while numero < 0:
    print("El valor númerico no puede ser negativo")
    numero=int(input("Introduce un número: "))
    intentos=intentos+1

    if intentos == 3:
        break
if intentos == 3:
    print("Los siento, no puedo realizar el cálculo")
else:
    print(math.isqrt(numero))
