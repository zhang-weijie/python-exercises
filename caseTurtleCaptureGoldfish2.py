import random as r
import myModules.easygui.easygui as g

def plus(a,b,c,d,minimum,maximum):
    list1=[]
    for m in range(a,b):
        for n in range(c,d):
            if minimum<=abs(m)+abs(n)<=maximum:
                list1.append((m,n))
    return list1

class Turtel:
    def __init__(self):
        self.power=100
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
        init_place=(self.x,self.y)
        g.msgbox('乌龟的初始位置为%s'%str(init_place))

    def move(self):
        list0=plus(-2,3,-2,3,1,2)
        list1=[]
        for i in range(len(list0)):
            list1.append(list0[i][0])
        x_choice=g.choicebox(msg='横向移动',choices=list1)
        list2=[]
        for each in list0:
            if each[0]==int(x_choice):
                list2.append(each[1])
        y_choice=g.choicebox(msg='纵向移动',choices=list2)     
        new_x=self.x+int(x_choice)
        new_y=self.y+int(y_choice)
        self.power-=abs(int(x_choice))+abs(int(y_choice))
        g.msgbox('乌龟的体力值为%d'%self.power)
        if new_x<0:
            self.x=0+(0-new_x)
        elif new_x>10:
            self.x=10-(new_x-10)
        else:
            self.x=new_x
        if new_y<0:
            self.y=0+(0-new_y)
        elif new_y>10:
            self.y=10-(new_y-10)
        else:
            self.y=new_y
        return (self.x,self.y)
    

    def eat(self):
        self.power+=20
        if self.power>100:
            self.power=100
        g.msgbox('乌龟的体力值为%d'%self.power)
        
class Fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
    
    def move(self):
        list1=plus(-1,2,-1,2,0,1)
        random_base=r.randint(0,len(list1)-1)
        result=(list1[random_base][0],list1[random_base][1])
        new_x=self.x+result[0]
        new_y=self.y+result[1]
        if new_x<0:
            self.x=0+(0-new_x)
        elif new_x>10:
            self.x=10-(new_x-10)
        else:
            self.x=new_x
        if new_y<0:
            self.y=0+(0-new_y)
        elif new_y>10:
            self.y=10-(new_y-10)
        else:
            self.y=new_y
        return (self.x,self.y)

turtel=Turtel()
fish=[]
for i in range(5):
    fish.append(Fish())


while True:
    if not len(fish):
        print('鱼吃完了，游戏结束')
        break
    if not turtel.power:
        print('乌龟累死了，游戏结束')
        break

    fish_pos=[]
    fish_place=''

    for each_fish in fish[:]:
        pos1=each_fish.move()
        fish_pos.append(pos1)
        fish_place+='一条鱼的位置在%s\n'%str(pos1)
    g.msgbox(fish_place)

    pos2=turtel.move()
    g.msgbox('乌龟的位置为%s'%str(pos2))

    if pos2 in fish_pos:
        turtel.eat()
        print('一条鱼被吃掉了')
        index=fish_pos.index(pos2)
        fish.remove(fish[index])

    


        
    
        
        
        

        

    
            
        
        
            
            
