import socket
import threading


def send_messages(message, destination):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    """Definimos una función send_messages que toma dos argumentos:
    message que es el mensaje que se desea enviar, y destination que
    es la dirección IP y el puerto del destinatario. Se crea un socket
    UDP usando socket.socket con la familia de direcciones IP AF_INET
    y el tipo de socket SOCK_DGRAM."""
    s.sendto(message.encode(), destination)
    s.close()
    """Enviamos el mensaje a la dirección del destinatario usando sendto(),
    que toma dos argumentos: el mensaje codificado en bytes y la dirección
    del destinatario. Luego cerramos el socket usando close()."""


def receive_messages():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", 5000))
    """Definimos una función receive_messages que crea un socket UDP usando
    socket.socket con la familia de direcciones IP AF_INET y el tipo de socket
    SOCK_DGRAM. Luego vinculamos el socket a una dirección IP y un puerto usando bind().
    La dirección IP en este caso es "", lo que significa que el socket escuchará en todas
    las interfaces de red."""
    while True:
        message, address = s.recvfrom(1024)
        print(address[0] + ":" + str(address[1]) + " > " + message.decode())


"""En un bucle infinito, el socket espera a recibir mensajes. Cuando un mensaje es recibido,
recvfrom() devuelve dos valores: el mensaje recibido y la dirección del remitente. 
El mensaje se decodifica en una cadena usando decode(), y se imprime junto con la dirección
del remitente."""

def connect():
    thread = threading.Thread(target=receive_messages)
    thread.start()
    """Definimos una función connect() que inicia un hilo que ejecuta la función 
    receive_messages."""
    while True:
        message = input("")
        destination = (socket.gethostname(), 5000)
        thread = threading.Thread(
            target=send_messages, args=(message, destination))
        thread.start()
    
    """En un bucle infinito, el usuario ingresa un mensaje desde la consola. 
    Luego se crea una tupla destination que contiene la dirección IP y el puerto 
    del destinatario, y se inicia un hilo que ejecuta la función send_messages con 
    los argumentos message y destination."""

if __name__ == '__main__':
    connect()
"""Finalmente, verificamos si el módulo está siendo ejecutado directamente 
(es decir, no siendo importado por otro módulo), y si es así, 
ejecutamos la función connect()."""
