import requests
import re
import os
from bs4 import BeautifulSoup
# Cách 2: Dựa trên quy tắc cấu trúc url để tạo link
url="https://truyenfull.vn/the-loai/kiem-hiep"
Links_ToDo=[url]
for i in range(2,36):
    Link="https://truyenfull.vn/the-loai/kiem-hiep/trang-" + str(i) + "/"
    Links_ToDo += [Link]
Links_ToDo.append("https://truyenfull.vn/the-loai/kiem-hiep") 

str=""
for i in Links_ToDo:
    url=i
    html = requests.get(url).text
    #Tối ưu hóa code HTML bằng thư viện html5lib
    soup = BeautifulSoup(html, 'html5lib')
    #Sử dụng thư viện BeautifulSoup để bóc tách dữ liệu
    Ten = soup.find_all("h3",class_="truyen-title")
    TacGia = soup.find_all("span",class_="author")
    Chuong = soup.find_all("div",class_="text-info")
    for i in range(len(Ten)):
        str+=Ten[i].text + "\n"
        str+="- " + TacGia[i].text + "\n"
        str+="- " + Chuong[i].text + "\n"
filename=os.path.join("F:\Web_Mining\Chuong2\ScrapingTruyenfull", "TruyenFull.txt")    
with open(filename, 'w',encoding='utf-8') as f:
    f.write(str)
