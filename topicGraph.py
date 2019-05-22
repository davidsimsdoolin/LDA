#TopicGraph.py

import os
import pandas as pd
from pandas import DataFrame as df
import numpy as np
import matplotlib.pyplot as plt


def topic_graph(file):
    print("Importing topic counts and topic names")
    topicCounts = pd.read_csv(os.getcwd() + "\\Topic Counts\\" + file + "\\count.csv")
    topicNames = pd.read_csv(os.getcwd() + "\\Named Topics\\" + file + "\\topic.csv")

    print("Matching count id to topic id")
    topicNamesSorted = df()
    p = 0
    topicNamesSorted['index'] = topicCounts.iloc[:,0]
    topicNamesSorted['Topic'] = topicCounts.iloc[:,0]
    while p < len(topicNames.index.tolist()):
        print(int(topicNamesSorted.iloc[p,0]))
        x = topicNames.iloc[int(topicNamesSorted.iloc[p,0]),2]
        topicNamesSorted.iloc[p, 1] = x
        p = p+1

    print("Graphing Topics Counts")
    ypos = np.arange(len(topicNames.index.tolist()))
    plt.bar(ypos, topicCounts['Topic'], align='center', alpha=0.5)
    plt.xticks(ypos, topicNamesSorted['Topic'], rotation =90)
    plt.ylabel('Popularity')
    plt.title('Topics ' + file)
    plt.tight_layout()

    plt.show(block=False)
    print("Saving Graph to png image file")
    plt.savefig(file + ".png")
