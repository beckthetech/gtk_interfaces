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

        self.port_entry = Gtk.Entry()
        self.port_entry.set_text('54321')
        box.add(self.port_entry)

        get_ip_entry = Gtk.Button.new_with_label('Get IP')
        get_ip_entry.connect('clicked', self.on_get_ip_entry)
        box.add(get_ip_entry)

        get_port_entry = Gtk.Button.new_with_label('Get Port')
        get_port_entry.connect('clicked', self.on_get_port_entry)
        box.add(get_port_entry)

    def on_get_ip_entry(self, button):
        print(self.ip_entry.get_text())

    def on_get_port_entry(self, button):
        print(self.port_entry.get_text())


win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
