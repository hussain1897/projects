import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email from Python!"
sender_email = "youremail@gmail.com" #add your email
reciever_email = "recipientemail@gmail.com" #add recipient
password = input("Enter a password:")

message = EmailMessage()
message["From"] = sender_email
message["To"] = reciever_email
message["subject"] = subject


html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</>
    </body>
</html>
"""
message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context =context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email,reciever_email, message.as_string)
print("Success")
