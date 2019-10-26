import os
from PIL import Image
import pytesseract as pyt
def pdf2jpg(fname):
    path = fname[:fname.find('.')]
    exist = False
    image = list()
    if(not os.path.isdir(path)):
        os.mkdir(path)
        image = convert_from_path(fname, 900, fmt="PNG")
    else:
        dirs = os.listdir(path)
        for fname in dirs:
            image.append(Image.open(path+"/"+fname))
        exist = True

    for i,pg in enumerate(image):
        if(not exist):
            outfile = path + "/"+fname[:fname.find('.')] + "_" + str(i+1) + ".png"
            pg.save(outfile, "PNG")
