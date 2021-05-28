import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "amandamakara7@gmail.com"
receiver_email = ["zakjardien23@gmail.com", "thapelo@lifechoices.co.za", "vuyanikunelisi@gmail.com"]
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "greetings"
message["From"] = sender_email
message["To"] = ", ".join(receiver_email)

a_message = """\
hello
i
y
"""

part1 = MIMEText(a_message, "plain")

message.attach(part1)


# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )