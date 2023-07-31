from tkinter import *

def callback():
    global var
    if var==1:
        Label(root,bg="red").place(relx=0.5,rely=0.5,relheight=0.75,relwidth=0.75,anchor=CENTER)
        var+=1
    elif var==2:
        Label(root,bg="green").place(relx=0.5,rely=0.5,relheight=0.5,relwidth=0.5,anchor=CENTER)
        var+=1
    elif var==3:
        Label(root,bg="blue").place(relx=0.5,rely=0.5,relheight=0.25,relwidth=0.25,anchor=CENTER)
        var+=1
    else:
        pass
        


root=Tk()
var=1

w1=Button(root,text="点我",command=callback)
w1.place(relx=0.1,rely=0.1,anchor=CENTER)


mainloop()
