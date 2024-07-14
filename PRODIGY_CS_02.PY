# Second Task of the internship
# Pixel Manipulation for Image Encryption
from PIL import Image

# Function for encryption of image
def image_encrypt(path_input, path_output, key):
    img = Image.open(path_input)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # for image encryption
            pixels_encrypt = (r,b,g)
            pixels[i, j] = pixels_encrypt

    img.save(path_output)
    print("Image pixels manipulation successfully encrypted")

# Function for decryption of image
def image_decrypt(path_input, path_output, key):
    img = Image.open(path_input)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # for image decryption
            pixels_decrypt = (r,b,g)
            pixels[i, j] = pixels_decrypt

    img.save(path_output)
    print("Image pixels manipulation successfully decrypted")

# taking path of images
path_input = r"E:\Internship\Cyber Security\1717174261091.jpg"
path_output_encrypt = r"E:\Internship\Cyber Security\Encrypted_image.jpg"
path_output_decrypt = r"E:\Internship\Cyber Security\Decrypted_image.jpg"

# calling the function of encryption of the image
image_encrypt(path_input, path_output_encrypt, key=None)

# calling the function of decryption of the image
image_decrypt(path_output_encrypt, path_output_decrypt, key=None)
