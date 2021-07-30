import gi
import json

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ButtonWindow(Gtk.Window):
    count = 1

    def __init__(self, sock):
        super().__init__(title='Button Demo')
        self.set_border_width(10)
        self.sock = sock
        self.count = 1

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        new_button = Gtk.Button.new_with_label

        button = new_button('send')
        button.connect('clicked', self.on_send_clicked)
        hbox.pack_start(button, True, True, 0)

        button = new_button('Count Up by 1')
        button.connect('clicked', self.on_count_up_clicked)
        hbox.pack_start(button, True, True, 0)

        button = new_button('Close')
        button.connect('clicked', self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_send_clicked(self, button):
        print('"Send" button was clicked')
        message = {
            'count data': self.count
        }
        data_string = json.dumps(message)
        print(f'sending "{data_string}"')
        try:
            self.sock.sendall(data_string.encode())
        except:
            pass
            print('socket exception')

    def on_count_up_clicked(self, button):
        self.count += 1
        print(self.count)

    def on_close_clicked(self, button):
        print('Closing application')
        self.sock.close()
        Gtk.main_quit()