import urllib.request, urllib.parse, urllib.error
import json
import ssl

clave_api = 42
url_de_servicio = 'http://py4e-data.dr-chuck.net/json?'


# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    direccion = input('Ingresa una ubicación: ')
    if len(direccion) < 1: break

    ubi = dict()
    ubi['address'] = direccion
    if clave_api is not False: ubi['key'] = clave_api
    url = url_de_servicio + urllib.parse.urlencode(ubi)

    print('Recuperando', url)
    uh = urllib.request.urlopen(url, context=ctx)
    datos = uh.read().decode()
    print('Recuperados', len(datos), 'caracteres')

    try:
        js = json.loads(datos)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Error al Recuperar ====')
        print(datos)
        continue

    print(json.dumps(js, indent=4))

    if (js['results'][0]['address_components'][0]['types'][0]) == 'locality':   
        pais_short = js['results'][0]['address_components'][-1]['short_name']
        print('Id País:',pais_short)
        
    else:
        print('No tiene patria') 