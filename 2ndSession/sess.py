import socket
import threading


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen()

    print('Chat room started.')

    while True:
        client_socket, address = server_socket.accept()
        print(f'Connection established from {address[0]}:{address[1]}')
        recv_thread = threading.Thread(
            target=receive_messages, args=(client_socket, address))
        recv_thread.start()


def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode()
        print(message)

    client_socket.close()
    print('Connection closed.')


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print('Connected to chat room.')

    recv_thread = threading.Thread(
        target=receive_messages, args=(client_socket,))
    recv_thread.start()

    while True:
        message = input()
        client_socket.sendall(message.encode())
