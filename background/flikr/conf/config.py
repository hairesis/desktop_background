API_KEY = '5f28264895e573c4b78c7fe6d81ce459'

BASE_API_URL = 'https://api.flickr.com/services/rest/?method={0}&api_key={1}&extras={2}&media=photo&page=1&format=json&nojsoncallback=1&text={3}&page={4}&date={5}'
PLUGIN_NAME = 'desktop_background:flykr'

MIN_WIDTH = 1920
MIN_HEIGHT = 1080
MIN_VIEWS = 1000

EXTRAS = ['original_format', 'views', 'o_dims', 'url_o']


CACHE_PATH = "/tmp/%s"

BASE_PATH = 'file://%s'
IMG = "%s.jpg"
