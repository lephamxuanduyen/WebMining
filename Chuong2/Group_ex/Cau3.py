import requests
import os 
from bs4 import BeautifulSoup

url = 'http://baovanhoa.vn/kinh-te/doanh-nghiep'

links_todo = [url]

for i in range(2,93):
    link = 'http://baovanhoa.vn/kinh-te/doanh-nghiep/pgrid/591/pageid/' + str(i)
    links_todo += [link]
str = ""
for i in links_todo:
    print('**Now visiting:',i)
    html = requests.get(i).text
    soup = BeautifulSoup(html,'html5lib')

    Title = soup.find_all('h2',class_='edn_articleTitle')
    Desc = soup.find_all('div',class_='edn_articleSummary')
    Time = soup.find_all('div',class_='edn_metaDetails')

    for x in range(len(Title)):
        str += '+ ' +Title[x].text + '\n'
        str += '- ' + Desc[x].text + '\n'
        str += '- ' + Time[x].text + '\n'

filename = os.path.join('F:\Web_Mining\Chuong2\Group_ex','Cau3.txt')
with open(filename,'w',encoding='utf-8') as f:
    f.write(str)