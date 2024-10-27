import random
import string

def generate_key():
    """Create a shuffled key for substitution cipher."""
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars_list = list(chars)
    key = chars_list.copy()
    random.shuffle(key)
    return chars_list, key

def caesar_cipher(text, shift, action):
    """Encrypt or decrypt text using the Caesar cipher method."""
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shift_direction = shift if action == 'e' else -shift
            result += chr((ord(char) - start + shift_direction) % 26 + start)
        else:
            result += char
    return result

def encrypt_substitution(plain_text, chars, key):
    """Encrypt text using the substitution cipher method."""
    cipher_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]
    return cipher_text

def decrypt_substitution(cipher_text, chars, key):
    """Decrypt text using the substitution cipher method."""
    plain_text = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]
    return plain_text

def main():
    while True:
        print("\nWelcome! Choose your cipher method:")
        print("1. Caesar Cipher")
        print("2. Substitution Cipher")
        print("3. Exit")
        
        choice = input("Please enter your choice (1/2/3): ")
        
        if choice == '3':
            print("Thanks for using the program. Goodbye!")
            break
        
        if choice == '1':
            action = input("Do you want to 'e' for encryption or 'd' for decryption? ").lower()
            while action not in ['e', 'd']:
                print("Oops! Please select 'e' or 'd'.")
                action = input("Do you want to 'e' for encryption or 'd' for decryption? ").lower()

            message = input("Enter your message: ")
            shift = int(input("Enter your shift value (integer): ")) % 26
            
            result = caesar_cipher(message, shift, action)
            action_word = "Encrypted" if action == 'e' else "Decrypted"
            print(f"{action_word} message: {result}")

        elif choice == '2':
            chars, key = generate_key()
            print(f"Character set: {chars} | Shuffled key: {key}")

            plain_text = input("Sender, please enter a message to encrypt: ")
            if any(letter not in chars for letter in plain_text):
                print("Error: Your message contains characters that aren't allowed.")
                continue
            
            encrypted_message = encrypt_substitution(plain_text, chars, key)
            print(f"Sender's encrypted message: {encrypted_message}")

            cipher_text = input("Receiver, please enter the encrypted message to decrypt: ")
            if any(letter not in key for letter in cipher_text):
                print("Error: The encrypted message has invalid characters.")
                continue
            
            decrypted_message = decrypt_substitution(cipher_text, chars, key)
            print(f"Receiver's decrypted message: {decrypted_message}")

        else:
            print("Hmm, that didn't seem right. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()