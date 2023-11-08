import os
import re
from bs4 import BeautifulSoup
import nltk
from emot.emo_unicode import UNICODE_EMOJI # For emojis
from emot.emo_unicode import EMOTICONS_EMO # For EMOTICONS
from textblob import TextBlob
from nltk.corpus import stopwords

lookup_dict = {'nlp':'natural language processing', 'ur':'your', "wbu" : "what about you"}

def text_std(input_text):
    words = input_text.split()
    # Get Abbreviations Words
    text_pre=""
    for word in words:
        w=word
        w = re.sub(r'[^\w\s]','',w) #Removing Punctuation
        if w.lower() in lookup_dict:
            word=lookup_dict[w]
        text_pre=text_pre + " " + word        
    return text_pre
 
# Function for converting emojis into word
def converting_emojis(text):
    for x in EMOTICONS_EMO:
        text = text.replace(x, "_".join(EMOTICONS_EMO[x].replace(",","").replace(":","").split()))
        
    for x in UNICODE_EMOJI:
        text = text.replace(x, "_".join(UNICODE_EMOJI[x].replace(",","").replace(":","").split()))
            
    return text

file_store = 'F:\Web_Mining\Chuong3\content'
file_kq = 'F:\Web_Mining\Chuong3\solve'

def remove_tags(html):
    # parse html content
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['style', 'script']):
        data.decompose() # Remove tags
    return ' '.join(soup.stripped_strings)
for i in range(1,79):
    f = open(os.path.join(file_store, "1.txt"), "r")
    data = f.read()
    data_pre = data.lower()
    data_pre = re.sub("\d+", " ", data_pre)
    sentence_list = nltk.sent_tokenize(data_pre)
    for sen in sentence_list:
        sen=re.sub(r'[^\w\s]','',sen)
        sen=converting_emojis(sen)
        stop = stopwords.words('english')
        sen = " ".join(text for text in sen.split() if text not in stop)
        sen=text_std(sen)
        sen=TextBlob(sen).correct()
        sen=sen.split(" ")
        sen.remove("")
        print(sen)

        content = ""
        for x in sen:
            content+= x + "\n"
        
        filename = os.path.join(file_kq,str(i)+'x.txt')
        with open(filename,'w',encoding='utf-8') as f:
            f.write(content)