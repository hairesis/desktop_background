#!/bin/python

from conf import config
from conf import images
import urllib
import os
import random
import sys

if sys.platform == "darwin":
    import subprocess
    SCRIPT = """/usr/bin/osascript<<END
    tell application "Finder"
    set desktop picture to POSIX file "%s"
    end tell
    END"""
else:
    from gi.repository import Gio
    _gsettings = Gio.Settings.new(config.SCHEMA)


BASE_PATH = 'file://%s'
IMG = "%s.jpg"


def download_image(img_file):
    urllib.urlretrieve(
        config.BASE_URL % img_file, config.CACHE_PATH % img_file)


def get_random_image():
    img_file = IMG % random.choice(images.image_ids)
    if not os.path.isfile(config.CACHE_PATH % img_file):
        download_image(img_file)
    return img_file


def set_background():
    background_file = BASE_PATH % config.CACHE_PATH % get_random_image()

    if sys.platform == "darwin":
        subprocess.Popen(SCRIPT % background_file, shell=True)
    else:
        _gsettings.set_string(
            config.KEY, background_file)


if __name__ == '__main__':
    set_background()
