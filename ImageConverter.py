import pandas as pd
from PIL import Image

question=input("Is your image in the same folder as this python file? ")

if question == "no" or question == "No" or question == "N" or question == "n":
    print("Please move it to the same folder as this one.")

if question == "yes" or question == "Yes" or question == "y" or question == "Y":
    filepath = input("What is the name of your image? Please include the file extension: ")

    #load the black and white image
    image = Image.open(filepath).convert('L')

    #get the pixel values as a 2D numpy array
    pixels = image.load()
    width, height = image.size

    #convert each pixel to a value between 0 and 1 based on its darkness
    data = [[pixels[x, y] / 255 for x in range(width)] for y in range(height)]

    #create a dataframe from the data
    df = pd.DataFrame(data)

    #save the dataframe as a csv file
    df.to_csv('image_data.csv', index=False)