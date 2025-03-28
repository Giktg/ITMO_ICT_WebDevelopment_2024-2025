import socket
import threading

HOST = '127.0.0.1'
PORT = 8080
clients = []


def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            break
    client_socket.close()
    clients.remove(client_socket)


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Сервер запущен на {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключение от {client_address}")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()


if __name__ == "__main__":
    start_server()
