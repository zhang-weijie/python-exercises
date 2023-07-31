from tkinter import *



def create_pane(n,m1):
    if n==1:
        left=Label(m1,text="left pane")
        m1.add(left)
        m2=PanedWindow(m1,orient="vertical",sashrelief="raised",showhandle=True)
        m1.add(m2)
        top=Label(m2,text="top pane")
        m2.add(top)
        m3=PanedWindow(m2,sashrelief="raised",showhandle=True)
        m2.add(m3)
    else:
        
        



        
m1=PanedWindow(sashrelief="raised",showhandle=True)
m1.pack(fill="both",expand=True)
n=int(input("请输入要创建的层数："))
create_pane(n,m1)
mainloop() 
