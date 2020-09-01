"""Ejercicio excepciones. Agregar elemento en una lista
Crea un programa que pida introducir por consola 10 nombres propios de personas.
Los nombres se guardarán en una lista.
Si introducimos un nombre repetido, el programa lanzará una excepción de tipo ValueError, la excepción nos informará del error con el texto “Error. Este nombre ya se ha introducido”, y no se guardará el nombre repetido en la lista.
Imprimir el contenido de la lista por consola."""
print("Debes de introduccir 10 nombres")
pregunta= str(input("¿Quieres empezar a introduccir los nombres? : "))
intentos=0
nombres=[]
if pregunta == "si" or pregunta == "Si":
	while intentos<10:
		nombre = str(input("Introduce el nombre: "))
		try:
			if nombre in nombres:
				raise ValueError
			else:
				nombres.append(nombre)
				
		except ValueError:
			intentos-=1
			print("Error. Este nombre ya se ha introducido")
			
		intentos+=1
		
print(nombres)
	


	


"""if nombres[2] == nombres[1]:
	del nombres[2]
print(nombres)"""
	
	
