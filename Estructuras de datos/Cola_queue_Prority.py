""" En esté archivo vamos a trabajar con las colas(queue) con tipo
LIFO.Son muy usadas para la programación concurrente(multitarea). """

import queue
#---------------------------------------------------------------
#Para crear la 1ª cola de tipo LIFO se realiza con la siguiente
#estructura
miCola = queue.PriorityQueue()
#---------------------------------------------------------------
#---------------------------------------------------------------

#Para agregar elementos a la cola se usa el método - put() -
miCola.put((3,"Madrid"))
miCola.put((1,"Bogotá"))
miCola.put((2,"México"))
#---------------------------------------------------------------
#El método -.full()- comprueba la cantidad de elementos que exite
#en la cola para saber si está llena o no.La respuesta es booleana
# por tanto, si está llena será TRUE y lo contrario FALSE.
print(miCola.full())
#---------------------------------------------------------------

#---------------------------------------------------------------
#El método -.empty()- comprueba si la cola  está vacia.
#Muy usada con un bucle while
"""while not miCola.empty():
    print(miCola.get())"""
#---------------------------------------------------------------



#---------------------------------------------------------------

#Para sacar elementos de la cola se usa el método - get() -
# Si sólo uso el método sin especificar nada más, saldrá el
#último elemento en haber entrado en la cola.

print(miCola.get())
#Sólo no imprimirá el último elemento introduccido; es decir, México.
#Además lo ha sacado de la cola.
#---------------------------------------------------------------
#---------------------------------------------------------------
#Si queremos ver todos los elementos restantes que se han quedado
#en la cola, debemos crear un bucle donde a cada vuelta de bucle 
#No imprima el elemnto.
# IMPORTARTE: especial atención en como se hace la estructura 
#del bucle. Se usa  "nombre de la cola".queue
print("A continuación se impre los elementos restantes de la cola")

for elemento in miCola.queue:
    print(elemento)
