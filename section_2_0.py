import nltk
import string
import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import os
def get_intro_plot(i):
    data = pd.read_csv("tsv\\{0}.tsv".format(i),sep='\t')
    data = list(data)[2:4]
    data =" ".join(data)
    return data
def preprocess(text):
    text ="".join([char for char in text if char not in string.punctuation])
    words = word_tokenize(text)
    stop_words = stopwords.words('english')
    filtered_words = [word for word in words if word not in stop_words]
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in filtered_words]
    return stemmed
def save_words():
    for i in range(30000):
        try:
            text=get_intro_plot(i)
        except:
            continue
        words =preprocess(text)
        words=" ".join(words)
        with open('word\\{0}.tsv'.format(i), 'w', encoding='utf-8', newline ='') as f:
            f.write(words)
os.mkdir('word')
save_words()