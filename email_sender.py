import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = ''  # enter your email here as a string
email['to'] = ''  # enter recipient's email here as a string
email['subject'] = ''  # enter subject here as a string
email.set_content('')  # enter email content here as a string

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('', '')
    # argument 1: your gmail address as a string
    # turn on 2-step authentication for your Google account and generate an app password
    # argument 2: the app password that you generated as a string
    smtp.send_message(email)
