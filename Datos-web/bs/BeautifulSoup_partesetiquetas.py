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

etiquetas = soup('a')
for etiqueta in etiquetas:
    print('ETIQUETA:',etiqueta)
    print('URL:',etiqueta.get('href',None))
    print('CONTENIDO:',etiqueta.contents[0])
    print('ATRIBUTOS:',etiqueta.attrs)