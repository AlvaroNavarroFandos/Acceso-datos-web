# Lee los datos de la web y crea un historiograma para ver con cuanta frecuencia se repiten las palabras, imprime el diccionario entero y luego saca las 3 que mas
import urllib.request, urllib.parse, urllib.error

manejador = urllib.request.urlopen(input("Introduce una url completa de una web: "))

contadores = dict()
for linea in manejador:
    palabras = linea.lower().decode().split()
    for palabra in palabras:
        contadores[palabra] = contadores.get(palabra, 0) + 1

print(sorted([v, k] for k, v in contadores.items()))

lst = list()
for k, v in contadores.items():
    lst.append((v, k))

lst = sorted(lst, reverse=True)

for v, k in lst[:3]:
    print(k, v)
