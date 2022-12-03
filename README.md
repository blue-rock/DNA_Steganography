# Project name: DNA Steganography
Members:\
	1. Varun Motwani - 201901044\
	2. Heer Gohil - 201901135\
	3. Mansi Madhvani - 201901194\
	4. Aakash Desai - 201901233\
	5. Jheel Shah - 201901452\
	6. Priyanshu - 201901468

In this project, we are implementing Cryptography along with DNA Steganography. 
Steganography is the science that involves communicating secret data in an appropriate multimedia carrier, e.g., image, audio, and video files.
In this project, we are using Least Significant Bit (LSB) image steganography. 
LSB Steganography is an image steganography technique in which messages are hidden inside an image by replacing each pixel’s least significant bit with the bits of the message to be hidden.

## Step 1: Convert the plaintext to DNA bases.
This is done in the file conversion.py. The text is first converted to binary. The binary string is then converted to DNA bases using the sequence:\
00 - A\
01 - T\
10 - C\
11 - G\
This DNA base is then compressed using g-zip. 
g-zip is a file format used to compress or decompress any file.
The compressed text is then written to a text file.

## Step 2: Converting the DNA Bases to a ciphertext using AES-256 encyrption technology.
We have a direct library function to encrypt the data into a ciphertext. To convert into a ciphertext, we first need to generate a key. 
This key is then used to encrypt the data into a secure format.

## Step 3: Steganography - Encoding
We used PIL and NumPy libraries to implement this part of the project. 
We have an encode function which hides the ciphertext behind an image provided by us.

## Step 4: Steganograpgy - Decoding
We have a decode function which unhides the ciphertext from the image and returns the data in the form of original cipher text.

## Step 5: AES Decyrption
Similar to the process of encryption, we have a library function for decrption which gives back our original message.
