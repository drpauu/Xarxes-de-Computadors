import socket

# create a socket object
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set the server address and port
server_address = ('localhost', 5000)
print('Starting up on {} port {}'.format(*server_address))
udp_server_socket.bind(server_address)

while True:
    print('\nWaiting to receive message')
    data, address = udp_server_socket.recvfrom(4096)
    
    print('Received {} bytes from {}'.format(len(data), address))
    print(data)
    
    # send a response back to the client
    message = b'ACK: ' + data
    udp_server_socket.sendto(message, address)
