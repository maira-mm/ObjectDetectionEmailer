import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = ""
SENDER = ""
RECEIVER = ""

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "An intruder has been spotted"
    email_message.set_content("Hey, we have a few images of movement spotted in our camera")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/19.png")