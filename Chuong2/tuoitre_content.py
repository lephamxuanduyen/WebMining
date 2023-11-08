import requests
import re
import os
from bs4 import BeautifulSoup
from urllib.parse import urlsplit

file_store = 'F:\Web_Mining\Chuong2\crawl_tuoitre\content'
url_fileRSS= 'https://tuoitre.vn/rss/kinh-doanh.rss'

domain = urlsplit(url_fileRSS).netloc

def url_to_filename(url):
    url = str(url).strip().replace(' ','_')
    return re.sub(r'(?u)[^-\w.]','',url) + '.txt'

def save_toTXT(url):
    print('Saving file...')

    html = requests.get(url).text
    soup = BeautifulSoup(html,'html5lib')

    try:
        Title = soup.find("h1",class_="detail-title article-title")
        Author = soup.find("div",class_="author-info")
        desc = soup.find("h2",class_="detail-sapo")
        detail = soup.find("div",class_="detail-content afcbc-body")
        content = Title.text + '\n' + Author.text + '\n' + desc.text + '\n' + detail.text

        filname = os.path.join(file_store,url_to_filename(url))
        with open(filname,'w',encoding='utf-8') as f:
            f.write(content)
    finally:
        return
    
def visit(url):
    print('**Now visiting:',url)
    save_toTXT(url)

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

links_todo = getURL_from_fileRSS(url_fileRSS)
while links_todo:
    url_to_visit = links_todo.pop()
    next_link = visit(url_to_visit)