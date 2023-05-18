
from PIL import Image

# Define the pastel colors
pastel_colors = [
    (255, 204, 204), (255, 229, 204), (255, 242, 204), (217, 232, 223),
    (204, 224, 245), (217, 204, 230), (230, 204, 255), (230, 232, 204),
    (204, 255, 204), (255, 217, 204), (255, 204, 230), (204, 230, 255),
    (243, 204, 255), (204, 255, 230), (255, 243, 204), (230, 255, 204)
]

def visualize_hex_data(hex_data):
    # Calculate the dimensions of the image based on the length of the hex data
    len_hex=len(hex_data)
    print(len_hex)
    width, height, i = 1, len_hex, 0
    while width < height:
        i += 1
        if len_hex % i == 0:
            width = i
            height = len_hex//width

    # Create a new image
    image = Image.new('RGB', (width, height))

    # Assign colors to pixels based on hexadecimal values
    for i, hex_value in enumerate(hex_data):
        color_index = int(hex_value, 16) % len(pastel_colors)
        color = pastel_colors[color_index]
        x = i % width
        y = i // width
        image.putpixel((x, y), color)

    # Save and display the image
    image.save('hex_visualization.png')
    image.show()


mp3_file = 'output.mp3'
with open(mp3_file, 'rb') as file:
    binary_data = file.read()
hex_data = binary_data.hex()
visualize_hex_data(hex_data)