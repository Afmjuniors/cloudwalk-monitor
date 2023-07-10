import smtplib
from email.mime.text import MIMEText

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class SendEmail:
    # Configure email information
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    subject = 'ALERT - Transactions'

    def construct_email(self, message, receiver_email):
        msg = MIMEText(f'Alert: {message}')
        msg['Subject'] = self.subject
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        return msg

    def send_email(self, message, receiver_email):
        try:
            # Connect to the Gmail SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.sender_email, self.sender_password)

            # Send the email
            server.sendmail(self.sender_email, receiver_email,
                            self.construct_email(message, receiver_email).as_string())
            print('Alert email sent successfully!')
        except Exception as e:
            print('Error sending alert email:', str(e))
        finally:
            # Close the SMTP server connection
            server.quit()
