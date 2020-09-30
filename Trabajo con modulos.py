# 1º forma de usar módulos
# import funciones_matematicas
""" Sentencias para funcionar con la 1º forma
funciones_matematicas.sumar(3,5)
funciones_matematicas.multiplicar(3,5)
funciones_matematicas.resta(3,5)"""

""" Hemos creado un módulo que se llama funciones_matematicas ( que no es más
que un archivo .py con unas operaciones). 

Para poder usarlo en este archivo, debemos importar primero el modulo:
import funciones_matematicas

Luego debemos llamar en la operación que deseemos realizar, llamar a la función del modulo
. y la operación deseada."""

# 2º Forma de usar módulos
"""from funciones_matematicas import sumar #Si quisera todas las funciones *
sumar(3,5)"""

# 3 Forma de usar Paquetes
#from moduloMatematico.funciones_matematicas import *
#sumar(3,5)
""" Creado dentro del directorio que deseemos el archivo __init__.py, declaramos
al editor que es un paquete.
A continuación en el archivo donde queremos usarlo, debemos:

from (nombre del paquete.archivo que deseamos trabajar) import (función que nos interesa)"""

# 4 Subpaquetes
#from moduloMatematico.calculosBasicos.funciones_matematicas import *
#sumar(6,6)
from moduloMatematico.otrosCalculos.PotenciaYRedondeo import*
potencia(2,5)
redondear(3.4534343434)