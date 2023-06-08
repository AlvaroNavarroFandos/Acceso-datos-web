# Escribir un programa que pida al usuario la URL que quiera para que pueda leer cualquier web
import socket  # Importamos el socket

URL_completa = input("Introduzca la URL: ")
# Por si el usuario mete mal la URL
try:
    puerto = 80
    URL = URL_completa.split("/")
    host = URL[2]
    print(URL)
    # http://data.pr4e.org/romeo.txt
    # SIEMPRE ASÍ ESTAS LÍNEAS
    misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    misock.connect((host, puerto))
    cmd = (("GET "+URL_completa+" HTTP/1.0\r\n\r\n").encode())
    misock.send(cmd)
except:
    print("URL incorrecta: ", URL_completa)
    exit()

# Hacemos un bucle para extraer los datos si los hay
while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(), end=" ")

misock.close()
