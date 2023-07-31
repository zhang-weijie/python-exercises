def int_input(file_name):
    try:
        f=open('D:\\'+file_name+'.txt')
        print(f.read())
        f.close()
    except OSError:
        file_name=input('输入错误，请重新输入：')
        int_input(file_name)

file_name=input('请输入文件名：')
int_input(file_name)
