import requests
import re

url = 'http://baovanhoa.vn/kinh-te/doanh-nghiep'

links_page = [url]
link_seen  = []

for i in range(2,93):
    link = 'http://baovanhoa.vn/kinh-te/doanh-nghiep/pgrid/591/pageid/' + str(i)
    links_page += [link]

def getlink(url_visit):
    print('**Now visiting:',url_visit)

    html = requests.get(url_visit).text
    nextLinks = re.findall('<h2 class="edn_articleTitle"><a href="(.*?)" target="_self">',html)

    for link in nextLinks:
        if link not in links_page and link not in link_seen and link != url_visit:
            link_seen.append(link)

    if links_page:
        getlink(links_page.pop())
    else:
        return
    
getlink(links_page.pop())

import os
str = ''
for i in link_seen:
    str += i + '\n'
filename = os.path.join('F:\Web_Mining\Chuong2\Group_ex','Cau2.txt')
with open(filename,'w',encoding='utf-8') as f:
    f.write(str)