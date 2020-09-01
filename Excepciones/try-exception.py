import sys
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
	try:
		return num1/num2
	except ZeroDivisionError:#En caso que dividan por cero
		print("No se puede dividir por cero")
		return "operacion incorrecta"
intentos=0
while True:
	try:
		op1=(int(input("Introduce el primer número: ")))
		op2=(int(input("Introduce el segundo número: ")))
		break	
	except ValueError:
		intentos+=1
		print("No se puede añadir letras")
		if intentos < 3:
			continue
		else:
			sys.exit()
			
""" Importante: No siempre se puede llenar un programa con try/except. A veces podemos ( como en bucle anterior), realizar un bucle para que el usario realice la opción que necesitamos por repetición"""

		
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")


if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecución del programa ")
