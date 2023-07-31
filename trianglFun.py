from tkinter import *
import math as m

root=Tk()

c=Canvas(root,width=200,height=100)
c.pack()

center_x=100
center_y=50
r=50

points=[
    center_x-int(r*m.sin(2*m.pi/5)),
    center_y-int(r*m.cos(2*m.pi/5)),
    center_x+int(r*m.sin(2*m.pi/5)),
    center_y-int(r*m.cos(2*m.pi/5)),
    center_x-int(r*m.sin(m.pi/5)),
    center_y+int(r*m.cos(m.pi/5)),
    center_x,
    center_y-r,
    center_x+int(r*m.sin(m.pi/5)),
    center_y+int(r*m.cos(m.pi/5))
    ]

c.create_polygon(points,outline="green",fill="pink")

mainloop()
