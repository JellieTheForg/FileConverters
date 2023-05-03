from PIL import Image
import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def image_to_binary(image_path):
    image = Image.open(image_path)
    binary_img_out = ""
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            pixel_value = pixels[x, y]
            binary_img_val_out = "1" if pixel_value == 0 else "0"
            binary_img_out += binary_img_val_out
    return binary_img_out

def ascii_to_binary(text):
    binary_img_in = ""
    for char in text:
        ascii_value = ord(char)
        binary_img_val_in = bin(ascii_value)[2:]  # Remove the '0b' prefix
        padded_binary = binary_img_val_in.zfill(8)
        binary_img_in += padded_binary
    return binary_img_in

def binary_to_image(binary_img_in):
    # Determine the width and height of the image based on the length of the binary string
    length = len(binary_img_in)

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
    for i, bit in enumerate(binary_img_in):
        pixel_value = 255 if bit == '0' else 0
        x = i % width
        y = i // width
        img.putpixel((x, y), pixel_value)

    # Display the image
    img.show()
    img.save('binary_img.png')

def image_to_CSV():
    question=input("Is your image in the same folder as this python file? ")

    if question == "no" or question == "No" or question == "N" or question == "n":
        print("Please move it to the same folder as this one.")

    if question == "yes" or question == "Yes" or question == "y" or question == "Y":
        filepath_img_csv = input("What is the name of your image? Please include the file extension: ")

        #load the black and white image
        image = Image.open(filepath_img_csv).convert('L')

        #get the pixel values as a 2D numpy array
        pixels = image.load()
        width, height = image.size

        #convert each pixel to a value between 0 and 1 based on its darkness
        data = [[pixels[x, y] / 255 for x in range(width)] for y in range(height)]

        #create a dataframe from the data
        df = pd.DataFrame(data)

        #save the dataframe as a csv file
        df.to_csv('image_data.csv', index=False)

def csv_to_image(csvimgdata):
    df = pd.read_csv('image_data.csv')

    #calculate the aspect ratio of the original image
    num_rows, num_cols = df.shape
    aspect_ratio= num_cols/num_rows

    #set the figure size with the original aspect ratio
    fig, ax = plt.subplots(figsize=(10, 10 / aspect_ratio), dpi=300)

    #create the heatmap plot using seaborn
    heatmap = sns.heatmap(df, cmap='gray', cbar=False)

    #remove the ticks and tick labels on the side of the heatmap
    heatmap.set_yticks([])
    heatmap.set_xticks([])
    heatmap.set_yticklabels([])
    heatmap.set_xticklabels([])

    #save the plot with high quality
    heatmap.figure.savefig('heatmap_high_quality2.png', bbox_inches='tight', dpi=300)

def mp3_to_photo(file_path_aud):
    with open(file_path_aud, "rb") as file:
        hex_string_in = file.read()

    # Convert binary data to base 2 (binary) string
    binary_aud_in = ''.join(format(byte, '08b') for byte in hex_string_in)

    print("Binary:", binary_aud_in)


    # Determine the width and height of the image based on the length of the binary string
    length = len(binary_aud_in)
    print(length)

    #If length is prime, it sets width and height to length and 1, respectively, and if there are factors, it finds the biggest ones between them
    width, height, i = 1, length, 0
    while width < height:
        i += 1
        if length % i == 0:
            width = i
            height = length//width

    # Create a new blank image
    img_aud = Image.new('L', (width, height))

    # Iterate through the binary string and draw black or white pixels
    for i, bit in enumerate(binary_aud_in):
        pixel_value = 255 if bit == '0' else 0
        x = i % width
        y = i // width
        img_aud.putpixel((x, y), pixel_value)

    # Display the image
    img_aud.show()
    img_aud.save('audio.png')

def img_to_binary_aud(aud_image_path):
    image = Image.open(aud_image_path)
    binary_aud_out = ""
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            pixel_value = pixels[x, y]
            binary_value = "1" if pixel_value == 0 else "0"
            binary_aud_out += binary_value
    return binary_aud_out

def photo_to_mp3(binary_aud_out):
    hex_string_out = hex(int(binary_aud_out, 2))[2:]

    # Pad the hexadecimal string if the length is not a multiple of 2
    padded_hex = hex_string_out.zfill((len(hex_string_out) + 1) // 2 * 2)

    hex_out = bytes.fromhex(padded_hex)

    # Save the binary data as an MP3 file
    output_file_path = "output.mp3"

    with open(output_file_path, "wb") as file:
        file.write(hex_out)
