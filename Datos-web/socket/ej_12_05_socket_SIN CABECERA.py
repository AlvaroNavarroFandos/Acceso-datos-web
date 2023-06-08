#Programa para solo mostrar los datos sin la cabecera con el metodo socket

import socket  # Importamos el socket

# SIEMPRE ASÍ ESTAS LÍNEAS
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
misock.send(cmd)

datos = b""
# Hacemos un bucle para extraer los datos si los hay
while True:
    datos = misock.recv(1024)
    if len(datos) < 1:
        break

    # Verificar si se ha recibido la línea en blanco y Mostrar los datos después de la línea en blanco
    if b"\r\n\r\n" in datos:
        datos = datos.split(b"\r\n\r\n", 1)[1] #Divide todo lo recibido en 2 partes con la línea en blanco en medio
                                                #el ,1 es porque solo se hace una division y el [1] porque mostrara solo
                                                #la segunda parte, lo de despues de la linea en blanco
           
        print(datos.decode(), end='')

misock.close()