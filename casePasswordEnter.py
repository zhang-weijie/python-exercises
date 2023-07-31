rightcode='我爱你'
code=input('请输入密码：')
while True:
    for i in code:
        if i=='*':
            break
        print('密码中不能含有“*”号')
        code=input('请重新输入：')
    while True:
        while True:
            if code==rightcode:
                break
            code=input('密码输入错误，您还有2次机会！请输入密码：')
        if code==rightcode:
            break
        code=input('密码输入错误，您还有一次机会！请输入密码：')
print('密码正确，进入程序...')

