import nltk
import re
import os

nltk.download('stopwords')
nltk.download('punkt')


from nltk.probability import FreqDist
from nltk.corpus import stopwords

#Read file text
path=os.path.dirname(__file__)
f = open(path+r"\1_txl.txt", "r", encoding="utf-8")
text=f.read()

text_pre=nltk.word_tokenize(text) # Tokenizing

#################################
##### Exploring Text Data #######
#################################
#print("List of Datasets:",text_pre)
print("Number of words: ",len(text_pre))

# Compute the frequency of all words
frequency_dist = FreqDist(word.lower() for word in text_pre)

## show only th top 50 results
print(frequency_dist.most_common(50))
