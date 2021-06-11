import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Rajaprasad paikaray'
email['to'] = 'paikaray.milan@gmail.com'
email['subject'] = 'you won 1,000,000 dollars'

email.set_content('i am a python developer')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email_id', 'password')
    smtp.send_message(email)
    print('All good Boss!')
