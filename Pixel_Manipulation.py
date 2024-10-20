from PIL import Image

def encrypt_image(image_path, shift, output_path='encrypted_image.png'):
    image = Image.open(image_path)
    pixels = image.load()  

  
    for x in range(image.width):
        for y in range(image.height):
            pixel = pixels[x, y]
           
            if len(pixel) == 3:
                r, g, b = pixel
                encrypted_r = (r + shift) % 256
                encrypted_g = (g + shift) % 256
                encrypted_b = (b + shift) % 256
                pixels[x, y] = (encrypted_r, encrypted_g, encrypted_b)
            elif len(pixel) == 4:
                r, g, b, a = pixel
                encrypted_r = (r + shift) % 256
                encrypted_g = (g + shift) % 256
                encrypted_b = (b + shift) % 256
                pixels[x, y] = (encrypted_r, encrypted_g, encrypted_b, a)

    image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(image_path, shift, output_path='decrypted_image.png'):
    image = Image.open(image_path)
    pixels = image.load() 
    for x in range(image.width):
        for y in range(image.height):
            pixel = pixels[x, y]
            if len(pixel) == 3:
                r, g, b = pixel
                decrypted_r = (r - shift) % 256
                decrypted_g = (g - shift) % 256
                decrypted_b = (b - shift) % 256
                pixels[x, y] = (decrypted_r, decrypted_g, decrypted_b)
            elif len(pixel) == 4:
                r, g, b, a = pixel
                decrypted_r = (r - shift) % 256
                decrypted_g = (g - shift) % 256
                decrypted_b = (b - shift) % 256
                pixels[x, y] = (decrypted_r, decrypted_g, decrypted_b, a)

    image.save(output_path)
    print(f"Decrypted image saved as {output_path}")

image_path = input("Enter the path to the image file: ")
shift_value = int(input("Enter the shift value for encryption/decryption: "))
mode = input("Do you want to (e)ncrypt or (d)ecrypt the image? ")

if mode.lower() == 'e':
    encrypt_image(image_path, shift_value)
elif mode.lower() == 'd':
    decrypt_image(image_path, shift_value)
else:
    print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
