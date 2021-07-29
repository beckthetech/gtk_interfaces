import socket
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f'connecting to {server_address[0]} port {server_address[1]}')
sock.connect(server_address)

try:
    # Send data
    message = {'message': 'This is the mssage. It will be repeated.'}
    data_string = json.dumps(message)
    print(f'sending "{data_string}"')
    sock.sendall(data_string.encode())

finally:
    print('closing socket')
    sock.close()
