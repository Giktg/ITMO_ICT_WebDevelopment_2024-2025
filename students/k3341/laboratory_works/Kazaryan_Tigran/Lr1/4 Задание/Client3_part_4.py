import socket
import threading

HOST = '127.0.0.1'
PORT = 8080

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(message)
        except:
            print("Отключено от сервера")
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Вы подключены к чату! Введите сообщение и нажмите Enter.")

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

while True:
    message = input()
    if message.lower() == "exit":
        break
    client_socket.send(message.encode("utf-8"))

client_socket.close()
