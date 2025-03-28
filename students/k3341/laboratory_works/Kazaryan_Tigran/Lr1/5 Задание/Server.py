import socket
from urllib.parse import parse_qs

# Хранилище для оценок
grades = {}


def handle_get_request(conn):
    # Формируем HTML-страницу с оценками
    html_content = """
    <html>
        <head>
            <meta charset="UTF-8">
            <title>Оценки по дисциплинам</title>
        </head>
        <body>
            <h1>Оценки по дисциплинам</h1>
            <table border="1">
                <tr>
                    <th>Дисциплина</th>
                    <th>Оценка</th>
                </tr>
    """

    for subject, grade in grades.items():
        html_content += f"""
                <tr>
                    <td>{subject}</td>
                    <td>{grade}</td>
                </tr>
        """

    html_content += """
            </table>
        </body>
    </html>
    """

    # Отправляем HTTP-ответ
    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: {len(html_content)}\r\n\r\n{html_content}"
    conn.send(response.encode('utf-8'))


def handle_post_request(conn, data):
    # Парсим данные из POST запроса
    post_data = parse_qs(data.decode('utf-8'))
    subject = post_data.get('subject', [''])[0]
    grade = post_data.get('grade', [''])[0]

    if subject and grade:
        grades[subject] = grade
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=UTF-8\r\n\r\nДанные успешно добавлены"
    else:
        response = "HTTP/1.1 400 Bad Request\r\nContent-Type: text/plain; charset=UTF-8\r\n\r\nНеверные данные"

    conn.send(response.encode('utf-8'))


def handle_request(conn):
    request = conn.recv(1024).decode('utf-8')
    headers = request.split('\r\n')
    method = headers[0].split(' ')[0]

    if method == 'GET':
        handle_get_request(conn)
    elif method == 'POST':
        # Получаем тело POST запроса
        body = request.split('\r\n\r\n')[1]
        handle_post_request(conn, body.encode('utf-8'))
    else:
        response = "HTTP/1.1 405 Method Not Allowed\r\nContent-Type: text/plain; charset=UTF-8\r\n\r\nМетод не поддерживается"
        conn.send(response.encode('utf-8'))


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
    print("Сервер запущен на http://localhost:8080")

    while True:
        conn, addr = server_socket.accept()
        print(f"Подключение от {addr}")
        handle_request(conn)
        conn.close()


if __name__ == "__main__":
    start_server()