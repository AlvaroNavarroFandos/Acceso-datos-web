# Siempre se importa esto para rascar web con BeautifulSoup ya que a veces html tiene errores
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduzca un enlace web: ')
html = urllib.request.urlopen(url, context=ctx)
soup = BeautifulSoup(html, 'html.parser')
cont = 0

l = list(
    
)
etiquetas = soup('p')
for etiqueta in etiquetas:
    cont += 1
    l.append(etiqueta)
    #print(l)    #si quisieramos mostrar todos los parrafos en forma de lista
    
print('Hay',cont,'párrafos en esta web') 