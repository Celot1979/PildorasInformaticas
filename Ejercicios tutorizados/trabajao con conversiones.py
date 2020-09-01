"""a = "15"
b= "35"
print(a+b)
print(int(a)+ int(b))

a= "15.5"
b= "35.5"
print(float(a)+float(b))"""
#---------------------------------------------------------------------
"""edad = 25
print("mi edad es: " + str(edad) + " años ")"""
"""Si no le ponemos la funcíón str, nos daría error a la 
hora de imprimir en consola"""
#---------------------------------------------------------------------
""" Funciones Join . Sirven para convertir
una lista en un texto"""

#empleados = ["Ana", "Oscar", "Maria", "Pedro", "Juan"]

#print(" ".join(empleados))

""" Importante, para convertir una lista en una cadena de texto, 
debemos usar la función join. La sintaxis correcta es indicar primero 
que signos de separación. Luego se pone join y el nombre de
la lista"""
#---------------------------------------------------------------------

""" La función split, sirve para convertir una cadena de 
texto en una lista."""
empleados = "Ana, Oscar, Maria, Pedro, Juan"
print(empleados.split())
#---------------------------------------------------------------------