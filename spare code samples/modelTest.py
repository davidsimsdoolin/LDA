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


dirName = os.getcwd() + "\\"
ldaPath = datapath(dirName + "Models\\")
dictPath = datapath(dirName + "Dictionaries\\")
topicsPath = datapath(dirName + "Topics\\")

lda = models.LdaModel.load(ldaPath + File + "\\models")
topicList = lda.show_topics(num_topics=40, num_words=15, log=False, formatted=True)
topic_winner = 0
topic_index = 0

with open(dictPath + File + "\\dictionary.pkl", 'rb') as d:
    dictionary = pickle.load(d)

print("Perplexity: " + lda.log_perplexity())