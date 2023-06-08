# Programa para sacar las lineas que empiezan por X seguida de cualquier caracter que no sea espacio y : seguido de un espacio y un numero decimal
# Extraemos solo los numeros de esas lineas si son mayores que cero
import re

archivo = open("mbox-short.txt")
for linea in archivo:
    linea = linea.rstrip()
    x = re.findall("^X\S*: ([0-9.]+)", linea)
    if len(x) > 0:
        print(x)
