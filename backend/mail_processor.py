import base64
import email
import imaplib
import requests
import random
import collections
import re
import numpy as np

from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

from pymystem3 import Mystem
from nltk import word_tokenize
from nltk.corpus import stopwords
from summa.summarizer import summarize

MAX_NB_WORDS = 50000
MAX_SEQUENCE_LENGTH = 250
EMBEDDING_DIM = 100

def cut_old_emails(text):
    text = text.split('\n')
    bar = ''
    for elem in text:
        if len(elem)>0:
            bar += '\n' + elem if elem[0] != '>' else ''
    return bar

def check_stopwords(text):
    ru_stopwords = stopwords.words("russian")
    ru_stopwords.append('привет')
    for word in text:
        if word in ru_stopwords:
            text.remove(word)
    return text

def replace_symbols(text):
    return re.sub(r'[^А-Яа-я]', ' ', text)
#     return re.sub(r' *', ' ', text).replace('  ',' ')

def get_priority(text):
    X = ' '.join(text)
    tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
    tokenizer.fit_on_texts(X)
    word_index = tokenizer.word_index
    X = tokenizer.texts_to_sequences([X[0]])
    X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)
    model = load_model('priority_model.h5')
    result = model.predict(X)
    return np.argmax(result)

def stemming(text):
#     print('------------------')
#     print(text)
#     text = re.sub(r'  *', ' ', text).replace('  ',' ')
#     print('------------------')
#     print(text)
#     print('------------------')
    stem = Mystem()
    tokens = stem.lemmatize(text)
    tokens = [word for word in tokens if len(word) > 2]
    return tokens

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
            
#             mail_tags = ' '.join(['#'+x[0] for x\
#                                   in collections.Counter(check_stopwords((replace_symbols(cut_old_emails(mail_content)))\
#                                                                          .split(' '))).most_common(6)])
            clean_message = check_stopwords(stemming(replace_symbols(cut_old_emails(mail_content.lower()))))
            mail_tags = ['#'+x[0] for x in collections.Counter(clean_message).most_common(5)]
            mail_tags.remove('#') if '#' in mail_tags else mail_tags
            mail_tags = ' '.join(mail_tags)
#             mail_tags = summarize(mail_content, words=10)
#             mail_priority = random.randint(0,3)
            mail_priority = get_priority(clean_message)
    
#             print(mail_priority)

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
                                                                'short_text': mail_short_content,\
                                                                'tags': mail_tags,\
                                                                'priority': str(mail_priority)})