import urllib.request as ur

def getkitten(image_size):
    responde=ur.urlopen('http://placekitten.com/g'+image_size)
    cat_image=responde.read()

    with open('C:\\安装应用\\Python学习\\练习\\cat.jpg','wb') as f:
        f.write(cat_image)

image_size=input('请按【/000/000】格式输入图片大小：')
getkitten(image_size)
