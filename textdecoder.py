from PIL import Image

img = Image.open('output.png')
#get the dimensions of the image
width, height = img.size

test=1
decoded_text = ''

#loop through each pixel in the image and decode the grayscale value to a character
for y in range(height):
    for x in range(width):
        #get the grayscale value of the pixel at position (x, y)
        grayscale_val = img.getpixel((x, y))
        #print(grayscale_val)
        #convert the grayscale value to an ASCII value
        ascii_val = int(grayscale_val/255 * 128) 
        #convert the ASCII value to a character and append it to the decoded text
        decoded_text += chr(ascii_val)
        test=test+1

#write the decoded text to a file using ASCII encoding
with open('Monke_out.txt', 'w', encoding='ascii') as f:
    f.write(decoded_text)
