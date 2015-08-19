__author__ = 'trampfox'

from gi.repository import Gio
from conf import config

class GnomeBgManager:

  def __init__(self):
    self._gsettings = Gio.Settings.new(config.SCHEMA)

  def set_background(self, background_file):
    self._gsettings.set_string(
            config.KEY, background_file)