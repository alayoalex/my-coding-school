from __future__ import print_function
from PIL import Image
import os


im = Image.open("my-examples/image_processing/resources/modelo0.jpg")
print(im.format, im.size, im.mode)
#im.show()

#region = im.crop(box)
#region.show()

r, g, b = im.split()
mm = Image.merge("RGB", (b, g, r))
mm.show()
