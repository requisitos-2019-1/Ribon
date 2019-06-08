import glob
import os

from PIL import Image

header = '.imgs/header.png'
list_imgs = glob.glob('./cropped/*.png')
for i in sorted(list_imgs):
    images_list = [header, i]
    imgs = [ Image.open(i) for i in images_list ]
    width1, height1 = imgs[0].size
    width2, height2 = imgs[1].size
    width = max(width1, width2)
    height = height1+height2
    
    result = Image.new('RGBA', (width, height), 'white')
    result.paste(imgs[0], (0, 0))
    result.paste(imgs[1], (10, height1))
    # result.show()
    result.save( '.imgs/test_headed/{0}'.format(i.split('/')[-1]))
