# modelCreation.py
import os
import pandas as pd
import gensim
from gensim import corpora, models
import preProcess as pp
import pickle
from gensim.test.utils import datapath
from pathlib import Path
from typing import Any
from gensim.models.coherencemodel import CoherenceModel


def model_creation(file):
    print("Importing Data")
    data = pd.read_csv(os.getcwd() + "\\Src Files\\" + file + ".csv", error_bad_lines=False)
    data_text = data[['Body']]
    documents = data_text
    print("Data import is completed")

    print("Running pre Processing on Documents")
    processed_body = documents['Body'].map(pp.pre_process)
    print("Pre Processing is completed")
    print("Creation dictionary with documents")
    dictionary = corpora.Dictionary(processed_body)
    dictionary.filter_extremes(no_below=100, no_above=0.5, keep_n=200000)
    print("Saving dictionary")

    print("Creating dictionary directory")
    dirName = os.getcwd() + "\\Dictionaries\\" + file
    dictPath = dirName + "\\dictionary.pkl"
    path = Path(dirName)
    path.mkdir(parents=True, exist_ok=True)

    print("Creating Topic directory")
    dirName = os.getcwd() + "\\Topics\\" + file
    path = Path(dirName)
    path.mkdir(parents=True, exist_ok=True)

    dirName = os.getcwd() + "\\Named Topics\\" + file
    path = Path(dirName)
    path.mkdir(parents=True, exist_ok=True)

    print("Saving Dictionary")
    with open(dictPath, 'wb') as d:
        pickle.dump(dictionary, d, protocol=pickle.HIGHEST_PROTOCOL)

    print("Creating Corpus")
    bow_corpus = [dictionary.doc2bow(doc) for doc in processed_body]
    tfidf = models.TfidfModel(bow_corpus)
    corpus_tfidf = tfidf[bow_corpus]

    print("Creating LDA Model")
    lda = gensim.models.ldamodel.LdaModel(corpus_tfidf, num_topics=20, id2word=dictionary, passes=4)
    coherence = CoherenceModel(model = lda, corpus = corpus_tfidf, dictionary = dictionary, coherence = 'u_mass')
    coherenceLda = coherence.get_coherence()
    print("Coherence: " + str(coherenceLda))

    print("Creating model directory")
    dirName = os.getcwd() + "\\Models\\" + file
    path = Path(dirName)
    path.mkdir(parents=True, exist_ok=True)

    print("Saving model")
    lda.save(dirName + "\\models")

    print("Saving Topics to file")
    topicList = lda.show_topics(num_topics=20, num_words=15, log=False, formatted=True)
    topicsPath = os.getcwd() + "\\Topics\\"
    namedTopicsPath = os.getcwd() + "\\Named Topics\\"

    with open(topicsPath + file + "\\topic.txt", 'w') as f:
        for x, item in topicList:
            f.write(str(x) + ", " + item + "\n")

    with open(namedTopicsPath + file + "\\topic.csv", 'w') as f:
        f.write("index,Body,Topic\n")
        for x, item in topicList:
            f.write(str(x) + ", " + item + ",Replace Topic Name" + "\n")
