#!/bin/python

from conf import config
from conf import images
from gnomebgmanager import GnomeBgManager
from osxbgmanager import OsxBgManager

import urllib
import os
import random
import sys

if sys.platform == "darwin":
    bgmanager = OsxBgManager()
else:
    bgmanager = GnomeBgManager()


def download_image(img_file):
    urllib.urlretrieve(
        config.BASE_URL % img_file, config.CACHE_PATH % img_file)


def get_random_image():
    img_file = config.IMG % random.choice(images.image_ids)
    if not os.path.isfile(config.CACHE_PATH % img_file):
        download_image(img_file)
    return img_file


def set_background():
    background_file = config.BASE_PATH % config.CACHE_PATH % get_random_image()
    bgmanager.set_background(background_file)

if __name__ == '__main__':
    set_background()
