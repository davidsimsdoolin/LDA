# preProcess.py
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
import re
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer


def lemmatize_and_stemming(text):
    stemmer = PorterStemmer()
    lemmatized = WordNetLemmatizer().lemmatize(text,pos='v')
    return stemmer.stem(lemmatized)


def remove_code(text):
    return re.sub(r'<code>[^>]+</code>', '', text)


def remove_text_tags(text):
    return re.sub(r'<[^>]+>', '', text)


def pre_process(text):
    result = []
    text_processed = remove_code(str(text))
    text = text_processed
    text_processed = remove_text_tags(str(text))
    text = text_processed

    for token in simple_preprocess(text):
        if token not in STOPWORDS and len(token) > 3:
            result.append(lemmatize_and_stemming(token))
    return result
