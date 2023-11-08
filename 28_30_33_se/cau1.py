links =['http://baovanhoa.vn/kinh-te/doanh-nghiep']
for i in range(2,94):
    link = 'http://baovanhoa.vn/kinh-te/doanh-nghiep/pgrid/591/pageid/'+str(i)
    links += [link]
for i in links:
    print(i, end='\n')


    with open("cau1.txt","a") as f:
        f.writelines(i+'\n')