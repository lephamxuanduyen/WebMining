import requests
import re
import os
from bs4 import BeautifulSoup
from urllib.parse import urlsplit

# Lấy link các bài báo
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

# Lấy file html của mỗi bài báo

file_store = 'F:\Web_Mining\Chuong2\Group_ex_bai4_html'

def url_to_filename(url):
    url = str(url).strip().replace(' ','_')
    return re.sub(r'(?u)[^-\w.]','',url) + '.html'

def download(url):
    print('Saving...')

    content = requests.get(url).text

    filename = os.path.join(file_store,url_to_filename(url))
    with open(filename,'w',encoding='utf-8') as f:
        f.write(content)

def visit(url):
    print('**Now visiting:',url)
    download(url)

while link_seen:
    link_to_visit = link_seen.pop()
    nextlink = visit(link_to_visit)