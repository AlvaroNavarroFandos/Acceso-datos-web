# Lee y descarga en la misma carpeta de trabajo una imagen de una web de internet
import urllib.request, urllib.parse, urllib.error

imagen = urllib.request.urlopen("http://data.pr4e.org/cover3.jpg").read()
manejador = open("portada.jpg", "wb")
manejador.write(imagen)
manejador.close()
