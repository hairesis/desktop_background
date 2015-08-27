#!/usr/bin/env python

from background.earth import get_image
from background.managers import bgmanager


def set_background():
    bgmanager.set_background(get_image())

if __name__ == '__main__':
    set_background()
