import requests
import os
from bs4 import BeautifulSoup

url = "https://philong.com.vn/may-tinh-xach-tay.html"
html = requests.get(url).text

soup = BeautifulSoup(html,'html5lib')

TenMay = soup.find_all("h4", class_="p-name line-clamp-2")
MoTa   = soup.find_all("div", class_="p-summary")
Price  = soup.find_all("span", class_="p-price")
Promo  = soup.find_all("span", class_="p-promotion")

str=""
for i in range(len(TenMay)):
    str+=TenMay[i].text + "\n"
    str+="Mô tả:" + "\n" +MoTa[i].text + "\n"
    str+="Giá: "+Price[i].text + "\n"
    str+=Promo[i].text + "\n"
    str+="==============================="

filename=os.path.join("F:\Web_Mining\Chuong2\ScrapingPhilong", "content_LapTop.txt")    
with open(filename, 'w',encoding='utf-8') as f:
    f.write(str)