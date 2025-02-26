import socket

def calculate_area(base, height):
    return base * height

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8090))
server_socket.listen(5)

print("Сервер работает и ждёт...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Подключен клиент {client_address}')

    client_data = client_socket.recv(1024).decode()

    base, height = map(float, client_data.split(','))
    result = calculate_area(base, height)
    client_socket.send(f'Площадь параллелограмма: {result}'.encode())
    client_socket.close()