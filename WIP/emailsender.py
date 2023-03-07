import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Email account details
sender_email = 'your_email@example.com'
sender_password = 'your_app_password'
recipient_email = 'recipient_email@example.com'

# Create the email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Test Email'

# Add the body text to the email
text = "This is a test email"
body = MIMEText(text)
message.attach(body)

# Send the email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())

# Read the most recent email in the inbox
with imaplib.IMAP4_SSL('imap.gmail.com') as server:
    server.login(sender_email, sender_password)
    server.select('inbox')
    _, data = server.search(None, 'ALL')
    email_ids = data[0].split()
    latest_email_id = email_ids[-1]
    _, data = server.fetch(latest_email_id, '(RFC822)')
    print(data[0][1])
