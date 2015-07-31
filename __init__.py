import config
import images
import urllib
import os
import random

from gi.repository import Gio

## TODO: support osx
## http://stackoverflow.com/questions/431205/how-can-i-programatically-change-the-background-in-mac-os-x

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
    _gsettings.set_string(
        config.KEY, BASE_PATH % config.CACHE_PATH % get_random_image())


if __name__ == '__main__':
    set_background()
