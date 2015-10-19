import os
import requests
import operator
import ujson
import urllib
import random
import logging
from decimal import Decimal

from datetime import datetime
from conf import config

logging.basicConfig()

logger = logging.getLogger(config.PLUGIN_NAME)
logger.setLevel(logging.INFO)


class PhotoSizeMissing(Exception):
    pass


class DownloadPageError(Exception):
    pass


def _has_original_url(photo):
    return photo.get('url_o') is not None


def _get_photo_size(photo):
    w = photo.get('width_o')
    h = photo.get('height_o')
    if None not in (w, h):
        return (int(w), int(h))
    raise PhotoSizeMissing()


def _is_landscape(photo):
    w, h = _get_photo_size(photo)
    return w > h


def _16_9_aspect_ratio(photo):
    d_w = Decimal(16)
    d_h = Decimal(9)
    w, h = tuple(map(lambda x: Decimal(x), _get_photo_size(photo)))
    return w/h == d_w/d_h


def _has_valid_resolution(photo):
    w, h = _get_photo_size(photo)
    return w >= config.MIN_WIDTH and h >= config.MIN_HEIGHT


def _is_popular(photo):
    v = photo.get('views')
    if v is not None:
        logger.debug('picture %s: views: %s' % (photo.get('id'), v))
        return int(v) > config.MIN_VIEWS
    return False


photo_quality = [
    _has_original_url,
    _is_landscape,
    #_16_9_aspect_ratio,
    _has_valid_resolution,
    _is_popular
]


def next_page_of_photos(search_text, page):
    d = datetime.now()
    api_url = config.BASE_API_URL.format('flickr.interestingness.getList',
                                         config.API_KEY,
                                         ','.join(config.EXTRAS),
                                         search_text,
                                         str(page),
                                         '%d-%d-%d' % (d.year, d.month, d.day - 1))
    resp = requests.get(api_url)
    if resp.status_code != 200:
        raise DownloadPageError('HTTP response error: %d', resp.status_code)

    j_resp = resp.json()
    if j_resp.get('stat', 'fail') == 'fail':
        raise DownloadPageError('no images found or wrong API request')
    return j_resp['photos']['photo']


def download_image(photo):
    if not os.path.isfile(config.CACHE_PATH % config.IMG % photo.get('id')):
        urllib.urlretrieve(
            photo.get('url_o'), config.CACHE_PATH % config.IMG % photo.get('id'))


def get_random_image(search_text='landscape'):
    page = 1
    valid_photos = []
    while(len(valid_photos) < 50):
        for photo in next_page_of_photos(search_text, page):
            try:
                is_valid_photo = reduce(
                    operator.and_, [check(photo) for check in photo_quality])
                if is_valid_photo:
                    valid_photos.append(photo)
                    logger.debug('Found image: %s' % ujson.dumps(photo))
            except PhotoSizeMissing:
                pass
        logger.debug('No photo in page %d mathces the criteria' % page)
        page += 1
    photo = random.choice(valid_photos)
    download_image(photo)
    return config.IMG % photo.get('id')


def get_image():
    return config.BASE_PATH % config.CACHE_PATH % get_random_image()

if __name__ == '__main__':
    try:
        print(get_image())
    except DownloadPageError as e:
        logger.error(str(e))
