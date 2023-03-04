import socket

# create a socket object
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set the server address and port
server_address = ('localhost', 5000)
message = b'Hello, server. This is the client.'

try:
    # send data
    print('Sending {!r}'.format(message))
    sent = udp_client_socket.sendto(message, server_address)

    # receive response
    print('Waiting to receive response')
    data, server = udp_client_socket.recvfrom(4096)
    print('Received {!r}'.format(data))

finally:
    print('Closing socket')
    udp_client_socket.close()
