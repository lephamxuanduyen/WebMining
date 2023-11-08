import re
import os
import requests

url="https://websosanh.vn/laptop/cat-18.htm"
html = requests.get(url).text
# soup = BeautifulSoup(html,'html5lib')

Ten=re.findall('<h3><a.*?">(.*?)</a></h3>', html)
Gia=re.findall('<span class="product-price".*?>(.*?)</span>', html)
noi=re.findall('<span class="product-bottom"><span class="product-store.*?">(.*?)</span>', html)
str=""
for i in range(len(Ten)):
    str+=Ten[i]+ "\n"
    str+="- " + Gia[i] + "\n"    
    str+="- " + noi[i] + "\n"
filename=os.path.join("F:\Web_Mining\Chuong2\ScrapingWebsosanh", "laptop.txt")     
with open(filename, 'w',encoding='utf-8') as f:
    f.write(str)