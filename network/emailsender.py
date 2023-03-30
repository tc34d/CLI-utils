import smtplib

# Prompt user for login credentials and email details
sender_email = input("Enter your email address: ")
sender_password = input("Enter your email password: ")
recipient_email = input("Enter the recipient email address: ")
subject = input("Enter the email subject: ")
message = input("Enter the email message: ")

# Create the email message
email = f"""\
From: {sender_email}
To: {recipient_email}
Subject: {subject}

{message}
"""

# Connect to the SMTP server and send the email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    smtp.sendmail(sender_email, recipient_email, email)

print("Email sent successfully.")
