import time as t
class Record:
    def __init__(self,initval=None,name=None):
        self.val=initval
        self.name=name

    def __get__(self,instance,owner):
        time=t.asctime(t.localtime())
        with open(r'C:\安装应用\Python 3.3.2\练习\record.txt','a') as f:
            f.write('%s变量于柏林时间%s被读取，%s=%s\n'%(self.name,time,self.name,str(self.val)))
        return self.val          
    def __set__(self,instance,value):
        time=t.asctime(t.localtime())
        
        with open(r'C:\安装应用\Python 3.3.2\练习\record.txt','a') as f:
            f.write('%s变量于柏林时间%s被修改，%s=%s\n'%(self.name,time,self.name,str(self.val)))
            self.val=value
    def __delete__(self,instance):
        time=t.asctime(t.localtime())
       
        with open(r'C:\安装应用\Python 3.3.2\练习\record.txt','a') as f:
            f.write('%s变量于柏林时间%s被删除\n'%(self.name,time))
        del self.name





class Test:
    x=Record(10,'x')
    y=Record(8.8,'y')
    
