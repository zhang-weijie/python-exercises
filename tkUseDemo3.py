from tkinter import *

root=Tk()

sb2=Scrollbar(root,orient=HORIZONTAL)
sb2.pack(side=BOTTOM,fill=X)

sb1=Scrollbar(root)
sb1.pack(side=RIGHT,fill=Y)



lb=Listbox(root,xscrollcommand=sb2.set,yscrollcommand=sb1.set)
lb.pack(side=LEFT,fill=BOTH)

for i in range(80):
    lb.insert(0,2**i)


sb1.config(command=lb.yview)
sb2.config(command=lb.xview)

mainloop()
