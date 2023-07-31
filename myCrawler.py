import os
from selenium import webdriver
import urllib.request
 
def url_open(url):  #返回普通不加密网页的源码(速度快)
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0')
        response = urllib.request.urlopen(url)
        html = response.read()
        return html
 
def url_open_jm(url):   #返回加密网页的源码(速度慢）
        chrome = webdriver.Firefox()
        chrome.get(url)
        html = chrome.page_source
        return html #返回的就是字符串
       
'''
def get_page(url): #得到最新页面的页码数(可以使用不加密读码得到，为了加快速度)
        html = url_open(url)
        
        #然后就是查找 html 中的 'current-comment-page'
        a = html.find( 'current-comment-page') + 23  #加上 23 位偏移就刚到到页码数的第一位数字
        b = html.find(']', a)  #找到 a 位置之后的第一个方括号所在位置的索引坐标
                
        return html[a : b]  #这就是最新的页码数啦
'''
def get_page(url): #得到最新页面的页码数
        html = url_open(url)
        html = html.decode('utf-8') #因为要以字符串的形式查找，所以要 decode
 
        #然后就是查找 html 中的 'current-comment-page'
        a = html.find('current-comment-page') + 23  #加上 23 位偏移就刚到到页码数的第一位数字
        b = html.find(']', a)  #找到 a 位置之后的第一个方括号所在位置的索引坐标
               
        return html[a : b]  #这就是最新的页码数啦
 
def find_imgs(url):  #给一个页面的链接，返回所有图片地址组成的列表
        html = url_open_jm(url)  #这个必须使用加密打开的方式
        
        img_addrs = []  #声明一个保存图片地址的列表
        
        #查找图片地址
        #加密的网页破解后得到的图像在这里：
        #<img src="http://ww3.sinaimg.cn/mw600/006XNEY7gy1fy66dacugfj30qh0zkdhu.jpg" 
        #所以要先找jpg，然后找img src=
        
        a = html.find('.jpg') 
        while a != -1:
                b = html.rfind('img src=', a-100, a) #在 a-100 到 a区间找 'img src='，必须反向查找
                
                #如果 b 找不到，b 就返回 -1        
                if b != -1:                        
                        img_addrs.append(html[b+9: a+4])
                
                a = html.find('.jpg', a+4)
        for each in img_addrs:
                print(each)
 
        return img_addrs               
                
def save_imgs(folder, img_addrs):
        for each in img_addrs:
                filename = each.split('/')[-1]
                with open(filename, 'wb') as f:
                        img = url_open(each)
                        f.write(img)
 
def download_figures(folder = r'C:\developmentTools\Lecture\Python\myPython\myExercises\myDownloads\figures5', page = 2):
        os.mkdir(folder)  #创建文件夹
        os.chdir(folder)
 
        url = r"http:/jandan.net/girl"  #随手拍栏目的链接，也是最新页面的链接
        page_num = int(get_page(url)) #得到最新页面的页码数
 
        for i in range(page):
        
                page_url = url + 'page-' + str(page_num) + '#comments'  #得到要爬取的页面的链接
                print(page_url)
                img_addrs = find_imgs(page_url)  #得到页面所有图片的地址，保存为列表
                save_imgs(folder, img_addrs)  #保存图片到本地文件夹
                page_num -= 1  #逐步找到前几个页面
 
if __name__ == '__main__':
        download_figures()
