<<<<<<< HEAD
# Programa que al introducir un nombre de archivo, busque las lineas de la forma 'New Revision: xxxxx', coja esos numeros y saque el promedio
import re

archivo = input("Ingresa nombre de archivo: ")
=======
#Programa que al introducir un nombre de archivo, busque las lineas de la forma 'New Revision: xxxxx', coja esos numeros y saque el promedio
import re
archivo = input ('Ingresa nombre de archivo: ')
>>>>>>> a05e020 (si)
n_archivo = open(archivo)
cont = 0
total = 0
for linea in n_archivo:
    linea = linea.rstrip()
<<<<<<< HEAD
    num = re.findall("^New .+: ([0-9]+)", linea)  # Expresion regular para entrar solo a esas lineas y quedarnos con el numero()
    if len(num) > 0:  # Para que entre cuando haya de verdad un numero y no este vacio
        fnum = float(num[0])  # Lo pasamos a decimal ya que el numero es un string
        total = total + fnum
        cont = cont + 1

promedio = total / cont
print("{:.7f}".format(promedio))
=======
    num = re.findall('^New .+: ([0-9]+)',linea) #Expresion regular para entrar solo a esas lineas y quedarnos con el numero()
    if len(num) > 0:            #Para que entre cuando haya de verdad un numero y no este vacio
        fnum = float(num[0])    #Lo pasamos a decimal ya que el numero es un string
        total = total + fnum
        cont = cont +1

promedio = total / cont
print("{:.7f}".format(promedio))
>>>>>>> a05e020 (si)
