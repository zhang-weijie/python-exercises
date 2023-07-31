from tkinter import *
from tkinter import messagebox,filedialog,colorchooser

def aoc():
    messagebox.askokcancel(title="请选择...",message="发射核弹！",parent=top)

def aq():
    messagebox.askquestion(title="请选择...",message="发射核弹！")

def arc():
    messagebox.askretrycancel(title="请选择...",message="发射失败，重试？")

def ayn():
    messagebox.askyesno(title="请选择...",message="发射核弹！")

def se():
    messagebox.showerror(title="警告",message="出错了！")

def si():
    messagebox.showinfo(title="提示",message="人类的命运在你手中")

def sw():
    messagebox.showwarning(title="警告",message="人类的命运已无可挽回！")

def aofn():
    f=filedialog.askopenfilename(title="请选择文件",defaultextension=".py",filetypes=[("PNG",",png"),("JPG",".jpg"),("TXT",".txt")])
    print(f)

def asafn():
    f=filedialog.asksaveasfilename(title="请选择文件",defaultextension=".py",filetypes=[("PNG",",png"),("JPG",".jpg"),("TXT",".txt")])
    print(f)

def ac():
    f=colorchooser.askcolor()
    print(f)
  
root=Tk()

top=Toplevel()
top.title("新的顶级窗口")

Button(root,text="请选择",command=aoc).pack()
Button(root,text="请选择",command=aq).pack()
Button(root,text="请选择",command=arc).pack()
Button(root,text="请选择",command=ayn).pack()
Button(root,text="警告",command=se).pack()
Button(root,text="提示",command=si).pack()
Button(root,text="警告",command=sw).pack()
Button(root,text="打开文件",command=aofn).pack()
Button(root,text="保存文件",command=asafn).pack()
Button(root,text="选择颜色",command=ac).pack()
mainloop()
