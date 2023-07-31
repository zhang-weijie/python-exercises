import random as r
import myModules.easygui.easygui as g

def plus(a,b,c,d,minimum,maximum):
    list1=[]  
    for m in range(a,b):
        for n in range(c,d):
            if minimum<=abs(m)+abs(n)<=maximum:
                list1.append((m,n))
    random_base=r.randint(0,len(list1)-1)   
    return (list1[random_base][0],list1[random_base][1])

class Turtel:
    def __init__(self):
        self.power=100
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
        init_place=(self.x,self.y)
        g.msgbox('乌龟的初始位置为%s'%str(init_place))

    def move(self):
        result=plus(-2,3,-2,3,1,2)
        new_x=self.x+result[0]
        new_y=self.y+result[1]
        self.power-=abs(result[0])+abs(result[1])
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
        movepath=r.choice([-1,0,1])
        new_x=self.x+movepath
        new_y=self.y+(1-abs(movepath))
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
    pos=turtel.move()
    g.msgbox('乌龟的位置为%s'%str(pos))

    fish_place=''

    for each_fish in fish[:]:
        pos2=each_fish.move()
        fish_place+='一条鱼的位置在%s\n'%str(pos2)
        if pos2==pos:
            turtel.eat()
            print('一条鱼被吃掉了')
            fish.remove(each_fish)
    g.msgbox(fish_place)
    


        
    
        
        
        

        

    
            
        
        
            
            
