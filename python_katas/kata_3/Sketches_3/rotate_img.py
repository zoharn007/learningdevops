ISO_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


def rotate_img(img_filename):
    """
    3 Kata

    Rotates image clockwise

    :param img_filename: image file path (png or jpeg)
    :return: None, the rotated image should be saved as 'rotated_<original image filename>'
    """
    image = open_img(img_filename)

    pass  # use rotate_matrix from previous kata 2 or implement....

    # use the below line to save list as image
    # save_img(rotated_img, f'rotated_{img_filename}')