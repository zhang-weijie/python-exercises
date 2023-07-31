def find_ids(filein,fileout):  #给一个页面的链接，返回所有图片地址组成的列表
    with open(filein, 'r',encoding='UTF-8') as f:    
        html = f.read()
    #print(html)
    img_ids = []  #声明一个保存图片地址的列表
    
    #查找图片地址
    #加密的网页破解后得到的图像在这里：
    #<img src="http://ww3.sinaimg.cn/mw600/006XNEY7gy1fy66dacugfj30qh0zkdhu.jpg" 
    #所以要先找jpg，然后找img src=
    
    a = html.find('/detail?id=')
    #print(a)
    while a != -1:
        b = html.find('"', a) #在 a-100 到 a区间找 'img src='，必须反向查找
        #print(b)
        #如果 b 找不到，b 就返回 -1        
        if b != -1:                        
            img_ids.append(html[a+11: b])
            
        a = html.find('/detail?id=', b)
        a = html.find('/detail?id=', a+1)
    
    
    with open(fileout,'w') as f:
        f.write('[')
        for each in img_ids:
            f.write(''.join(['"',each,'"',',','\n'])) 
        f.write(']')
    print(len(img_ids))
    '''
    for each in img_ids:
       print(each)
    print('print done')
    '''
if __name__ == '__main__':
    #print('main starts')
    find_ids('wyCrawlerPage2.html','wyCrawlerIds3.txt')
