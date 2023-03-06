import socket
import threading
"Importamos las bibliotecas socket y threading."

def send_messages():
    while True:
        message = input("")
        for client_socket in client_sockets:
            client_socket.send(message.encode())

"""La función send_messages() se ejecuta en un hilo dedicado y es responsable 
de enviar mensajes a todos los clientes conectados. Cada vez que se ingresa 
un mensaje desde la consola, el mensaje se codifica en bytes y se envía a 
cada uno de los sockets de los clientes almacenados en la lista client_sockets."""

def receive_messages(client_socket, client_address):
    while True:
        message = client_socket.recv(1024).decode()
        print(client_address[0] + ":" +
              str(client_address[1]) + " > " + message)


"""La función receive_messages() se ejecuta en un hilo dedicado para cada cliente
y es responsable de recibir mensajes entrantes. Cada vez que se recibe un mensaje,
se decodifica en una cadena de caracteres y se muestra en la consola junto con la 
dirección IP y el puerto del remitente."""

def connect():
    host = socket.gethostname()
    port = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print("Server started.")

    while True:
        client_socket, client_address = s.accept()
        print("Connected by:", client_address)
        client_sockets.append(client_socket)
        thread = threading.Thread(
            target=receive_messages, args=(client_socket, client_address))
        thread.start()


"""La función connect() es responsable de configurar el servidor para escuchar 
conexiones entrantes de los clientes. En primer lugar, se obtiene el nombre de host
y se define el puerto en el que se escucharán las conexiones entrantes. A continuación,
se crea un objeto de socket TCP y se enlaza al host y puerto definidos. Luego, el servidor
comienza a escuchar conexiones entrantes y muestra un mensaje en la consola para indicar
que el servidor se ha iniciado correctamente.

Dentro del bucle infinito de la función connect(), se aceptan conexiones entrantes y se
almacena cada socket del cliente en la lista client_sockets. Luego, se inicia un nuevo 
hilo para manejar la comunicación con el cliente utilizando la función receive_messages()."""

if __name__ == '__main__':
    client_sockets = []
    thread = threading.Thread(target=send_messages)
    thread.start()
    connect()

"""Finalmente, en la sección principal del programa, se inicializa la lista client_sockets
y se inicia un hilo para enviar mensajes utilizando la función send_messages(). Luego, se
llama a la función connect() para configurar y ejecutar el servidor."""
