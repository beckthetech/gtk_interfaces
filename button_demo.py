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

        button = new_button('Click Me')
        button.connect('clicked', self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = new_button('Open')
        button.connect('clicked', self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)

        button = new_button('Test')
        button.connect('clicked', self.on_test_clicked)
        hbox.pack_start(button, True, True, 0)

        button = new_button('Count Up by 1')
        button.connect('clicked', self.on_count_up_clicked)
        hbox.pack_start(button, True, True, 0)

        button = new_button('Close')
        button.connect('clicked', self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_click_me_clicked(self, button):
        print('"Click" me button was clicked')
        message = {
            'message': 'This is the mssage.',
            'count': self.count
        }
        data_string = json.dumps(message)
        print(f'sending "{data_string}"')
        self.sock.sendall(data_string.encode())

    def on_open_clicked(self, button):
        print('"Open" button was clicked')

    def on_test_clicked(self, button):
        print('"Test" button was clicked')

    def on_count_up_clicked(self, button):
        print(self.count)
        self.count += 1

    def on_close_clicked(self, button):
        print('Closing application')
        self.sock.close()
        Gtk.main_quit()


# win = ButtonWindow()
# win.connect("destroy", Gtk.main_quit)
# win.show_all()
# Gtk.main()
