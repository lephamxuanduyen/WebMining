# a. Lấy văn bản

# import re
# import requests
# from bs4 import BeautifulSoup

# url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
# html = requests.get(url).text
# soup = BeautifulSoup(html,"html5lib")
# cont = soup.find_all("p")
# for i in range(len(cont)):
#     with open("F:\DATA\caua.txt","a") as f:
#         f.writelines(cont[i].text)

# b. Chuyển văn bản thành chữ thường

# with open("F:\DATA\caua.txt","r") as f:
#     cnt = f.read()
# cnt = cnt.lower()
# with open("F:\DATA\caub.txt","w") as f:
#     cnt = f.write(cnt)

# c. loại bỏ thẻ html

# with open("F:\DATA\caub.txt","r") as f:
#     cnt = f.read()
# def remove_tags(html):
#     soup = BeautifulSoup(html,"html.parser")
#     for data in soup(['style','script']):
#         data.decompose()
#     return ' '.join(soup.stripped_strings)
# with open("F:\DATA\cauc.txt","a") as f:
#     f.writelines(remove_tags(cnt))

# d. Xóa dấu câu

# import string

# with open("F:\DATA\cauc.txt","r") as f:
#     text = f.read()

# for c in string.punctuation:
#     text = text.replace(c,'')
# text_pre = text
# print(text_pre)
# with open("F:\DATA\caud.txt","w") as f:
#     f.writelines(text_pre)

# e. Xóa chữ số

# with open("F:\DATA\caud.txt","r") as f:
#     text = f.read()

# text_pre = re.sub("\d", " ", text )
# with open("F:\DATA\caue.txt","w") as f:
#     f.writelines(text_pre)

# Tách câu
# f. Chuyển biểu tượng cảm xúc thành văn bản
# from emot.emo_unicode import UNICODE_EMOJI
# from emot.emo_unicode import EMOTICONS_EMO

# def convert_emo(text):
#     for x in EMOTICONS_EMO:
#         text = text.replace(x, "_".join(EMOTICONS_EMO[x].replace(",","").replace(":","").split()))
#     for x in UNICODE_EMOJI:
#         text = text.replace(x, "_".join(UNICODE_EMOJI[x].replace(",","").replace(":","").split()))
#     return text

# with open("F:\DATA\caue.txt","r") as f:
#     text = f.read()

# with open("F:\DATA\cauf.txt","w") as f:
#     f.writelines(convert_emo(text))

# g. Xóa các từ không có nghĩa

# from nltk.corpus import stopwords

# with open("F:\DATA\cauf.txt","r") as f:
#     text = f.read()
# stop = stopwords.words('english')
# text_pre = " ".join(text for text in text.split() if text not in stop)

# with open("F:\DATA\caug.txt","a") as f:
#     f.writelines(text_pre)

# Chuẩn hóa văn bản
# h. Sửa lỗi chính tả

# from textblob import TextBlob

# with open("F:\DATA\caug.txt","r") as f:
#     text = f.read()
# with open("F:\DATA\cauh.txt","a") as f:
#     f.writelines(TextBlob(text).correct())

# Tách từ

# import nltk
# from nltk.stem import WordNetLemmatizer
# from nltk.probability import FreqDist

# with open("F:\DATA\cauh.txt","r") as f:
#     text = f.read()
# words = nltk.word_tokenize(text)

# # Chuẩn hóa từ

# lemmatizer = WordNetLemmatizer()

# for i in range(len(words)):
#     words = [lemmatizer.lemmatize(word) for word in words]

# # Khám phá dữ liệu văn bản
# print("===================")
# print("Số từ:", len(words))
# frequency_dict = FreqDist(word.lower() for word in words)
# print(frequency_dict.most_common(50))

# large_words = dict([(k,v) for k,v in frequency_dict.items() if len(k)>3])
# frequency_dict = nltk.FreqDist(large_words)
# frequency_dict.plot(50,cumulative=False)

# from wordcloud import WordCloud
# wcloud = WordCloud().generate_from_frequencies(frequency_dict)
# #plotting the wordcloud
# import matplotlib.pyplot as plt
# plt.imshow(wcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()

# import pandas as pd
# # Danh sách các từ trong văn bản
# text="We are learning Natural Language Processing"
# words=text.split()
# # Tạo DataFrame từ danh sách các từ
# df = pd.DataFrame({'word': words})
# # Thực hiện one-hot encoding
# one_hot = pd.get_dummies(df['word'])
# # Ghép kết quả vào DataFrame gốc
# df = pd.concat([df, one_hot], axis=1)
# print(df)

# from functools import reduce

# # Dau vao la 2 cau van ban
# Data = ["The quick brown fox jumps over the lazy dog and",
#         "Never jump over the lazy dog quickly"]

# # B1. Tach tu
# texts=[]
# for x in Data:
#     texts.append([text for text in [x for x in x.lower().split()]])

# # B2: Xay dung tu dien
# dictionary = sorted(list(set(reduce(lambda x, y: x + y, texts))))
# print("Words in dictionary:",dictionary)

# # B3: Xay dung vector BOW
# def bag_of_word(sentence):
#     vector = []

#     # Dem cac tu trong cau xuat hien trong tu dien.
#     for word in dictionary:
#         count = 0        
        
#         # Dem so tu xuat hien trong cau.
#         for w in sentence:
#             if w == word:
#                 count += 1
#         vector.append(count)
#     return vector
            
# print("Vector Bag-of-Word:")
# for sentence in texts:
#     print(bag_of_word(sentence))

# from sklearn.feature_extraction.text import CountVectorizer

# # Dau vao la 2 cau van ban
# Data = ["The quick brown fox jumps over the lazy dog and",
#         "Never jump over the lazy dog quickly"]

# # Xay dung vector BOW
# vect = CountVectorizer()
# X = vect.fit_transform(Data)

# # Xay dung tu dien
# dictionary=list(vect.get_feature_names_out())

# print("Words in dictionary: ", dictionary)
# print("Vector Bag-of-Word: \n", X.toarray())
