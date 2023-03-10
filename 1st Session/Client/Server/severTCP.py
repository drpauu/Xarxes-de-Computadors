import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# bind the socket to a public host, and a well-known port
server_socket.bind((host, 7032))

# set the server to listen for incoming connections
server_socket.listen(1)

print('Waiting for incoming connections...')

# establish a connection with a client
client_socket, address = server_socket.accept()

print(f'Connection from {address} has been established!')

# send a message to the client
message = 'Thank you for connecting!'
client_socket.send(message.encode('utf-8'))

# close the connection
client_socket.close()
