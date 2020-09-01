capitales={"España": "Madrid", "Inglaterra": "Londres", "Portugal": "Lisboa", "Francia": "Paris", "Alemania": "Berlin"}

for i in capitales:
	valores = capitales[i]
	print(i)
	print(valores)
	
""" Para imprimir sòlo las keys del diccionario, simplemente habría
que hacer un for i in capitales. La sigueinte línea de código, sería print(i)
Para realizar una impresión de keys y value; tendríamos que crear una variable y dentro de ella, posicionar el nombre del diccionario y meter entre corchete / llamar a el value"""

"""Si quisieramos que saliese todo el diccionario impreso de una sóla vez; simplemente pondríamos esta sentencia"""
print(capitales.items())
print(capitales.keys())
print(capitales.values())

""" Otr forma es usar un bucle para imprimir tanto la clave como el valor"""
for clave, valor in capitales.items():
	print(clave + " ==> " + valor)
