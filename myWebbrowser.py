from tkinter import *
import hashlib
import webbrowser

def check():
    content=text.get(1.0,END)
    if sig!=getSig(content):
        print("警告，内容发生改变！")
    else:
        print("风平浪静")

def insert():
    text.insert("here","Revolutionario\n")

def getSig(content):
    m=hashlib.md5(content.encode())
    return m.digest()

def getIndex(text,key):
    return tuple(map(int,str.split(text.index(key),".")))

def index_(text,key):
    start=1.0
    while 1:
        pos=text.search(key,start,stopindex=END)
        if not pos:
            break
        print("找到了，位置是：",getIndex(text,pos))
        start=pos+"+1c"

def callback(event):
    text.edit_separator()

root=Tk()

sb=Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)

text=Text(root,height=40,width=40,yscrollcommand=sb.set,undo=True,autoseparator=False)
text.pack()

sb.config(command=text.yview)




text.insert(INSERT,"Commarade\n")
print(text.index(INSERT))
text.mark_set("here",2.0)
text.insert("here","Che Guevara!\n")
print(text.index(INSERT))

text.tag_config("tag_1",background="yellow",foreground="red",underline=True)
text.tag_add("tag_1",1.0,1.9)
text.tag_bind("tag_1","<Enter>",lambda x=1:text.config(cursor="arrow"))
text.tag_bind("tag_1","<Leave>",lambda x=1:text.config(cursor="xterm"))
text.tag_bind("tag_1","<Button-1>",lambda x=1:webbrowser.open("https://www.marxists.org/archive/guevara/index.htm"))


text.bind("<Key>",callback)

photo=PhotoImage(file=r"C:\Users\张为杰\Desktop\foto5.gif")
b1=Button(text,text="点我点我！",command=lambda x=text:x.image_create(END,image=photo))
b1.pack()
text.window_create(END,window=b1)

content=text.get(1.0,END)
sig=getSig(content)

b2=Button(root,text="检查",command=check)
b2.pack(side=BOTTOM,anchor=E)
b3=Button(root,text="插入",command=insert)
b3.pack(side=BOTTOM,anchor=E)
b4=Button(root,text="索引",command=index_(text,key=input("请输入要检索的字符：")))
b4.pack(side=BOTTOM,anchor=E)
b5=Button(root,text="撤销",command=lambda x=text:x.edit_undo())
b5.pack(side=BOTTOM,anchor=E)
b6=Button(root,text="恢复",command=lambda x=text:x.edit_redo())
b6.pack(side=BOTTOM,anchor=E)

root.mainloop()
