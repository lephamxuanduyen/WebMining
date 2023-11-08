# import requests
# import os
# from bs4 import BeautifulSoup

# url="https://phongtro123.com/tinh-thanh/da-nang"
# html = requests.get(url).text
# #Tối ưu hóa code HTML bằng thư viện html5lib
# soup = BeautifulSoup(html, 'html5lib')
# #Sử dụng thư viện BeautifulSoup để bóc tách dữ liệu
# TieuDe = soup.find_all("h3",class_="post-title")
# DonGia = soup.find_all("span",class_="post-price")
# DienTich = soup.find_all("span",class_="post-acreage")
# DiaChi = soup.find_all("span",class_="post-location")
# NgayDang = soup.find_all("time",class_="post-time")
# str=""
# for i in range(len(TieuDe)):
#     str+=TieuDe[i].text + "\n"
#     str+="- " + DonGia[i].text + "\n"
#     str+="- " + DienTich[i].text + "\n"
#     str+="- " + DiaChi[i].text + "\n"
#     str+="- " + NgayDang[i].text

# filename=os.path.join("F:\Web_Mining\Chuong2\ScrapingNhatro123BS", "PhongTro123.txt")    
# with open(filename, 'w',encoding='utf-8') as f:
#     f.write(str)


import requests
import os
from bs4 import BeautifulSoup

url="https://tapchinganhang.gov.vn/chinh-sach.htm?fbclid=iwar050azhvr7vpwq0d6aktlcipwf-sm-0jsuq03bygkkaoy77l0ciaqcv8fq"
html = requests.get(url).text
#Tối ưu hóa code HTML bằng thư viện html5lib
soup = BeautifulSoup(html, 'html5lib')
#Sử dụng thư viện BeautifulSoup để bóc tách dữ liệu
title = soup.find_all('a',class_='title')
# time  = soup.find('div',class_='edn_metaDetails1')
# desc  = soup.find('div',class_='Detail_Summary')
# detail= soup.find('div',class_='main_content')

for i in title:
    print(i.text,'\n')
# str=""
# for i in range(len(Title)):
#     str+=Title[i].text + "\n"
#     str+="- " + Time[i].text + "\n"
#     str+="- " + Detail[i].text

# filename=os.path.join("F:\Web_Mining\Chuong2\ScrapingNhatro123BS", "kiemtra.txt")    
# with open(filename, 'w',encoding='utf-8') as f:
#     f.write(str)