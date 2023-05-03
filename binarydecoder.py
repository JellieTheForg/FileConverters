from PIL import Image

def image_to_binary(image_path):
    image = Image.open(image_path)
    binary_string = ""
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            pixel_value = pixels[x, y]
            binary_value = "1" if pixel_value == 0 else "0"
            binary_string += binary_value
    return binary_string

image_path = "binary_img.png"
binary = image_to_binary(image_path)
print("Binary output: ", binary)