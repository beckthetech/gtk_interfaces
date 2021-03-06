import socket

# Creates a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binds the socket to the port
server_address = ('localhost', 10000)
print(f'starting up on {server_address[0]} port {server_address[1]}')
sock.bind(server_address)

sock.listen(1)

while True:
    # Waits for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print(f'connection from {client_address}')

        # Receives the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print(f'received "{data}"')
            if data:
                print(f'sending data back to the client')
                connection.sendall(data)
            else:
                print(f'no more data from {client_address}')
                break
    finally:
        # Cleans up the connection
        connection.close()
