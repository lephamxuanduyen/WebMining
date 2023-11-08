import requests
import os
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
html = requests.get(url).text

soup = BeautifulSoup(html,'html5lib')
content = soup.find_all("p", class_="")
str=""
for i in range(len(content)):
    str += content[i].text + " "

filename=os.path.join("F:\Web_Mining\Chuong3\38", "cau1.txt")    
with open(filename, 'w',encoding='utf-8') as f:
    f.write(str)