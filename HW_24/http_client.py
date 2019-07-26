import socket
import sys

host = '10.0.3.15'
port = 80

# Создаю сокет
print('# Create socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()


# Подключение к серверу
print('# Connecting to server, ' + host)
s.connect((host, port))

# Отправка запроса
print('# Send request to server')
request = "GET / HTTP/1.0\r\n\r\n"

try:
    s.sendall(request)
except socket.error:
    print('Send failed')
    sys.exit()

# Получение данных
print('Receive data')
reply = s.recv(4096)

print(reply)

