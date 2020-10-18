import tkinter
import tkinter.ttk as Ttkinter

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('UI maker')
        self.pack()
        self.setup()
        self.create_widgets()

    def create_widgets(self):
        tool_num=2
        self.mouse_coordinate_label_text=tkinter.StringVar()
        self.mouse_coordinate_label_text.set("x,y")
        self.mouse_coordinate_label=tkinter.Label(self,textvariable=self.mouse_coordinate_label_text)
        self.mouse_coordinate_label.grid(row=0,column=0)

        self.UIcanvas=tkinter.Canvas(self,width=self.UIwidth,height=self.UIheight,bg=self.UIbackground_color)
        self.UIcanvas.grid(rowspan=tool_num,row=1,column=1)

        self.draw_line_button=tkinter.Button(self,text="line")
        self.draw_line_button.grid(row=1,column=0)

        self.draw_rectangle_button=tkinter.Button(self,text="rect")
        self.draw_rectangle_button.grid(row=2,column=0)


        self.ID_information_tree=Ttkinter.Treeview(self)
        self.ID_information_tree.grid(rowspan=tool_num,row=1,column=2)
        self.ID_information_tree["column"]=(1,2,3)
        self.ID_information_tree["show"]="headings"
        self.ID_information_tree.column(1,width=75)
        self.ID_information_tree.column(2,width=75)
        self.ID_information_tree.column(3,width=75)

        self.ID_information_tree.heading(1,text="ID")
        self.ID_information_tree.heading(2,text="type")
        self.ID_information_tree.heading(3,text="tag")



    def setup(self):
        self.UIwidth=320
        self.UIheight=240
        self.UIbackground_color="white"



root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
