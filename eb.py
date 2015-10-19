#!/usr/bin/env python

import logging
import importlib
from background.managers import bgmanager

logging.basicConfig()

logger = logging.getLogger('desktop_background:main')
logger.setLevel(logging.INFO)

__version__ = '1-flikr'


def get_plugin(name='earth'):
    return importlib.import_module('background.%s' % name)

plugin = get_plugin()


def _parse_arguments():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source',
                        nargs='?', default='earth',
                        type=str, help='flikr earth')
    args = parser.parse_args()
    return args.source


def set_background():
    bgmanager.set_background(plugin.get_image())


if __name__ == '__main__':
    plugin_name = _parse_arguments() or 'earth'
    try:
        logger.info(
            "chnging desktop background using '%s' plugin" % plugin_name)
        plugin = get_plugin(plugin_name)
    except ImportError as ex:
        logger.warning(
            "No '%s' plugin found, fallback to default: 'earth'" % plugin_name)
    set_background()
