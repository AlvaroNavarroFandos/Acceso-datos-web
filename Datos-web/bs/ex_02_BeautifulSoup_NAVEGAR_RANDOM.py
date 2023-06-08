#Programa que pide una URL, un numero de repeticiones y una posicion para etiquetas o enlaces web. Extrae los datos que hay en esa posicion con 
#BeautifulSoup y guarda la url para dirigirse a ella en la siguiente repeticion y asi sucesivamente. Va de una url a otra tantas veces como queramos
#y se queda con el contenido de la ultima etiqueta iterada en la posicion marcada en la ultima repeticion

import urllib.request, urllib.parse, urllib.error   #Importar urllib, BeautifulSoup y SSL
from bs4 import BeautifulSoup
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

 #Prueba http://py4e-data.dr-chuck.net/known_by_Fikret.html 
 #Real  http://py4e-data.dr-chuck.net/known_by_Aishah.html

#Pedimos los datos a introducir por el usuario
url = input('Introduzca - ')   
n_veces = input('¿Cuántas veces quieres repetir el proceso?: ')
spos = input ('Introduzca la posición: ')
#Convertir a int los str recibidos
pos = int(spos) -1
repe = int(n_veces)
#Inicializar las variables
i = 0
l_nombres = list()
l_url = list()

def repe0(url):                             #Funcion para sacar el primer nombre(triple split) de la primera URL para guardar en las listas
    casinombre1 = url.split('/')
    casnombre1 = casinombre1[3].split('_')
    canombre1 = casnombre1[2].split('.')
    nombre1 = canombre1[0]
    l_nombres.append(nombre1)
    l_url.append(url)

repe0(url)  #Conseguir la iteracion inicial gracias a la funcion

#Bucle para realizar las repeticiones necesarias que quiere el usuario
while i < repe:
    html = urllib.request.urlopen(url, context=ctx).read()  #Abrimos la web a rascar
    soup = BeautifulSoup(html, 'html.parser')               #LLamamos a la biblioteca de BeautifulSoup
    etiquetas = soup('a')                                   #Tipo de etiquetas que queremos rascar ('a' son las de anclaje)
    
    l_nombres.append(etiquetas[pos].contents[0])            #Extraer el contenido de las etiquetas en la posicion que quiere el usuario    
    url = etiquetas[pos].get('href',None)                   #Extraer la url de las etiquetas en la posicion que quiere el usuario
    l_url.append(url)
    i += 1                                                  #Los guardamos en sus listas y preparamos la siguiente iteracion

ult_nombre = l_nombres[repe]                                #Mostramos el ultimo contenido despues de realizar las repeticiones en la pos requerida
print(ult_nombre)