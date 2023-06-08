#Programa para introducir una ubicacion en Geo Google y devolver el identificador del sitio PLACE ID

import urllib.request, urllib.parse, urllib.error
import json
import ssl

#Clave API y url de servicio
clave_api = 42
url_de_servicio = 'http://py4e-data.dr-chuck.net/json?'

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    direccion = input('Ingresa una ubicación: ')        #Ingresar una ubicacion no vacía
    if len(direccion) < 1: break

    ubi = dict()                                       #Crear un diccionario para apuntar direccion introducida y API,
    ubi['address'] = direccion                         #luego gracias a parse y urlencode la url es la buena para acceder
    if clave_api is not False: ubi['key'] = clave_api  #Parrafo siempre asi para rascar de Google Geocode, si no ERROR
    url = url_de_servicio + urllib.parse.urlencode(ubi)

    print('Recuperando', url)
    archivo = urllib.request.urlopen(url, context=ctx)  #Abrir la web y leer todos los datos en json
    datos = archivo.read().decode()
    print('Recuperados', len(datos), 'caracteres')      #Mostrar la longitud de los datos leidos caracter a caracter

    try:
        js = json.loads(datos)                          #Puede dar error y mejor salir de manera elegante
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':    #Hay un campo de estatus que debe estar OK
        print('==== Error al Recuperar ====')
        continue

    p_id = js['results'][0]['place_id']                   #Solo nos interesa el place_id asi que lo mostramos
    print('Identificacion del lugar',p_id)