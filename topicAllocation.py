# topicAllocation.py

import os
import preProcess as pp
from gensim.test.utils import datapath
from gensim import models
import pickle
import pandas as pd
from pandas import DataFrame as df
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

File = ""
FileCount = 0


def topic_allocation(file):
    global File
    File = file

    print("Importing Data")
    data = pd.read_csv(os.getcwd() + "\\Src Files\\" + file + ".csv", error_bad_lines=False)
    data_text = data[['Body']]
    documents = data_text
    global FileCount
    FileCount = data_text.size
    print("Data import is completed")

    print("Creating Topic directory")
    dirName = os.getcwd() + "\\Topics\\" + file
    path = Path(dirName)
    path.mkdir(parents=True, exist_ok=True)

    print("Creating Topic Count directory")
    dirName = os.getcwd() + "\\Topic Counts\\" + file
    path = Path(dirName)
    path.mkdir(parents=True, exist_ok=True)

    print("Allocating topics to documents")
    allocation_Results = documents['Body'].map(allocation)
    print("Allocation of topics is completed")
    topics = df(allocation_Results)
    data['Topic'] = topics[['Body']]

    print("Running counts of Topics")
    topicCount = df(data['Topic'].value_counts())
    print("Saving Topic Counts to  a csv file")
    topicCount.to_csv(os.getcwd() + "\\Topic Counts\\" + file + "\\count.csv")

    print("Saving csv with topic id's")
    data.to_csv(os.getcwd() + "\\Topic Allocated Files\\" + file + ".csv")


def allocation(document):
    global FileCount
    FileCount = FileCount - 1
    print(FileCount)
    dirName = os.getcwd() + "\\"
    ldaPath = datapath(dirName + "Models\\")
    dictPath = datapath(dirName + "Dictionaries\\")
    topicsPath = datapath(dirName + "Topics\\")

    lda = models.LdaModel.load(ldaPath + File + "\\models")
    topicList = lda.show_topics(num_topics=20, num_words=15, log=False, formatted=True)
    topic_winner = 0
    topic_index = 0

    with open(dictPath + File + "\\dictionary.pkl", 'rb') as d:
        dictionary = pickle.load(d)

    for index, score in sorted(lda[dictionary.doc2bow(pp.pre_process(str(document)))], key=lambda tup: -1*tup[1]):
        if topic_winner < score:
            topic_winner = score
            topic_index = index

    with open(topicsPath + File + "\\topic.txt", 'w') as f:
        for x, item in topicList:
            f.write(item)

    return topic_index
