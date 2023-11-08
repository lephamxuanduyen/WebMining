import requests
import re
import os
from bs4 import BeautifulSoup

url = 'https://edition.cnn.com/business'

link_seen = []
file_store = 'F:\Web_Mining\Chuong3\content'

html = requests.get(url).text
links = re.findall('<a href="(/2.*?)" ',html)

for link in links:
    if link not in link_seen and link != url:
        url_link = "https://edition.cnn.com"+link
        link_seen += [url_link]

i=1
for link in link_seen:
    print('Saving file...')

    html1 = requests.get(link).text
    soup = BeautifulSoup(html1,'html5lib')

    title = soup.find('h1')
    time  = soup.find('div',class_='headline__sub-text')
    detail  = soup.find('div',class_='article__content-container')

    content = title.text + '\n' + time.text + '\n' + '\n' + detail.text

    filename = os.path.join(file_store,str(i)+'.txt')
    with open(filename,'w',encoding='utf-8') as f:
        f.write(content)
    
    i+=1
print('----------------------------------')
print('Đã tìm thấy',len(link_seen),'link')