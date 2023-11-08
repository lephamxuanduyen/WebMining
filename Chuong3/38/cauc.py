import nltk
import re
import os

nltk.download('stopwords')
nltk.download('punkt')


from nltk.probability import FreqDist
from nltk.corpus import stopwords


#Read file text
path=os.path.dirname(__file__)
f = open(path+r"\cau1.txt", "r", encoding="utf-8")
text=f.read()

#################################
######## Text Processing ########
#################################
text_pre=text.replace("\n","")  # Remove the newline command
text_pre=text.lower() # Convert text to lowercase
text_pre=re.sub(r'[^\w\s]','',text_pre) # Remove punctuation
text_pre = re.sub("\d+", " ", text_pre) # Remove number
text_pre = re.sub(r"[!@#$[]()]'", "", text_pre) # Remove character: !@#$[]()
stop = stopwords.words('english')   # Remove StopWords
text_pre = " ".join(text_pre for text_pre in text_pre.split() if text_pre not in stop)
text_pre=nltk.word_tokenize(text_pre) # Tokenizing


#################################
##### Exploring Text Data #######
#################################
#print("List of Datasets:",text_pre)
print("Number of words: ",len(text_pre))

# Compute the frequency of all words
frequency_dist = FreqDist(word.lower() for word in text_pre)

## show only th top 50 results
print(frequency_dist.most_common(50))

