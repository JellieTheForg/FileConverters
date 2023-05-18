from PIL import Image

def convert_image_to_hex(image_path):
    color_mapping = {
    (255, 204, 204): '0',
    (255, 229, 204): '1',
    (255, 242, 204): '2',
    (217, 232, 223): '3',
    (204, 224, 245): '4',
    (217, 204, 230): '5',
    (230, 204, 255): '6',
    (230, 232, 204): '7',
    (204, 255, 204): '8',
    (255, 217, 204): '9',
    (255, 204, 230): 'A',
    (204, 230, 255): 'B',
    (243, 204, 255): 'C',
    (204, 255, 230): 'D',
    (255, 243, 204): 'E',
    (230, 255, 204): 'F'
    }
    img = Image.open(image_path)
    width, height = img.size

    hex_data = ''
    for y in range(height):
        for x in range(width):
            pixel_color = img.getpixel((x, y))
            hex_digit = color_mapping.get(pixel_color, '0')  # Get the corresponding hexadecimal digit
            hex_data += hex_digit

    return hex_data

def convert_hex_to_mp3(hex_data):
    output_file = "heximageoutput.mp3"
    binary_data = bytes.fromhex(hex_data)
    with open(output_file, 'wb') as f:
        f.write(binary_data)


image_path = 'hex_visualization.png'

hex_data = convert_image_to_hex(image_path)
convert_hex_to_mp3(hex_data)
