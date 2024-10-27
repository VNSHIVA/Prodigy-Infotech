import re

def clean():
    with open("log.txt", 'r') as file:
        msg = file.read()

    # Remove unnecessary spaces
    msg = re.sub(r'\s+', ' ', msg)  # Replace multiple spaces with a single space

    # Replace space key representation with a space
    msg = re.sub(r"<Key.space: ''>", ' ', msg)  # Fix the space representation

    # Gather and remove special keys
    regex_key = re.compile(r"<Key\..*?>(?=\s|$)")  # Match special keys
    msg = re.sub(regex_key, '', msg)  # Replace special keys with empty strings

    # Remove unwanted characters
    msg = msg.replace('\'', '').replace(',', '')  # Remove single quotes and commas

    # Print the cleaned message
    print(msg.strip())  # Strip leading/trailing spaces for cleaner output
