print('---欢迎进入通讯录程序---\n---1:查询联系人资料---\n---2:添加新的联系人---\n---3:删除已有联系人---\n---4:退出通讯录程序---')
dailbook={}

while True:
    temp=int(input('请输入相关的指令代码：'))
    if temp==1:
        name=input('请输入联系人姓名：')
        if name in dailbook:
            number=dailbook[name]
            print(name,':',number)
        else:
            print('该联系人不存在!')

    if temp==2:
        name=input('请输入联系人姓名：')
        if name in dailbook:
            print('联系人已存在：',dailbook[name])
            answer=input('是否修改联系电话(YES/NO):')
            if answer=='YES':
                newnumber=input('请输入联系电话：')
                dailbook[name]=newnumber
        else:
            number=input('请输入联系电话：')
            dailbook[name]=number

    if temp==3:
        name=input('请输入联系人姓名：')
        dailbook.pop(name)

    if temp==4:
        print('---感谢您的使用---')
        break


