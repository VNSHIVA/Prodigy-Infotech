from PIL import Image
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def encrypt_image(input_path, output_folder, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size
    key = sum(ord(c) for c in key)  # Summing ASCII values of characters in the key

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    # Create the output path for the encrypted image
    encrypted_path = os.path.join(output_folder, os.path.basename(input_path).replace('.', '_encrypted.'))
    img.save(encrypted_path)
    logging.info(f"Encrypted image saved to {encrypted_path}")

def decrypt_image(input_path, output_folder, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size
    key = sum(ord(c) for c in key)  # Summing ASCII values of characters in the key

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    # Create the output path for the decrypted image
    decrypted_path = os.path.join(output_folder, os.path.basename(input_path).replace('_encrypted', '_decrypted'))
    img.save(decrypted_path)
    logging.info(f"Decrypted image saved to {decrypted_path}")

def batch_process_images(input_folder, output_folder_encrypted, output_folder_decrypted, key, operation):
    # Create output directories if they don't exist
    os.makedirs(output_folder_encrypted, exist_ok=True)
    os.makedirs(output_folder_decrypted, exist_ok=True)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        if operation == 'encrypt':
            if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                encrypt_image(input_path, output_folder_encrypted, key)
        elif operation == 'decrypt':
            if filename.endswith('_encrypted.png') or filename.endswith('_encrypted.jpg') or filename.endswith('_encrypted.jpeg') or filename.endswith('_encrypted.bmp'):
                decrypt_image(input_path, output_folder_decrypted, key)

def main():
    input_folder = r"C:\Users\vnshi\Prodigy infotech\Pixel Manipulator - A Simple Image Encryption and Decryption\input_image"  # Input folder path
    output_folder_encrypted = r"C:\Users\vnshi\Prodigy infotech\Pixel Manipulator - A Simple Image Encryption and Decryption\encrypted_images"  # Output folder for encrypted images
    output_folder_decrypted = r"C:\Users\vnshi\Prodigy infotech\Pixel Manipulator - A Simple Image Encryption and Decryption\decrypted_images"  # Output folder for decrypted images
    key = "my_secret_key"  # Your encryption/decryption key

    # User selection for operation
    operation = input("Would you like to (e)ncrypt or (d)ecrypt images? ").strip().lower()
    
    if operation == 'e':
        batch_process_images(input_folder, output_folder_encrypted, output_folder_decrypted, key, operation='encrypt')
    elif operation == 'd':
        batch_process_images(input_folder, output_folder_encrypted, output_folder_decrypted, key, operation='decrypt')
    else:
        print("Invalid selection. Please enter 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()
