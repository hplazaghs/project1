from __future__ import print_function
import os

from PIL import Image

files = [
  '/images/1.png',
  '/images/2.png',
  '/images/3.png',
  '/images/4.png']

result = Image.new("RGB", (800, 800))

for index, file in enumerate(files):
  path = os.path.expanduser(file)
  img = Image.open(path)
  img.thumbnail((400, 400), Image.ANTIALIAS)
  x = index // 2 * 400
  y = index % 2 * 400
  w, h = img.size
  print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
  result.paste(img, (x, y, x + w, y + h))

result.save(os.path.expanduser('/images/image.png'))