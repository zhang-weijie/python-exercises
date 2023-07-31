def Fun():
    print('新建用户：N\n登录账号：E\n退出程序:Q')
    dict1={}

    while True:
        code=input('请输入指令代码：')
        if code=='N':
            newname=input('请输入用户名：')
            while newname in dict1:
                newname=input('此用户名已被使用，请重新输入:')
                continue                
            newpasswd=input('请输入密码：')
            dict1[newname]=newpasswd
            print('新建用户成功，赶快登陆吧！')

        if code=='E':
            name=input('请输入用户名：')
            while name not in dict1:
                name=input('该用户不存在，请重新输入：')
                continue
            passwd=input('请输入密码：')
            while passwd!=dict1[name]:
                passwd=input('密码错误，请重新输入：')
                continue
            print('登陆成功！')
            break
        if code=='Q':
            print('退出程序...')
            break
Fun()
