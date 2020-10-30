'''Escribir un programa que , dada una frase por el usuario muestre la cantidad de vocales'''
from colorama import Fore, Style
vocales = "a,e,i,o,u"
count = 0
frase = str(input (" Escribe la frase "))
for c in frase:
    if c in vocales:
        count = count + 1

print(" La frase es: " + str(frase) + " tiene esta cantidad de vocales: " + str(count))


