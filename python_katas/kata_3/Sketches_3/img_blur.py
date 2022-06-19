ISO_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


def img_blur(img_filename):
    """
    4 Kata

    Blurs an image (every pixel is an average of its nearest neighbors)

    :param img_filename: image file path (png or jpeg)
    :return: None, the rotated image should be saved as 'rotated_<original image filename>'
    """
    image = open_img(img_filename)

    pass  # use matrix_avg from previous kata 2 or implement....

    # use the below line to save list as image
    # save_img(blured_img, f'blured_{img_filename}')