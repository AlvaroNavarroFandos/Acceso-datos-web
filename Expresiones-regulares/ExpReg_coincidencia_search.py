<<<<<<< HEAD
# Programa que al introducir una palabra  cuente las lineas en las que está esa palabra
import re

archivo = open("mbox-short.txt")
exp = input("Ingresa una expresión regular: ")
cont = 0
for linea in archivo:
    if re.search(exp, linea):
        cont = cont + 1

print("mbox.txt tiene", cont, "líneas que coinciden con", exp)
=======
#Programa que al introducir una palabra  cuente las lineas en las que está esa palabra
import re
archivo = open ('mbox.txt')
exp = input ('Ingresa una expresión regular: ')
cont = 0
for linea in archivo:
    if re.search(exp,linea):
        cont = cont +1

print('mbox.txt tiene',cont,'líneas que coinciden con',exp)
>>>>>>> a05e020 (si)
