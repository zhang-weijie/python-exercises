import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import random
import re
def get_urls(polysemantList):
    for each_semant in polysemantList:
        result='%s -> %s'%(each_semant.find_next('a')['title'],''.join(['http://baidu.baike.com',each_semant.find_next('a')['href']]))
        yield result
        
        
        
    

def main():
    keyword=input('请输入要查找的关键词：')
    keyword=urllib.parse.quote(keyword)
    url='https://baike.baidu.com/item/%s'%keyword
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0')
    proxy_addrs=[{'http':'39.137.95.73:8080'},{'http':'39.106.223.134:80'},{'http':'39.137.69.6:8080'}]
    proxy_support=urllib.request.ProxyHandler(random.choice(proxy_addrs))
    opener=urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    response=opener.open(req)
    html=response.read().decode('utf-8')
    soup=BeautifulSoup(html,'html.parser')
    h2=soup.find('h2').string
    text=soup.find('div',class_='para').get_text()
    print('%s\n%s'%(h2,text))
    polysemant_link=soup.find('a',href=re.compile('force=1$'))
    if polysemant_link==None:
        pass
    else:
        print('多义项词，%s'%polysemant_link.string)
        polysemantList_tag=soup.find('ul',class_='polysemantList-wrapper cmn-clearfix')
        polysemantList=polysemantList_tag.find_all('li',class_='item')
        print(polysemantList)

        each_semant=get_urls(polysemantList)
        try:
            for i in range(10):
                print(next(each_semant))
        except StopIteration:
            print('无更多条目！')

if __name__=='__main__':
    main()
