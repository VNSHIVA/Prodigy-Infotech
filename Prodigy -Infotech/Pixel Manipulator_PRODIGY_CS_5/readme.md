# Task 2: Pixel Manipulation / Image Encryption Tool

This Python program provides a simple image encryption tool using pixel manipulation techniques. Users can encrypt and decrypt images by performing mathematical operations on pixel values, all while enjoying a user-friendly experience with clear prompts.

## Features

- **Image Encryption**: Encrypts an image by applying a mathematical operation to each pixel value, altering the image.
- **Image Decryption**: Reverses the encryption process to restore the original image.
- **User Input**: Users can specify the image file and the encryption key.
- **File Handling**: Saves encrypted and decrypted images to designated file paths.

## How It Works

- **Encrypt Image**: Each pixel value is multiplied by a key and then divided by the key plus one to create the encrypted image.
- **Decrypt Image**: The encryption process is reversed by multiplying each pixel value by the key plus one and dividing by the key.

## Usage Instructions

1. **Run the Program**: Execute the script to start the Image Encryption Tool.
2. **Select an Action**:
   - Press `'e'` for encryption
   - Press `'d'` for decryption
   - Press `'q'` to quit
3. **Encrypting an Image**:
   - Enter the encryption key.
   - Specify the location or URL of the image you want to encrypt.
4. **Decrypting an Image**:
   - Enter the decryption key.
   - Specify the location of the encrypted image.
5. **View Results**: The program will save the encrypted and decrypted images and indicate their file paths.
