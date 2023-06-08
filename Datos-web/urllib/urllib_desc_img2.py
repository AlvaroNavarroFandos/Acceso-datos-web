# Programa para descargar una imagen de una web pero poco a poco para no utilizar toda la memoria disponible de vez
import urllib.request, urllib.parse, urllib.error

imagen = urllib.request.urlopen("http://data.pr4e.org/cover3.jpg")
manejador = open("portada.jpg", "wb")
tamaño = 0
while True:
    info = imagen.read(100000)
    if len(info) < 1:
        break
    tamaño = tamaño + len(info)
    manejador.write(info)

print(tamaño, "caracteres copiados")
manejador.close()
