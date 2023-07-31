import urllib.request
import os

pagedict = { }
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('Usr-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_page(url,pages=2):
    html = url_open(url).decode('utf-8')
    a = html.find('//jandan.net/ooxx/',0)
    b = html.find('">', a)
    c = html.find('</a>', b)
    page = 'http:'+ html[a:b]
    pagenum = html[b+2:c].strip()
    pagedict.update({pagenum:page})
    print(pagedict)
    for i in range(pages):
        a = html.find('//jandan.net/ooxx/',c)
        b = html.find('">', a)
        c = html.find('</a>', b)
        page = 'http:'+ html[a:b]
        pagenum = html[b+2:c].strip()
        pagedict.update({pagenum:page})
        print(pagedict)
        
def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        print('http:' + each)
        with open(filename, 'wb') as f:
            img = url_open('http:' + each)
            f.write(img)

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            print('%s'%html[a+9 : b+4])
            img_addrs.append(html[a+9 : b+4])
        else:
            b = a + 9
        a = html.find('img src=', b)
    for each in img_addrs:
        print(each)
    return img_addrs


def download_mm(folder='OOXX',pages=2):
    os.mkdir(folder)
    os.chdir(folder)
    url = "http://jandan.net/ooxx"
    page_num = get_page(url)
    print(pagedict)
    for key in pagedict:
        page_url = pagedict[key]
        print(page_url)
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__ == '__main__':
    download_mm()

    
    
    
    
