from conf import config
from conf import images

import urllib
import os
import random


def download_image(img_file):
    urllib.urlretrieve(
        config.BASE_URL % img_file, config.CACHE_PATH % img_file)


def get_random_image():
    img_file = config.IMG % random.choice(images.image_ids)
    if not os.path.isfile(config.CACHE_PATH % img_file):
        download_image(img_file)
    return img_file


def get_image():
    return config.BASE_PATH % config.CACHE_PATH % get_random_image()
