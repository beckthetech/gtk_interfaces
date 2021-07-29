import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
# print >>sys.stderr, 'starting up on %s port %s'
print(f'starting up on {server_address[0]} port {server_address[1]}')
sock.bind(server_address)

sock.listen(1)

while True:
    # Wait for a connection
    # print >>sys.stderr, 'waiting for a connection'
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        # print >>sys.stderr, 'connection from', client_address
        print(f'connection from {client_address}')

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            # print >>sys.stderr, 'received "%s"' % data
            print(f'received "{data}"')
            if data:
                # print >>sys.stderr, 'sending data back to the client'
                print(f'sending data back to the client')
                connection.sendall(data)
            else:
                # print >>sys.stderr, 'no more data from', client_address
                print(f'no more data from {client_address}')
                break
    finally:
        # Clean up the connection
        connection.close()
