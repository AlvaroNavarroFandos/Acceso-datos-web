#Programa para sacar las lineas que empiezan por X seguida de cualquier caracter que no sea espacio y : seguido de un espacio y un numero decimal
#Extraemos solo los numeros de esas lineas si son mayores que cero
import re
archivo = open('mbox-short.txt')
for linea in archivo:
    linea = linea.rstrip()
    if re.search('^X\S*: [0-9.]+', linea):
        linea = linea.split()
        numerin = float(linea[1])
        if numerin > 0:
            print(numerin)