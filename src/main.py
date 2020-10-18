import tkinter

class Uimaker(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('UI maker')
        self.pack()
        self.setup()
        self.create_widgets()

    def setup(self):
        pass

    def create_widgets(self):
        self.draw_line_button = tkinter.Button(self, text='drawline', command=self.line_mode)#直線描画ツール
        self.draw_line_button.grid(row=1, column=0)

        self.draw_rectangle_button = tkinter.Button(self, text='draw rect', command=self.rectangle_mode)#長方形描画ツール（塗りつぶしなし）
        self.draw_rectangle_button.grid(row=2, column=0)

        self.clear_button = tkinter.Button(self, text='clear all', command=self.clear_canvas)#キャンバスリセット
        self.clear_button.grid(row=0, column=1)

        self.delete_object_button = tkinter.Button(self, text='delete_object', command=self.delete_object)#消去ボタン
        self.delete_object_button.grid(row=0, column=2)

        self.line_width_label= tkinter.Label(self,text="太さ")
        self.line_width_label.grid(row=0,column=3)

        self.line_width_entry = tkinter.Entry(self,width=20)
        self.line_width_entry.grid(row=0,column=4)
        self.line_width_entry.insert(tkinter.END,"1")

        self.mouse_coordinate_label_text=tkinter.StringVar()
        self.mouse_coordinate_label_text.set("x,y")
        self.mouse_coordinate_label=tkinter.Label(self,textvariable=self.mouse_coordinate_label_text)
        self.mouse_coordinate_label.grid(row=0, column=0)

        list_object_id_string=tkinter.StringVar(value=self)
        object_tags=[x[0] for x in self.object_coordinate_datas]
        self.object_list = tkinter.Listbox(self, listvariable=object_tags,width=28, height=15)
        self.object_list.grid(row=1,column=3,columnspan=2,rowspan=2)

        self.test_canvas = tkinter.Canvas(self, bg='white', width=320, height=240)
        print(self.test_canvas)
        """self.test_canvas.grid(row=1, column=1, columnspan=2,rowspan=4)
        self.test_canvas.bind('<B1-Motion>', self.draft)
        self.test_canvas.bind('<B1-Motion>',self.mouse_coordinate_viewer,"+")
        self.test_canvas.bind('<ButtonRelease-1>', self.draw)
        self.test_canvas.bind('<Motion>',self.mouse_coordinate_viewer)
        self.object_list.bind('<Double-1>',  self.object_property)"""

def line_mode(self):
    print("")

root = tkinter.Tk()
app = Uimaker(master=root)
app.mainloop()