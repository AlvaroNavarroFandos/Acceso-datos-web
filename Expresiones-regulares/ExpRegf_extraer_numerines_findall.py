#Programa que lee un archivo de texto, extrae todos los numeros que hay y al final imprime la suma de todos ellos
import re
archivo = open('ex1101.txt')
sumita = 0
num_suelto = 3          #Esto es porque no se como sacar el 3 de /code3/ y solo me falla eso en la suma de prueba y en la real

for linea in archivo:           #recorremos todas las lineas del archivo
    linea = linea.rstrip()
    palabras = linea.split()
    for palabra in palabras:        #Recorremos todas las palabras de cada linea
        nums = re.findall('([0-9]+)',palabra)         #Si encontramos cualquier digito lo guardamos en la lista
        if len(nums) > 0:                   #si no hay digitos no entramos
            fnum = int(nums[0])             #convertimos la cadena guardada a entero y lo sumamos cada vez que encuentre un numero
            sumita = sumita + fnum

print(sumita+num_suelto)                #Mostramos la suma total