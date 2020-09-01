def divide():
	try:
		op1=(float(input("Introducce el primer número: ")))
		op2=(float(input("Introducce el segundo número: ")))
		print("El resultado es " + str(op1/op2))
	except ZeroDivisionError:
		print("No se puede dividir por cero")
	except ValueError:
		print("El valor introduccido no es correcto")

divide()
print("Cálculo finalizado")
