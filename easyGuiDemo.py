import easygui as g

title='账号中心'
msg='请填写以下联系方式'
fieldnames=[' *用户名',' *真实姓名','  固定电话',' *手机号码','  QQ',' *E-mail']
fieldvalues=g.multenterbox(msg,title,fieldnames)

while 1:
    if fieldvalues==None:
        break
    errmsg=''
    for i in range(len(fieldnames)):
        option=fieldnames[i].strip()
        if fieldvalues[i].strip()=='' and option[0]=='*':
            errmsg+='【%s】为必填项\n'%fieldnames[i]
    if errmsg=='':
        break
    fieldvalues=g.multenterbox(errmsg,title,fieldnames,fieldvalues)
print('用户资料为：%s'%str(fieldvalues))
    
            
