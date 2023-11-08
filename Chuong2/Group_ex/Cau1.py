url = 'http://baovanhoa.vn/kinh-te/doanh-nghiep'

links_todo = [url]

for i in range(2,93):
    link = 'http://baovanhoa.vn/kinh-te/doanh-nghiep/pgrid/591/pageid/' + str(i)
    links_todo += [link]

import os

str = ''
for i in links_todo:
    str += i + '\n'
filename = os.path.join('F:\Web_Mining\Chuong2\Group_ex','Cau1.txt')
with open(filename,'w',encoding='utf-8') as f:
    f.write(str)