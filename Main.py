import socket
import gi

from gi.repository import Gtk
gi.require_version("Gtk", "3.0")


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Remote UI")

        box = Gtk.Box()
        self.add(box)

        self.ip_entry = Gtk.Entry()
        self.ip_entry.set_text('169.254.123.123')
        box.add(self.ip_entry)
        TCP_IP = self.ip_entry.get_text()

        self.port_entry = Gtk.Entry()
        self.port_entry.set_text('54321')
        box.add(self.port_entry)
        TCP_PORT = self.port_entry.get_text()

        self.test_entry = Gtk.Entry()
        self.test_entry.set_text('Enter text...')
        box.add(self.test_entry)

        get_ip_entry = Gtk.Button.new_with_label('Get IP')
        get_ip_entry.connect('clicked', self.on_get_ip_entry)
        box.add(get_ip_entry)

        get_port_entry = Gtk.Button.new_with_label('Get Port')
        get_port_entry.connect('clicked', self.on_get_port_entry)
        box.add(get_port_entry)

        get_text_entry = Gtk.Button.new_with_label('Get test entry')
        get_text_entry.connect('clicked', self.on_get_test_entry)
        box.add(get_text_entry)

        BUFFER_SIZE = 1024
        MESSAGE = self.test_entry.get_text()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE)
        data = s.recv(BUFFER_SIZE)
        s.close()

    def on_get_ip_entry(self, button):
        print(self.ip_entry.get_text())

    def on_get_port_entry(self, button):
        print(self.port_entry.get_text())

    def on_get_test_entry(self, button):
        print(self.test_entry.get_text())


win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
