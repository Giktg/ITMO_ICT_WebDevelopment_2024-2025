import socket

base = float(input("Введите значение основания параллелограмма: "))
height = float(input("Введите значение высоты параллелограмма: "))

# Настраиваем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Подключаем сокет к порту и адресу
client_socket.connect(('localhost', 8090))
# Отправляем данные о размер параллелограмма серверу
client_socket.send(f'{base},{height}'.encode())
# Декодируем полученное сообщение от сервера и записываем его в переменную
response = client_socket.recv(1024).decode()

print(f'Ответ от сервера: {response}')

# Закрываем соединение
client_socket.close()
