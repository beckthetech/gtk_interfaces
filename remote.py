from button_demo import ButtonWindow
from gi.repository import Gtk
import socket
import gi

gi.require_version('Gtk', '3.0')


# Creates a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connects the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f'connecting to {server_address[0]} port {server_address[1]}')
sock.connect(server_address)

try:
    win = ButtonWindow(sock)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
    # Sends data
    # message = {
    #     'message': 'This is the mssage. It will be repeated.',
    #     'count': win.count
    # }
    # data_string = json.dumps(message)
    # print(f'sending "{data_string}"')
    # sock.sendall(data_string.encode())

finally:
    print('closing socket')
    sock.close()
