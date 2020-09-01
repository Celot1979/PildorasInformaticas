def generarPares(limite):
	num=1
	while num < limite:
		yield num*2
		num+=1
pares=generarPares(6)
print(next(pares))
print(next(pares))#Cada vez que se llame, imprimirá el siguiente






'''En esta tercera parte quitamos el ciclo for; y 
usamos el método next().'''

'''El método next realizada la impresión de cada 
elememto iterable. Su particularidad es que lo hace en uno en uno;es decir, imprime el primero, y hasta que no es llamado nuevamente, no imprime el segundo'''
