import requests
import re
import os
from bs4 import BeautifulSoup
from urllib.parse import urlsplit

file_store = 'F:\Web_Mining\Chuong2\crawl_cafebiz\content'
url_fileRSS= 'https://cafebiz.vn/rss/xa-hoi.rss'

domain = urlsplit(url_fileRSS).netloc

def url_to_filename(url):
    url = str(url).strip().replace(' ','_')
    return re.sub(r'(?u)[^-\w.]','',url) + '.txt'

def save_toTXT(url):
    print('Saving file...')

    html = requests.get(url).text
    soup = BeautifulSoup(html,'html5lib')

    try:
        Title = soup.find('h1',class_='title')
        Time  = soup.find('span',class_='time')
        Desc  = soup.find('h2',class_='sapo')
        detail= soup.find('div',class_='detail-content')

        content = Title.text + '\n' + Time.text + '\n' + Desc.text + '\n' + detail.text

        filename = os.path.join(file_store,url_to_filename(url))
        with open(filename,'w',encoding='utf-8') as f:
            f.write(content)
    finally:
        return
    
def visit(url):
    print('**Now visting:',url)
    save_toTXT(url)

def getURL_from_fileRSS(url_fileRSS):
    xml = requests.get(url_fileRSS).text
    links = re.findall('<link>(.*?)</link>',xml)

    links_todo = []
    for url_link in links:
        if url_link is None:
            continue
        if urlsplit(url_link).netloc != domain:
            continue
        if url_link in links_todo:
            continue

        links_todo.append(url_link)

    return links_todo

links_todo = getURL_from_fileRSS(url_fileRSS)

while links_todo:
    url_to_visit = links_todo.pop()
    next_link    = visit(url_to_visit)