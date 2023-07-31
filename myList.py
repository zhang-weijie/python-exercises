class M:
    def __init__(self,*args):
        self.values=[x for x in args]
        self.count={}.fromkeys(range(len(self.values)),0)
        
    def __len__(self):
        return len(self.values)

    def __getitem__(self,key):
        try:
            if self.values[key]:
                self.count[key]+=1
                return self.values[key]
        except IndexError:
            print('您要访问的元素不存在！')

    def __setitem__(self,key,value):
        try:
            self.values[key]=value
            self.count[key]=0
        except IndexError:
            print('您要修改的元素不存在！')

    def __delitem__(self,key):
        try:
            if self.values[key]:
                del self.count[key]
                del self.values[key]
        except IndexError:
            print('您要删除的元素不存在！')
        

    def counter(self,index):
        if index in self.values:
            return self.count[self.values.index(index)]
        else:
            print('您索引的元素不存在！')
            
    def append(self,value):
        self.values.append(value)
        self.count[len(self.values)-1]=0

    def pop(self):
        self.values.pop()
        del self.count[len(self.count)-1]

    def remove(self,value):
        if value in self.values:
            del self.count[self.values.index(value)]
            self.values.remove(value)
        else:
            print('您要移除的元素不存在！')

    def insert(self,key,value):
        self.values.insert(key,value)
        for i in range(len(self.count)):
            if i>=key:
                self.count[i+1]=self.count[i]
        self.count[key]=0
                

        
    def clear(self):
        self.values.clear()
        self.count.clear()

    def reverse(self):
        values_list=list(self.count.values())
        values_list.reverse()
        for i in range(len(self.count)):
            self.count[i]=values_list[i]
        self.values.reverse()
        
            
    
            
        
        
        
    
