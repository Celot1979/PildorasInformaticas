def capitales_mundo(*ciudades):
	for capital in ciudades:
		for letra_capital in capital:
			yield letra_capital
		
capitales_devuletas=capitales_mundo("Berlin", "Roma", "Bogota", "Pekin", "Hanoi")

print(next(capitales_devuletas))
print(next(capitales_devuletas))

	
