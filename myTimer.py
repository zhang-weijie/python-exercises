import time as t
class Mytimer():
    def __init__(self):
        self.unit=['年','月','天','小时','分钟','秒']
        self.begin=0
        self.end=0
        print('等待计时')

    def __str__(self):
        return self._calc()
    __repr__=__str__

          
    def start(self):
        if not self.begin:
            self.begin=t.localtime()
            print('开始计时...')
        else:
            print('请先用stop方法结束计时')

    def stop(self):
        if self.begin:
            self.end=t.localtime()
            print('停止计时！')
        else:
            print('请先用start方法开始计时')
    def _calc(self):
        self.lasted=[]
        result='用时'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                result+=str(self.lasted[index])+self.unit[index]
        return result
    
    def __add__(self,other):
        list1=[]
        result='两次共用时'
        for index in range(6):
            list1.append(self.lasted[index]+other.lasted[index])
            if list1[index]:
                result+=str(list1[index])+self.unit[index]
        return result
            
            
        
            
            
            
