import tkinter as Tkinter
root = Tkinter.Tk()
c = Tkinter.Canvas(root, width = 200, height = 200)
a=c.create_oval(20, 20, 150, 150)
b=c.create_oval(30, 20, 150, 150)
d=c.create_rectangle(c.bbox(a))
c.pack()
print(c.bbox(a))

root.mainloop()
