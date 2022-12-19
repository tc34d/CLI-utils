import smtplib

# Get the email address and password from the user
email = input("Enter your email address: ")
password = input("Enter your password: ")

# Set up the SMTP server
server = smtplib.SMTP('smtp.email.com', 587)
server.starttls()
server.login(email, password)

# Send the email
recipient = input("Enter the recipient's email address: ")
subject = input("Enter the subject of the email: ")
body = input("Enter the body of the email: ")
msg = "Subject: " + subject + "\n\n" + body
server.sendmail(email, recipient, msg)

# Disconnect from the server
server.quit()
