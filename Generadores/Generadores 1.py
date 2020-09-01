"""def generarPares(limite):
	num=1
	numerosPares=[]
	while num < limite:
		numerosPares.append(num*2)
		num =num+1
	return numerosPares
	
print(generarPares(6))"""

"""El código de arriba es una función normal
A continuación realizarmos una
transformación para realiacar un
generador"""
def generarParesGenerador(limite):
	num=1
	
	while num < limite:
		yield num*2
		num=num+1
su_par=generarPares(6)
	
"""for i in su_par:
	print(i)"""
print(next(su_par))


