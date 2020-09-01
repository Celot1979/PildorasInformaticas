'''Vamos a crear un generador a
 raiz de la funcion de generador I.py'''

def generarPares(limite):
	num=1#Hasta aqui es como la primera funcion
	#Quitamos la lista
	while num < limite:
		yield num*2
		num+=1
		#Esta es la estructura del generador

pares=generarPares(6)
'''Para llamar al generador se crea la variable 
anterior que está fuera del generador'''
	
				
#Para que salga por consola
for i in pares:
    print(i)

'''IMPORTANTE:En este caso, lo que va a 
representar el programa en consola es que cada 
elemento iterrable se vaya impriemdo en orden, 
pero hay que tener cuenta que serán todos a la vez'''