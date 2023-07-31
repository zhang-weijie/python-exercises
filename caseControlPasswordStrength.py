symbols = r'`!@#$%^&*()_=-/,.?<>;:[]{}\|'
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

passwd = input('请输入需要检查的密码组合：')
length = len(passwd)

while length == 0 or passwd.isspace():
    passwd = input('你输入的密码为空，请重新输入需要检查的密码组合：')

if length <= 8:
    flag_len = 1
elif 8 < length < 16:
    flag_len = 2
else:
    flag_len = 3

flag_con = 0
for each in passwd:
    if each in symbols:
        flag_con += 1
        break

for each in passwd:
    if each in chars:
        flag_con += 1
        break

for each in passwd:
    if each in nums:
        flag_con += 1
        break

while -1:
    print('你的密码组合复杂度为：', end = ' ')
    if flag_len == 1 or flag_con == 1:
        print('低级')
    elif flag_len == 2 or flag_con == 2:
        print('中级')
    else:
        if passwd[0] in chars:
            print('高级')
        else:
            print('中级')
            print('建议使用以下方式对你的密码安全级别进行提升: \n\
        \t1. 密码必须由数字、字母及特殊字符三种组合\n\
        \t2. 密码只能由字母开头\n\
        \t3. 密码长度不能低于16位')
        break

    print('建议使用以下方式对你的密码安全级别进行提升: \n\
        \t1. 密码必须由数字、字母及特殊字符三种组合\n\
        \t2. 密码只能由字母开头\n\
        \t3. 密码长度不能低于16位')
    break
            
    
