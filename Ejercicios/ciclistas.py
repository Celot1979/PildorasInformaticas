
import operator
'''La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).

Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
a) Determinar y mostrar el nombre del ganador de la carrera.
b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.
c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.'''

numero = int(input("¿Cúantos ciclistas compiten? "))

corredores = {}
record=[]
tiempos = []

tiempo_record= int(input("El record está en: "))
record.append(tiempo_record)




for c in range(numero):
    nombre = str(input("¿Cúal es el nombre del ciclista?: "))
    tiempo = int(input("Tiempo efectuado: "))
    tiempos.append(tiempo)
    corredores[nombre]= tiempo
#print(d)

'''for nombre in enumerate(corredores):
    print(nombre[1], 'realizó la carrera en ', corredores[nombre[1]])
    if tiempo_record > corredores.values():
        print("NUEVO RECORD!!!!")'''
    

ciclistas_ordenados = sorted(corredores.items())
#print(ciclitas_ordenados)

ciclistas_ordenados = sorted(corredores.items(), key=operator.itemgetter(1), reverse=False)

print("RANKING DE LA VUELTA")
for nombre in enumerate (ciclistas_ordenados):
    
    print(nombre[1] [0], " hizo la carrera en:  ", corredores[nombre[1] [0]])

for r in record:
    print("El record actual es de: " + str(r))
    if r < tiempo:
        print("No ha habido record")
    elif r > tiempo:
        print("TENEMOS NUEVO RECORD")

#print(str(tiempos))

media = sum(tiempos)
total = media/2
minutos = total/60
print("La media de los tiempos de los ciclistas fue de: " + str(minutos))