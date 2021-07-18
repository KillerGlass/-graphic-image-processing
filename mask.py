import numpy as np


def createMask(coords, img):
    """
    this method receives a list containing the coordinates of an image,
    and returns an image with the Bounding Boxes.

    PARAMETERS
    ==========
    coords : list
        list with object's coordinates.

    img : np.array
        image base.

    """
    shape = img.shape

    mask = np.zeros([shape[0], shape[1], shape[2]], dtype=int).astype(np.uint8)

    for dot in coords:
        xmin = dot['xmin']
        ymin = dot['ymin']
        xmax = dot['xmax']
        ymax = dot['ymax']
        
        mask[ymin: ymax + 1, xmin:xmax + 1, :] = 255

    return mask
