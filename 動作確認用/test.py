from tkinter import *

from tkinter import messagebox
import tkinter.simpledialog as simpledialog

root = Tk()
c0 = Canvas(root, width = 200, height = 150)
c0.pack()
id = c0.create_rectangle(10, 10, 20, 20, fill = 'brown')

# 移動
def move_rect(event):

    inputdata = simpledialog.askstring("Input Box", "値を入力してください",)
    print("simpledialog",inputdata)


# バインディング
c0.tag_bind(id, '<Button1-Motion>', move_rect)

root.mainloop()
