import requests
import re
import os
from urllib.parse import urlsplit

file_store = "F:\Web_Mining\Chuong2\crawl_vnexpress\html"
url_fileRSS="https://vtc.vn/rss/suc-khoe.rss"

domain = urlsplit(url_fileRSS).netloc

def url_to_file_name(url):
    url = str(url).strip().replace(' ','_')
    return re.sub(r'(?u)[^-\w]','',url) + ".html"

def download(url):
    print("Saving file,...")
    content = requests.get(url).text
    
    filename = os.path.join(file_store,url_to_file_name(url))
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def visit(url):
    print("**Now visiting:",url)
    download(url)

def getURL_from_fileRSS(url_fileRSS):
    xml = requests.get(url_fileRSS).text
    links = re.findall('<link>(.*?)</link>',xml)

    link_todo=[]
    for link_url in links:
        if link_url is None:
            continue
        if urlsplit(link_url).netloc != domain:
            continue
        if link_url in link_todo:
            continue

        link_todo.append(link_url)

    return link_todo

links_todo = getURL_from_fileRSS(url_fileRSS)

while links_todo:
    url_to_visit = links_todo.pop()
    print(url_to_visit)
    new_link = visit(url_to_visit)
