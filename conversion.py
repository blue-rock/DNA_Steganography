import gzip
import AESenc
import Steganography
# function to convert input string to ascii and then to binary


def stringtobin(s):
    # converting string to ascii list
    ascii_list = [ord(c) for c in s]
    print(ascii_list)
    # converting ascii to binary string
    bin_str = ""
    for i in ascii_list:
        bin = format(i,'08b')
        bin_str = bin_str+bin
    print("binary string :", bin_str)
    return bin_str

# function to convert binary string to DNA bases


def binToDna(bstr):
    output_seq = ''
    for start in range(0, len(bstr), 2):
        curr_code = bstr[start:start+2]
        if curr_code == '00':
            output_seq += 'A'
        elif curr_code == '01':
            output_seq += 'T'
        elif curr_code == '10':
            output_seq += 'C'
        elif curr_code == '11':
            output_seq += 'G'
    print("DNA bases :", output_seq)
    return output_seq

# converts dna to ascii list and multiply it with a factor


def dnaToAscii(dstr):
    factor = 7
    f_list = list()
    dna_list = [ord(c) for c in dstr]
    print(dna_list)
    for a in dna_list:
        a = a*factor
        f_list.append(a)
    f_joined = " ".join(str(n) for n in f_list)
    print("dna to ascii :", f_joined)
    return f_joined

# writes the ciphertext to a text file


def fwrite(dnaascii):
    with open("cipher.txt", 'wb') as f:
        f.write(dnaascii)
        f.close()
    print("fwrite")
    return None
# compresses the message using gzip


def compression(ascString):
    compressed_value = gzip.compress(bytes(ascString, 'utf-8'))
    print("compression :", compressed_value.hex()) #converts byte to hex
    return compressed_value


s = input("Enter your secret messege: ")
bistr = stringtobin(s)
btd = binToDna(bistr)
dToA = dnaToAscii(btd)
compr = compression(dToA)
filewrite = fwrite(compr)

AESenc.encryption()


orig_img = "Original_image\\hut.png"
destImg = "Output_image\\steg.png"
with open('encrypted.bin','rb') as f:
    message = f.read()
    f.close()
hexmessage = message.hex()
Steganography.Encode(orig_img,hexmessage,destImg)