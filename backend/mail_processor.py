import base64
import email
import imaplib
import requests
from summa.summarizer import summarize

def cut_old_emails(text):
    text = text.split('\n')
    bar = ''
    for elem in text:
        if len(elem)>0:
            bar += '\n' + elem if elem[0] != '>' else ''
    return bar

EMAIL = 'adva.mailer.pub@gmail.com'
PASSWORD = 'qazwsxedcrfvtgbyhn123456'
SERVER = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(SERVER, 993)
mail.login(EMAIL, PASSWORD)
mail.select('inbox')

status, data = mail.search(None, 'UNSEEN')
mail_ids = []
for block in data:
    mail_ids += block.split()

for i in mail_ids:
    status, data = mail.fetch(i, '(RFC822)')

    for response_part in data:
        if isinstance(response_part, tuple):
            message = email.message_from_bytes(response_part[1])

#             print(message.keys())
            
            mail_id = message['Message-ID']
            mail_date = message['Date']
            try:
                mail_from = base64.b64decode(message['from'] if message['from'][:10].upper() !=\
                                             '=?UTF-8?B?' else message['from'][10:-2])
            except:
                mail_from = message['from']
            try:
                mail_from = mail_from.decode('utf-8','ignore')
            except:
                pass
            
            try:
                mail_subject = base64.b64decode(message['subject'] if message['subject'][:10].upper() !=\
                                                '=?UTF-8?B?' else message['subject'][10:-2])
#                 mail_subject = base64.b64decode(message['subject'])
            except:
                mail_subject = message['subject']
            try:
                mail_subject = mail_subject.decode('utf-8','ignore')
            except:
                pass
            if message.is_multipart():
                mail_content = ''

                for part in message.get_payload():
                    if part.get_content_type() == 'text/plain':
                        mail_content += part.get_payload()
                mail_content = base64.b64decode(mail_content).decode("utf-8", "ignore")
            else:
                mail_content = base64.b64decode(message.get_payload()).decode("utf-8", "ignore")
                
            mail_short_content = summarize(cut_old_emails(mail_content), ratio=0.2)

            # and then let's show its result
#             print(f'ID: {mail_id}')
#             print(f'Date: {mail_date}')
#             print(f'From: {mail_from}')
#             print(f'Subject: {mail_subject}')
#             print(f'Content: {mail_content}')
#             print(f'Short Content: {mail_short_content}')
            requests.post('http://localhost:8000/mails/', json={'date': mail_date,\
                                                                'mail': mail_from,\
                                                                'subject': mail_subject,\
                                                                'text': mail_content,\
                                                                'short_text': mail_short_content})