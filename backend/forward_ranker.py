import re
import pandas as pd

from pymystem3 import Mystem
from nltk import word_tokenize
from nltk.corpus import stopwords

ru_stopwords = stopwords.words("russian")

def stemming(tokens: list) -> pd.Series:
    stem = Mystem()
    tokens = [word_tokenize("".join(stem.lemmatize(sentence))) for sentence in tokens]
    tokens = [[word for word in sentence if len(word) > 2] for sentence in tokens]
    return tokens

def text_pr(text):
    s = pd.Series(text)
    s = s.apply(lambda x: re.sub('[0-9]+', '', x))
    s = s.apply(lambda x: re.sub('[^а-яА-Я]+', ' ', x))
    s = s.apply(lambda x: x.lower())
    s = stemming(s)
    s = check_stopwords(s)
    return ' '.join(s)

def check_stopwords(text: pd.Series) -> pd.Series:
    result = [
        [word for word in sentence if word not in ru_stopwords and word != " "]
        for sentence in text
    ]
    return result