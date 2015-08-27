import sys

from gnomebgmanager import GnomeBgManager
from osxbgmanager import OsxBgManager

_platforms = dict(darwin=OsxBgManager())
bgmanager = _platforms.get(sys.platform, GnomeBgManager())
