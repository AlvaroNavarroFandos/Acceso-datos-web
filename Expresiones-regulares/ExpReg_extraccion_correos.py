#Programa para sacar todos los correos electronicos de un archivo de texto
import re
archivo = open('mbox-short.txt')
for linea in archivo:
    linea = linea.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', linea)
    if len(x) > 0 :
        print(x)