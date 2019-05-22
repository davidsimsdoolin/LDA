import pandas as pd
import gensim
from gensim import corpora, models
from preProcess import pre_process
import pickle
from gensim.test.utils import  datapath

print("test1")
data = pd.read_csv("C:\\Users\\Dsims\\OneDrive\\Desktop\\questions_9.09_to_9.10.csv", error_bad_lines=False)
print("tset2")
data_text = data[['Body']]
data_text['Index'] = data_text.index
documents = data_text
print("test3")

with open("C:\\Users\\Dsims\\OneDrive\\Desktop\\dictionary.pkl", 'rb') as f:
    dictionary = pickle.load(f)
temp_file = datapath("C:\\Users\\Dsims\\OneDrive\\Desktop\\model")
lda = models.LdaModel.load(temp_file)

processed_body = documents['Body'].map(pre_process)
new_dictionary = corpora.Dictionary(processed_body)
dictionary.merge_with(new_dictionary)
new_dictionary.filter_extremes(no_below=50, no_above=0.5, keep_n=200000)
dictionary.filter_extremes(no_below=50, no_above=0.5, keep_n=200000)
with open("C:\\Users\\Dsims\\OneDrive\\Desktop\\dictionary.pkl", 'wb') as f:
    pickle.dump(dictionary, f, pickle.HIGHEST_PROTOCOL)

bow_corpus = [dictionary.doc2bow(doc) for doc in processed_body]
tfidf = models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]

##error here "IndexError: index 4783 is out of bounds for axis 1 with size 4783"
lda.update(corpus_tfidf, passes=4)

for idx, topic in lda.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))
lda.save(temp_file)