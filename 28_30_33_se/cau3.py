from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

with open('cau1.txt','r') as f:
    list_todo = f.read().split('\n')
str = ''
for link in list_todo:
    driver = webdriver.Chrome()
    driver.get(link)
    articles=driver.find_elements(By.CSS_SELECTOR,'article.edn_article')
    for article in articles:
        try:
            title =article.find_element(By.TAG_NAME,'a').text
            time = article.find_element(By.TAG_NAME,'time').text
            desc = article.find_element(By.CLASS_NAME,'edn_articleSummary').text
            print(title)
            print(time)
            print(desc)
            print('------')
            str += title + '\n' + time + '\n' + desc + '\n' + '=============' + '\n'
            with open('cau3.txt','a',encoding='utf-8') as f:
                f.writelines(str)
                
        except NoSuchElementException: 
            pass	
    driver.close()
    