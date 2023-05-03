from PIL import Image
import math

def ascii_to_binary(text):
    binary_string = ""
    for char in text:
        ascii_value = ord(char)
        binary_value = bin(ascii_value)[2:]  # Remove the '0b' prefix
        padded_binary = binary_value.zfill(8)
        binary_string += padded_binary
    return binary_string

text = input("Input a sentence you want made in binary: ")
binary_string = ascii_to_binary(text)
print("Binary: ",binary_string)

# Determine the width and height of the image based on the length of the binary string
length = len(binary_string)
print(length)

#If length is prime, it sets width and height to length and 1, respectively, and if there are factors, it finds the biggest ones between them
width, height, i = 1, length, 0
while width < height:
    i += 1
    if length % i == 0:
        width = i
        height = length//width

# Create a new blank image
img = Image.new('L', (width, height))

# Iterate through the binary string and draw black or white pixels
for i, bit in enumerate(binary_string):
    pixel_value = 255 if bit == '0' else 0
    x = i % width
    y = i // width
    img.putpixel((x, y), pixel_value)

# Display the image
img.show()
img.save('binary_img.png')