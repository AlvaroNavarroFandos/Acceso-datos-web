# Programa para descargar una imagen de una web pero poco, los 3000 primeros caracteres y mostrarlos, y luego
#acabar y contar todos los caracteres del documento
import urllib.request, urllib.parse, urllib.error


imagen = urllib.request.urlopen("http://data.pr4e.org/cover3.jpg")
manejador = open("portada.jpg", "wb")
tamaño = 0

while tamaño < 3000:
    info = imagen.read(500)
    if len(info) < 1:
        break
    tamaño += len(info)
    manejador.write(info)

print('STOP THE COUNT',tamaño)

while len(info) >= 1:
    info = imagen.read(1000)
    tamaño += len(info)
    
print(tamaño, "caracteres copiados")
manejador.close()