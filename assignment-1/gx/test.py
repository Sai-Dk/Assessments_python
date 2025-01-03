import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

smtp_address = 'smtp.office365.com'
smtp_port = 587
sender_login = os.getenv('sender_login')
sender_password = os.getenv('sender_password')
receiver_email = os.getenv('receiver_email')

def send_test_email():
    msg = MIMEText('This is a test email.')
    msg['Subject'] = 'Test Email'
    msg['From'] = sender_login
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP(smtp_address, smtp_port) as server:
            server.starttls()
            server.login(sender_login, sender_password)
            server.sendmail(sender_login, [receiver_email], msg.as_string())
            print("Test email sent successfully.")
    except Exception as e:
        print(f"Failed to send test email: {e}")

send_test_email()
