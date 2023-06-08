#Programa que solicitará una URL, leerá los datos XML de esa URL usando urllib y luego analizará y extraerá los recuentos
# de comentarios de los datos XML y calculará la suma de los números en el archivo.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Ingresa una url: ')    #Pedimos la URL
#Muestra: http://py4e-data.dr-chuck.net/comments_42.xml
#Real: http://py4e-data.dr-chuck.net/comments_1788967.xml
sumita = 0                          #Inicializamos variables numericas
cont = 0
url = urllib.request.urlopen(url, context=ctx)  #Abrimos la URL indicada

#Bucle para leer los caracteres
while True: 
    datos = url.read()
    if len(datos) < 1:                                  #Cuando no haya datos que leer salimos del bucle 
        break
    arbol = ET.fromstring(datos)                        #Convierte el xml en un arbol de nodos
    cosa = arbol.findall('comments/comment')            #creas los subarboles con 'findall'
    print('Recuperados', len(datos), 'caracteres')  

    for item in cosa:                                   #Para cada una de las etiquetas comment
        num = item.find('count').text                   #En el subarbol count(etiquetas), guardamos los numeros como int
        numerin = int(num)
        sumita += numerin                               #Para cada item leido actualizamos suma y cont
        cont += 1
      

#Al final mostramos la suma y el contador de etiquetas de la web xml
print('Cont:',cont)
print('Suma:',sumita)

