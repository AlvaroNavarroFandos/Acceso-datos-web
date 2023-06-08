# Busqueda de las lineas que empiezan con 'From' y un caracter seguido de un numero de dos digitos seguido de ':' e imprimirlo si es >0
# Para sacar las horas de una linea de correo
import re

archivo = open("mbox-short.txt")
for linea in archivo:
    linea = linea.rstrip()
    lineabuena = re.findall("^From .* ([0-9][0-9]):", linea)
    if len(lineabuena) > 0:
        print(lineabuena)
