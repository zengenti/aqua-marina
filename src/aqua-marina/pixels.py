"""Images are stored as `numpy` multidimensional arrays.

This will definitely come in handy and avoid the need to mess about directly with the
images.
"""

import imageio.v3 as iio

import ipympl
from matplotlib import pyplot
import numpy as np
import skimage as ski


eight = iio.imread(uri='../data/raw/training/eight.tif')
print(type(eight))

fig, ax = pyplot.subplots()
ax.imshow(eight)

print(eight.shape)
print(eight)


