import numpy as np
from PIL import Image
import AESDecrypt
import gzip

def Decode(src):

    pic = Image.open(src, 'r')
    arr = np.array(list(pic.getdata()))

    if pic.mode == 'RGB':
        n = 3
    elif pic.mode == 'RGBA':
        n = 4
    net_pix = arr.size//n

    hid_bits = ""
    for p in range(net_pix):
        for q in range(0, 3):
            hid_bits += (bin(arr[p][q])[2:][-1])

    hid_bits = [hid_bits[i:i+8] for i in range(0, len(hid_bits), 8)]

    msg = ""
    for i in range(len(hid_bits)):
        if msg[-5:] == "$t3g0":
            break
        else:
            msg += chr(int(hid_bits[i], 2))
    if "$t3g0" in msg:
        print("Hidden message:", msg[:-5])
        msg = msg[:-5]
    else:
        print("There was no hidden Message")
    return msg

dest = "C:\\Users\\hp\\Desktop\\DNA\\Project\\Output_image\\steg.png"
msg = Decode(dest)
b_msg = bytes.fromhex(msg)

output_file = 'encrypted.bin'
file_out = open(output_file, "wb")
file_out.write(b_msg)
file_out.close()

def Extract(c_value):
    plain_string = gzip.decompress(c_value).decode('utf-8')
    print(plain_string)
    return plain_string

def AsciiToDna(asciiv):
    ascii_list = list()
    dna_seq = list()
    factor = 7
    list_fascii = asciiv.split(' ')
    print(list_fascii)
    for i in list_fascii:
        asc = int(i)/factor
        ascii_list.append(int(asc))
    for i in ascii_list:
        dna_seq.append(chr(i))
    print(dna_seq)
    result_string = ''
    for i in dna_seq:
        if i == 'A':
            result_string += '00'
        elif i == 'T':
            result_string += '01'
        elif i == 'C':
            result_string += '10'
        elif i == 'G':
            result_string += '11'
    print(result_string)
    return result_string

def binToStr(bstr):
    n = 8
    btoa_list = list()
    bin_list = [bstr[i:i+n] for i in range(0, len(bstr), n)]
    print(bin_list)
    for i in bin_list:
        btoa_list.append(int(i, 2))
    print(btoa_list)
    plaintxt = ''.join(chr(i) for i in btoa_list) #ascii to string
    print(plaintxt)
    print("Successfully Decoded the message")
    z = input("Press enter to exit")
    return None

comp_val = AESDecrypt.Decrypt()
asciiv = Extract(comp_val)
bstr = AsciiToDna(asciiv)
binToStr(bstr)

