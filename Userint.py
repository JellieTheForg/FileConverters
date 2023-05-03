import allconverts

choice = input("What would you like to do? ")

if choice == "Image To Binary":
    from allconverts import image_to_binary
    binary_usr = image_to_binary("binary_img.png")
    print("Binary output: ", binary_usr)

if choice == "Binary To Image":
    from allconverts import ascii_to_binary
    text = input("""Input a sentence you want made in binary: """)
    binary_img_in = ascii_to_binary(text)
    print("Binary: ",binary_img_in)
    from allconverts import binary_to_image
    binary_to_image(binary_img_in)

if choice == "Image To CSV":
    from allconverts import image_to_CSV
    image_to_CSV()

if choice == "CSV To Image":
    from allconverts import csv_to_image
    csvimgdata = input("What is the name of your CSV file? Remember to include the file ext ")
    csv_to_image(csvimgdata)

if choice == "MP3 To Image":
    from allconverts import mp3_to_photo
    file_path_aud = input("What is the name of your audio file? Make sure to include file ext and make sure it is in the same folder: ")
    mp3_to_photo(file_path_aud)

if choice == "Image To MP3":
    from allconverts import img_to_binary_aud
    aud_image_path = input("What is the name of your photo? Remember to include file ext ")
    binary_aud_out = img_to_binary_aud(aud_image_path) 
    print("Binary: ", binary_aud_out)
    from allconverts import photo_to_mp3
    photo_to_mp3(binary_aud_out)