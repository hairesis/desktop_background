from background.earth import get_random_image, get_image


def test_get_random_image():
    img1 = get_random_image()
    img2 = get_random_image()
    assert img1 != img2


def test_the_returned_image_is_well_formed():
    img = get_image()
    assert img.startswith('file://') and img.endswith('.jpg')
