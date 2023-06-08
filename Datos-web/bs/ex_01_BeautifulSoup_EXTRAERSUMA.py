#Programa que utiliza BeautifulSoup para extraer todos los numeros de las etiquetas <span> del HTML del sitio web
#Al final calcula la suma de todos esos números y el total de numeros y los muestra en pantalla.

# Siempre se importa esto para rascar web con BeautifulSoup ya que a veces html tiene errores
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduzca un enlace web: ')
#http://py4e-data.dr-chuck.net/comments_1788965.html
html = urllib.request.urlopen(url, context=ctx)
soup = BeautifulSoup(html, 'html.parser')

cont = 0
suma = 0
etiquetas = soup('span')
for etiqueta in etiquetas:
    numerin = float(etiqueta.contents[0])
    cont += 1
    suma += numerin
    
print('Cont',cont)
print('Suma',suma)