import requests
import re
import os 
from urllib.parse import urlsplit

file_store = "F:\Web_Mining\Chuong2\crawl_tinhte\html"
url_fileRSS= "https://tuoitre.vn/rss/kinh-doanh.rss"

domain = urlsplit(url_fileRSS).netloc

def url_to_filename(url):
    url = str(url).strip().replace(' ','_')
    return re.sub(r'(?u)[^-\w]','',url) + '.html'

def download(url):
    print('Saving...')
    content = requests.get(url).text

    filename = os.path.join(file_store,url_to_filename(url))
    with open(filename,'w',encoding='utf-8') as f:
        f.write(content)

def visit(url):
    print('**Now visiting:',url)
    download(url)

def getURL_from_fileRSS(url_fileRSS):
    xml = requests.get(url_fileRSS).text
    links = re.findall('<a href="(.*?)">',xml)

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

link_todo = getURL_from_fileRSS(url_fileRSS)

while link_todo:
    url_to_visit = link_todo.pop()
    print(url_to_visit)
    next_link = visit(url_to_visit)