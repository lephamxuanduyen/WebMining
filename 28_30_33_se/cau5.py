from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import re

fileStore = 'F:\content'

with open('cau2.txt','r') as f:
    link_pages = f.read().split('\n')

def url_to_file_name(url):
    url = str(url).strip().replace(' ','_')
    return re.sub(r'(?u)[^-\w.]','',url)+'.txt'

for link in link_pages:
    driver = webdriver.Chrome()
    driver.get(link)
    
    title = driver.find_element(By.TAG_NAME,'h1').text
    time = driver.find_element(By.CLASS_NAME,'edn_metaDetails1').text
    decs = driver.find_element(By.CLASS_NAME,'Detail_Summary').text
    detail = driver.find_element(By.CLASS_NAME,'main_content').text
    output = title + '\n' + time + '\n' + decs + '\n' + detail
    filename = os.path.join(fileStore,url_to_file_name(link))
    with open(filename,'w',encoding='utf-8') as f:
        f.write(output)
    driver.close()