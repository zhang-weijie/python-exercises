from tkinter import *

def callback():
    var1.set("等着被查水表吧！")
    var2.set("我知道了！")

root=Tk()

frame1=Frame(root)
frame2=Frame(root)

var1=StringVar()
var1.set("您所访问的页面含有危险信息，请停止访问！")

photo1=PhotoImage(file=r"C:\Users\张为杰\Desktop\foto2.gif")
imgLabel=Label(frame1,image=photo1,textvariable=var1,compound=TOP).pack()

photo2=PhotoImage(file=r"C:\Users\张为杰\Desktop\foto1.gif")

var2=StringVar()
var2.set("仍要访问！")
theButton=Button(frame2,textvariable=var2,command=callback).pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

root.mainloop()
