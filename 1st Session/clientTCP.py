import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# connect to the server on a specific port
client_socket.connect((host, 8000))

# receive the message sent by the server
message = client_socket.recv(1024).decode('utf-8')
print(message)

# close the connection
client_socket.close()
