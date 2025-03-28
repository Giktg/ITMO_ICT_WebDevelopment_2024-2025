import socket

HOST = '127.0.0.1'
PORT = 8082

def load_html():
    with open('index.html', 'r', encoding='utf-8') as file:
        return file.read()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Сервер запущен на {HOST}:{PORT}")

while True:
    # Принятие входящего соединения
    client_socket, addr = server_socket.accept()
    print(f"Подключение от {addr}\n\n")

    # Получение данных от клиента (HTTP-запрос)
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Запрос клиента:\n{request}")

    # Формирование HTTP-ответа
    response_body = load_html()
    response_headers = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    response = response_headers + response_body

    # Отправка HTTP-ответа клиенту
    client_socket.sendall(response.encode('utf-8'))

    # Закрытие соединения с клиентом
    print("Соединение закрыто\n")
