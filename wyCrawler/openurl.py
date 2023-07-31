from selenium import webdriver
import time

def url_open_jm(url):   #返回加密网页的源码(速度慢）
    chrome = webdriver.Chrome()
    chrome.get(url)
    time.sleep(5)
    

def open_urls(file):
    #with open(file, 'r',encoding='UTF-8') as f:
    for line in open(file, 'r',encoding='UTF-8'):
        url = ''.join(['https:','//www.wyav.tv/play?id=',line])
        print(url)
        url_open_jm(url)
        time.sleep(6)
    

if __name__ == '__main__':
    open_urls('wyCrawlerIds3.txt')