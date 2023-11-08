# Tìm nhà trọ trên nhiều trang

import requests
import re
import os
from bs4 import BeautifulSoup

url="https://phongtro123.com/tinh-thanh/da-nang"
html = requests.get(url).text

def get_LinksbyRegEx(url_visit):
    global Links_ToDo
    print("** Now visiting:",url_visit)
    
    Links_seen.append(url_visit)    
    html = requests.get(url_visit).text
    NextLinks=re.findall('<a class="page-link" href="(.*?)"', html)

    for Link in NextLinks:
        if  Link not in Links_ToDo and Link not in Links_seen:
            Links_ToDo.append(Link)
        
    if Links_ToDo:
        get_LinksbyRegEx(Links_ToDo.pop())
    else:
        return

#Cách 1: Lấy link tự động từ Biểu thức chính quy - Sử dụng thuật toán đệ quy
# Links_ToDo=[url]
# Links_seen=[]
# get_LinksbyRegEx(Links_ToDo.pop())
# print(len(Links_seen), "links found!")
# print(len(Links_ToDo))


#Cách 2: Dựa trên quy tắc cấu trúc url để tạo link
Links_ToDo=[url]
for i in range(2,51):
    Link="https://phongtro123.com/tinh-thanh/da-nang?page=" + str(i)
    Links_ToDo += [Link]
Links_ToDo.append("https://phongtro123.com/tinh-thanh/da-nang") 

str=""
for i in Links_ToDo:
    url=i
    html = requests.get(url).text
    #Tối ưu hóa code HTML bằng thư viện html5lib
    soup = BeautifulSoup(html, 'html5lib')
    #Sử dụng thư viện BeautifulSoup để bóc tách dữ liệu
    TieuDe = soup.find_all("h3",class_="post-title")
    DonGia = soup.find_all("span",class_="post-price")
    DienTich = soup.find_all("span",class_="post-acreage")
    DiaChi = soup.find_all("span",class_="post-location")
    NgayDang = soup.find_all("time",class_="post-time")
    for i in range(len(TieuDe)):
        str+=TieuDe[i].text + "\n"
        str+="- " + DonGia[i].text + "\n"
        str+="- " + DienTich[i].text + "\n"
        str+="- " + DiaChi[i].text + "\n"
        str+="- " + NgayDang[i].text

filename=os.path.join("F:\Web_Mining\Chuong2\ScrapingPhongtro123", "PhongTro123.1.txt")    
with open(filename, 'w',encoding='utf-8') as f:
    f.write(str)