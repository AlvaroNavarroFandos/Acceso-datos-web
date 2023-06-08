import time
import socket

SERVIDOR = "data.pr4e.org"
PUERTO = 80
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect((SERVIDOR, PUERTO))
misock.sendall(b"GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n")
contador = 0
total = 0
imagen = b""

while contador<3000:
    datos = misock.recv(500)
    if len(datos) < 1:
        break
    contador += len(datos)
    imagen += datos
    
print('STOP THE COUNT',contador,'\n\n')    
    
while len(datos) >= 1:
    datos = misock.recv(1024)
    total += len(datos)
    imagen += datos


misock.close()

# Búsqueda del final de la cabecera (2 CRLF)
pos = imagen.find(b"\r\n\r\n")
print("Header length", pos)
print(imagen[:pos].decode())

# Ignorar la cabera y guardar los datos de la imagen
imagen = imagen[pos + 4 :]
fhand = open("cosa.jpg", "wb")
fhand.write(imagen)
fhand.close()

print('Número total de carácteres recibidos: ',total+contador)