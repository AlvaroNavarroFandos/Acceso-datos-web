#Programa que al introducir una URL extrae los datos en 'json' y guarda los numeros de los comments y hace la suma
# AL SOLO QUERER EL COUNT, SERA UNA LISTA DE ENTEROS (DEFINIR LA LISTA PRIMERO), SI QUISIERA MAS COSAS SERIA UN DICCIONARIO
#Importamos las librerias necesarias
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#PRUEBA: http://py4e-data.dr-chuck.net/comments_42.json
#REAL:  http://py4e-data.dr-chuck.net/comments_1788968.json

#Inicializamos las variables
suma = 0
cont = 0

url = input('Ingresa una URL: ')                    #Introducimos la URL y miramos que no esté vacia
print('Recuperando',url)

try:
    archivo = urllib.request.urlopen(url, context=ctx)   #Accedemos a la web
    datos = archivo.read().decode()                     #Leemos y descodificamos los datos
    print(len(datos),'carácteres recuperados')          #Mostramos los caracteres recuperados del json en la web
    info = json.loads(datos)                            #Cargamos el json para crear una lista o diccionario
except:
    print('error')
    quit()  
    
comentarios = info['comments']  #OBTENEMOS LA LISTA DE COMENTARIOS, SI NO NO VA A IMPRIMIR NADA!!!!!!!!!!

for item in comentarios:                       #Para todos los items de la lista, cogemos los counts y sumamos
    numerin = item['count']
    suma += numerin
    cont += 1

#Mostramos el resultado de la salida requerida por pantalla
print('Cont:', cont)
print('Suma:',suma)
     
    