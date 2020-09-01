import math
def calculaRaizCuadrada(numero):
	if numero<0:
		raise ValueError("El numero no puede ser negativo")
	else:
		return math.sqrt(numero)
numeroUsuario=(int(input("Introduce un número: ")))
print(calculaRaizCuadrada(numeroUsuario))
print("y por aquí continuaría el programa")

""" La función raise es para provocar al imprimir en consola, un error tipo valueError, con la salvedad que saldrá imprimido el mensaje que nosostros elijamos. 
Será muy practico cuando podamos crear paquetes nosotros mismo"""
