"""Crea un programa que pregunte por consola la renta. En función de la renta introducida, el programa devolverá el texto: “A la renta (aquí iría la renta introducida) le corresponde un (aquí iría el tipo impositivo) de tipo impositivo.

Ejemplo: En caso de introducir por consola 13500, el programa devolverá el texto: “A la renta 13500 le corresponde un 15% de tipo impositivo”

El programa debe permitir la introducción de rentas decimales."""

pregunta = float(input(" ¿Qué renta tienes? \n"))
tipo = 0 

if pregunta <= 12000 :
   tipo = 7
elif pregunta > 12000 and pregunta < 18000:
    tipo = 15
elif pregunta > 18000 and pregunta < 35000:
    tipo=21
elif pregunta > 35000 and pregunta < 70000:
    tipo = 35
else:
    tipo = 45


print('A la renta {} le corresponde un {}  de tipo impositivo"'.format(pregunta, tipo))
