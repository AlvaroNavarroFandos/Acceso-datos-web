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

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

#Ejemplo codigo JSON Broto (para ver el codigo)

# {
#     "results": [
#         {
#             "address_components": [
#                 {
#                     "long_name": "Broto",
#                     "short_name": "Broto",
#                     "types": [
#                         "locality",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Huesca",
#                     "short_name": "HU",
#                     "types": [
#                         "administrative_area_level_2",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Aragon",
#                     "short_name": "AR",
#                     "types": [
#                         "administrative_area_level_1",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Spain",
#                     "short_name": "ES",
#                     "types": [
#                         "country",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "22370",
#                     "short_name": "22370",
#                     "types": [
#                         "postal_code"
#                     ]
#                 }
#             ],
#             "formatted_address": "22370 Broto, Huesca, Spain",
#             "geometry": {
#                 "bounds": {
#                     "northeast": {
#                         "lat": 42.6068768,
#                         "lng": -0.1175057
#                     },
#                     "southwest": {
#                         "lat": 42.5969686,
#                         "lng": -0.1250208
#                     }
#                 },
#                 "location": {
#                     "lat": 42.6047671,
#                     "lng": -0.1233353
#                 },
#                 "location_type": "APPROXIMATE",
#                 "viewport": {
#                     "northeast": {
#                         "lat": 42.6068768,
#                         "lng": -0.1175057
#                     },
#                     "southwest": {
#                         "lat": 42.5969686,
#                         "lng": -0.1250208
#                     }
#                 }
#             },
#             "place_id": "ChIJz1SYQ7v5Vw0RkR_jV9rMlCg",
#             "types": [
#                 "locality",
#                 "political"
#             ]
#         }
#     ],
#     "status": "OK"
# }