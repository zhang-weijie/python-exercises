from tkinter import *

def callback(event):
    print(event.x,event.y)
    print(event.x_root,event.y_root)
    print(event.num)
    print(event.type)
    print(event.width,event.width)


root=Tk()

frame=Frame(root,width=200,height=200)
frame.bind("<Expose>",callback)
frame.focus_set()
frame.pack()

mainloop()
