import socket  # Importamos el socket

# SIEMPRE ASÍ ESTAS LÍNEAS
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
misock.send(cmd)

# Hacemos un bucle para extraer los datos si los hay
while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(), end=" ")

misock.close()
