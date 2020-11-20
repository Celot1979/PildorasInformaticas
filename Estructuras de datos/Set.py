""" Ejemplo de como crear un SET con la estucturas de datos """
#Primero creamos un string para alojar los nombres de los planetas
sistema_solar="Mercurio venus Tierra Marte Jupiter Saturno Urano Neptuno Pluton"

#Ahora creamos el set donde vamos alojar estos planetas

planetas=set()

for planeta in sistema_solar.split(' '):
    planetas.add(planeta)

""" Explicación del bucle:
1º Si nos fijamos, en la declaración del string los elementos
están espaciados entre si por un hueco.A la hora que python
recorra ese string con el bucle, hay que especificar con que 
elemento lo hemos espaciado, para eso se usa el método SPLIT.

2º Posteriormete se añade los elementos con el método ADD a cada 
vuelta de bucle.  """
print(planetas)
print(len(planetas))

