from tkinter import *
import easygui

def callback():
    print("我被调用了...")

def fileopen():
    result=easygui.fileopenbox(msg="请选择打开文件",title="打开文件",default="C:\\安装应用\\Python学习\\练习\\*.py",filetypes="*.py")
    print(result)

def filesave():
    result=easygui.filesavebox(msg="请选择保存文件的路径",title="保存文件",default="C:\\安装应用\\Python学习\\练习\\*.py",filetypes="*.py")
    print(result)

def popup(event):
    editmenu.post(event.x_root,event.y_root)

def print_choice():
    print(variable.get())

root=Tk()

photo_che=PhotoImage(file=r"C:\Users\张为杰\Desktop\foto1.gif")
photo_big=PhotoImage(file=r"C:\Users\张为杰\Desktop\foto2.gif")
photo_v=PhotoImage(file=r"C:\Users\张为杰\Desktop\foto3.gif")

menubar=Menu(root,postcommand=lambda x=1:print("我被自动调用了"))

filemenu=Menu(menubar,tearoff=False)
filemenu.add_command(label="Che Guevara",command=fileopen,image=photo_che,compound="center")
filemenu.add_command(label="Big Brother",command=filesave,image=photo_big,compound="center")
filemenu.add_separator()
filemenu.add_command(label="V Scourage",command=root.quit,image=photo_v,compound="center")
menubar.add_cascade(label="文件",menu=filemenu)

root.config(menu=menubar)

editmenu=Menu(root,tearoff=False)
editmenu.add_command(label="复制",command=callback)
editmenu.add_command(label="粘贴",command=callback)
editmenu.add_command(label="选择",command=callback)

frame1=Frame(root,width=100,height=100,bg="green")
frame1.pack(padx=10,pady=10)
frame1.bind("<Button-3>",popup)

frame2=Frame(root,width=100,height=2,bg="black")
frame2.pack(padx=10,pady=10)

mb=Menubutton(root,text="点我",relief="raised")
mb.pack()
editmenu=Menu(mb,tearoff=False)
editmenu.add_command(label="复制",command=callback)
editmenu.add_command(label="粘贴",command=callback)
editmenu.add_command(label="选择",command=callback)
mb.config(menu=editmenu)

frame3=Frame(root,width=100,height=2,bg="black")
frame3.pack(padx=10,pady=10)

OPTIONS=["ANHUI","Hefei","JIANGSU","Nanjing","ZHEJIANG","Hangzhou","HUBEI","Wuhan"]

variable=StringVar()
variable.set(OPTIONS[0])
om=OptionMenu(root,variable,*OPTIONS)
om.pack()
Button(root,text="打印选择结果",command=print_choice).pack()


mainloop()
