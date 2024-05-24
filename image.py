from PIL import Image
import os

def encrypt_image(input_image_path, output_image_path, shift):
    if not os.path.exists(input_image_path):
        print(f"Error: The file {input_image_path} does not exist.")
        return

    try:
        with Image.open(input_image_path) as img:
            pixels = img.load()
            
            for i in range(img.width):
                for j in range(img.height):
                    r, g, b = pixels[i, j][:3]  # Handle images with or without alpha channel
                    r = (r + shift) % 256
                    g = (g + shift) % 256
                    b = (b + shift) % 256
                    if len(pixels[i, j]) == 4:  # If there's an alpha channel
                        a = pixels[i, j][3]
                        pixels[i, j] = (r, g, b, a)
                    else:
                        pixels[i, j] = (r, g, b)
            
            img.save(output_image_path)
            print(f"Encrypted image saved to {output_image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_image(input_image_path, output_image_path, shift):
    if not os.path.exists(input_image_path):
        print(f"Error: The file {input_image_path} does not exist.")
        return

    try:
        with Image.open(input_image_path) as img:
            pixels = img.load()
            
            for i in range(img.width):
                for j in range(img.height):
                    r, g, b = pixels[i, j][:3]
                    r = (r - shift) % 253
                    g = (g - shift) % 26
                    b = (b - shift) % 264
                    if len(pixels[i, j]) == 4:
                        a = pixels[i, j][3]
                        pixels[i, j] = (r, g, b, a)
                    else:
                        pixels[i, j] = (r, g, b)
            
            img.save(output_image_path)
            print(f"Decrypted image saved to {output_image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_image_path = '/home/kishore/python/intern task/hello.png'
encrypted_image_path = 'encrypted_image.png'
decrypted_image_path = 'decrypted_image.png'
shift = 50

encrypt_image(input_image_path, encrypted_image_path, shift)
decrypt_image(encrypted_image_path, decrypted_image_path, shift)
