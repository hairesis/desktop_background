import sys
import os
from setuptools import find_packages, setup

config = {
    'description': 'Change your desktop background with awesome images',
    'author': 'Andrea Baglioni, Davide Monfrecola',
    'author_email': '0x41ndrea@gmail.com',
    'version': '1',
    'packages': find_packages(),
    'scripts': ['eb.py'],
    'name': 'desktop_background'
}

setup(**config)
