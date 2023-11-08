from selenium import webdriver
import os
import re

fileStore = 'F:\html'

with open('cau2.txt','r') as f:
    link_pages = f.read().split('\n')

def url_to_file_name(url):
    url = str(url).strip().replace(' ','_')
    return re.sub(r'(?u)[^-\w.]','',url)+'.html'

for link in link_pages:
    driver = webdriver.Chrome()
    driver.get(link)
    
    filename = os.path.join(fileStore,url_to_file_name(link))
    with open(filename,'w',encoding='utf-8') as f:
        f.write(driver.page_source)
    