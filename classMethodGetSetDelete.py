class MyDes:
    @classmethod
    def __init__(self,value,name):
        self.value=value
        self.name=name

    def __get__(self,instance,owner):
        print('正在获取变量：',self.name)
        return self.value

    def __set__(self,instance,vlaue):
        print('正在修改变量：',self.name)
        self.value=vlaue
        

    def __delete__(self,instance):
        print('正在删除变量:',self.name)
        if MyDes.instance:
            print('噢~这个变量没法删除~')
        else:
            del self.instance

class Test:
    x=MyDes(10,'x')
    
