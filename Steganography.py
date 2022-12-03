#        LSB Steganography
# Reference: https://medium.com/swlh/lsb-image-steganography-using-python-2bbbee2c69a2

import numpy as np
from PIL import Image

def Encode(src, message, dest):

    pic = Image.open(src, 'r')
    pic_width, pic_height = pic.size
    array = np.array(list(pic.getdata()))

    if pic.mode == 'RGB':
        n = 3
    elif pic.mode == 'RGBA':
        n = 4
    img_pixels = array.size//n

    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > img_pixels:
        print("ERROR: Need larger file size")

    else:
        index=0
        for p in range(img_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        array=array.reshape(pic_height, pic_width, n)
        enc_pic = Image.fromarray(array.astype('uint8'), pic.mode)
        enc_pic.save(dest)
        print("Image Encoded Successfully")
        return None