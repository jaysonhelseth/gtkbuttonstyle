import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
from gi.repository import Gdk, Gtk


class Handler:
    def on_destroy(self, *args):
        Gtk.main_quit()


def set_style_sheet():
    provider = Gtk.CssProvider()
    provider.load_from_path("theming.css")
    screen = Gdk.Display.get_default_screen(Gdk.Display.get_default())
    priority = 600
    Gtk.StyleContext.add_provider_for_screen(screen, provider, priority)


def main():
    set_style_sheet()
    builder = Gtk.Builder()
    builder.add_from_file("layout.glade")
    builder.connect_signals(Handler())

    window = builder.get_object("app_window")
    window.show_all()

    Gtk.main()


if __name__ == '__main__':
    main()
