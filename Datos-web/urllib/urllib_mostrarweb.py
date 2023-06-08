# Imprime la url web que encuentra en una web y se dirige a ella para mostrar su contenido
import urllib.request

archivo = urllib.request.urlopen(input("Introduce una url completa de una web: "))

for linea in archivo:
    linea = linea.decode()
    palabras = linea.split()
    for palabra in palabras:
        if palabra.startswith("href="):
            direccion = palabra.split('"')
            print(direccion[1])
            websig = urllib.request.urlopen(direccion[1])
            for linea in websig:
                print(linea.decode().rstrip())
