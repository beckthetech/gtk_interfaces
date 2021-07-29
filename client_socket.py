import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
# print >>sys.stderr, 'connecting to %s port %s' % server_address
print(f'connecting to {server_address[0]} port {server_address[1]}')
sock.connect(server_address)

try:
    # Send data
    message = 'This is the mssage. It will be repeated.'
    # print >>sys.stderr, 'sending "%s"' % message
    print(f'sending "{message}"')
    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        # print >>sys.stderr, 'received "%s"' % data
        print(f'received "{data}"')

finally:
    # print >>sys.stderr, 'closing socket'
    print('closing socket')
    sock.close()
