from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

with open('cau1.txt','r') as f:
    list_todo = f.read().split('\n')

for link in list_todo:
    driver = webdriver.Chrome()
    driver.get(link)
    articles=driver.find_elements(By.CSS_SELECTOR,'article.edn_clearFix')
    for article in articles:
        try:
            title =article.find_element(By.TAG_NAME,'a').text
            url = article.find_element(By.CSS_SELECTOR, 'h2.edn_articleTitle > a').get_attribute('href')
            print(title)
            print(url)
            print('------')
            with open('cau2.txt','a') as f:
                f.writelines(url+'\n')
        except NoSuchElementException: 
            pass	
    driver.close()