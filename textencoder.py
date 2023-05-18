from PIL import Image

with open('Monkee.txt', 'r', encoding='utf8') as f:
    data = f.read()

#determine the image dimensions based on the length of the string
length = len(data)
width, height, i = 1, length, 0
while width < height:
    i += 1
    if length % i == 0:
        width = i
        height = length // width

#create a new image with the calculated dimensions
img = Image.new('L', (width, height))

#loop through each character in the string and assign it to a pixel in the image
for i, c in enumerate(data):
    #convert the character to its ASCII value
    ascii_val = ord(c)

    x = i % width   
    y = i // width
    #set the pixel at position (x, y) to the grayscale value
    img.putpixel((x, y), int((ascii_val/127*255)))


img.save('output.png')
