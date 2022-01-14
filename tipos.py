import math
"""Escribe una cadena de formato para los datos de tipo string y float
 usando las siguientes sintaxis: Hola  Juan Perez. Tu balance es 53.44$."""

name = "Juan Perez"
balance = 53.44

print ("Hola %s. Tu balance es %.2f$." %(name,balance))


"""Realiza varias conversiones de tipo (a_float = float("3,14") o string = str(a_float) )
 con float, int, boolean y string, y comprueba el tipo que se le asigna a la variable convertida.
"""


num1 = float(math.pi)

value_True = 1

boolTrue = bool(value_True)

floatPi = float(num1)

stringFalse = str(False)

print(type(num1))
print(type(boolTrue))
print(type(floatPi))
print(type(stringFalse))


#Comprueba la longitud de varios tipos (int, string, float) con el método len

num = 12345

valInt = len(str(num))

st = "hola mundo"

valString = len(st)

flo = 12.5678

valFloat = len(str(flo))

print("Longitud de un int: %d. Longitud de un string: %d. Longitud de un float: %d" % (valInt,valString,valFloat))


#Realiza un ejemplo de utilización de los métodos de string strip, split, lower, upper, find, index y startswith.

frase1 = "Hola mundo"

frase2 = frase1.strip('H')

print(frase2)

frase3 = frase1.split()

print(frase3[1] + frase3[0])

frase4 = frase1.lower()

print(frase4)

frase5 = frase1.upper()

print(frase5)

frase6 = frase1.find("mun")

print("La cadena 'mun' se encuentra en el indice %d" % frase6)

frase7 = frase1.index('la')

print("La cadena 'la' se encuentra en el indice %d" % frase7)

frase8 = frase1.startswith('H')

print("La frase comienda con 'H'?: %s" % frase8)


#Utiliza el paquete re para buscar el número de ocurrencias de la letra “a” en la primera frase del Quijote.

import re

quijote = "En un lugar de La Mancha, cuyo nombre no quiero acordarme..."

iterator = re.findall('a',quijote)

print(len(iterator))