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

dirName = os.getcwd() + "\\"
ldaPath = datapath(dirName + "Models\\")

lda = models.LdaModel.load(ldaPath + "questions_9.08_to_9.09" + "\\models")
topicList = lda.show_topics(num_topics=20, num_words=15, log=False, formatted=True)


with open(os.getcwd() + "\\topic.csv", 'w') as f:
    for x, item in topicList:
        f.write(item)
