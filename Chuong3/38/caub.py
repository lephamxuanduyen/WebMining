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

str=""
for i in text_pre:
    str+=i+' '

filename=os.path.join("F:\Web_Mining\Chuong3", "cau1_txl.txt")    
with open(filename, 'w',encoding='utf-8') as f:
    f.write(str)