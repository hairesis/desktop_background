from gi.repository import Gio

SCHEMA = 'org.gnome.desktop.background'
KEY = 'picture-uri'


class GnomeBgManager:
    def __init__(self):
        self._gsettings = Gio.Settings.new(SCHEMA)

    def set_background(self, background_file):
        self._gsettings.set_string(KEY, background_file)
