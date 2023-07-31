from tkinter import *

root=Tk()

w=Canvas(root,width=200,height=200,background="white")
w.pack()

oval1=w.create_oval(60,35,140,115,fill="blue")
oval2=w.create_oval(70,55,130,115,fill="white")
rect3=w.create_rectangle(73,108,128,150,fill="blue")
oval10=w.create_oval(80,100,120,140,fill="white")
oval11=w.create_oval(90,110,110,130,fill="white")
oval3=w.create_oval(85,50,100,70,fill="white")
oval4=w.create_oval(100,50,115,70,fill="white")
oval5=w.create_oval(89,56,95,64,fill="black")
oval6=w.create_oval(111,56,105,64,fill="black")
oval7=w.create_oval(91,58,93,62,fill="white")
oval8=w.create_oval(107,58,109,62,fill="white")
oval9=w.create_oval(95,65,105,75,fill="red")
arc1=w.create_arc(120,85,80,95,extent=359,style="arc")
rect1=w.create_rectangle(80,85,120,90,outline="",fill="white")
line1=w.create_line(100,75,100,95)
lin2=w.create_line(74,105,126,105,width=6,capstyle="round",fill="red")
rect2=w.create_rectangle(90,110,110,120,outline="",fill="white")
line3=w.create_line(90,120,110,120)
poly1=w.create_polygon(56,120,74,108,74,125,56,130,outline="black",fill="blue")
poly2=w.create_polygon(128,108,145,120,145,130,128,125,outline="black",fill="blue")
oval12=w.create_oval(46,121,60,135,outline="black",fill="white")
oval13=w.create_oval(141,121,155,135,outline="black",fill="white")
oval14=w.create_oval(65,145,95,160,outline="black",fill="white")
oval15=w.create_oval(105,145,135,160,outline="black",fill="white")
oval16=w.create_oval(95,105,105,115,fill="yellow")
line4=w.create_line(97,107,103,107,width=2,capstyle="round",fill="black")
oval17=w.create_oval(98,110,102,114,fill="red")

w.postscript(file=r"C:\Users\张为杰\Desktop\foto5.ps",colormode="color")


mainloop()

