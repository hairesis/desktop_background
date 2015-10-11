#!/usr/bin/env python

from background.flikr import get_image
from background.managers import bgmanager

__version__ = '1-earth'


def set_background():
    bgmanager.set_background(get_image())

if __name__ == '__main__':
    set_background()
