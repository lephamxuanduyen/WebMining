import requests
import re
import os
from bs4 import BeautifulSoup

url = 'http://baovanhoa.vn/kinh-te/doanh-nghiep'

link_seen = [url]
link_page = []

for i in range(2,93):
    link = 'http://baovanhoa.vn/kinh-te/doanh-nghiep/pgrid/591/pageid/' + str(i)
    link_page += [link]

def getLink(url):
    print('**Now visiting:',url)

    html1 = requests.get(url).text
    links = re.findall('<h2 class="edn_articleTitle"><a href="(.*?)" target="_self">',html1)

    for link in links:
        if link not in link_seen and link not in link_page and link != url:
            link_seen.append(link)

    if link_page:
        getLink(link_page.pop())
    else:
        return
    
getLink(link_page.pop())
def url_to_filename(url):
    url = str(url).strip().replace(' ','_')
    return re.sub(r'(?u)[^-\w.]','',url) + '.txt'

file_store = 'F:\Web_Mining\Chuong3\Group_ex'

def save_toTXT(url):
    print('Saving file...')

    html = requests.get(url).text
    soup = BeautifulSoup(html,'html5lib')
    try:
        title = soup.find('h1')
        time  = soup.find('div',class_='edn_metaDetails1')
        desc  = soup.find('div',class_='Detail_Summary')
        detail= soup.find('div',class_='main_content')

        content = title.text + '\n' + time.text + '\n' + desc.text + '\n' + detail.text

        filename = os.path.join(file_store,url_to_filename(url))
        with open(filename,'w',encoding='utf-8') as f:
            f.write(content)
    finally:
        return

def visit(url):
    print('**Now visiting:',url)
    save_toTXT(url)

while link_seen:
    url_to_visit = link_seen.pop()
    nextLink = visit(url_to_visit)