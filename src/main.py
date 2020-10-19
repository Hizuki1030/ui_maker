import tkinter

class Uimaker(tkinter.Frame):
    layer={}　#描画する度にレイヤー辞書にidとレイヤーをいれてい置く

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
        self.draw_line_button = tkinter.Button(self, text='drawline',command = self.drawLine)#直線描画ツール
        self.draw_line_button.grid(row=1, column=0)

        self.draw_rectangle_button = tkinter.Button(self, text='draw rect',command = self.drawRectangle )#長方形描画ツール（塗りつぶしなし）
        self.draw_rectangle_button.grid(row=2, column=0)

        self.clear_button = tkinter.Button(self, text='clear all',command= self.Canvas_reset)#キャンバスリセット
        self.clear_button.grid(row=0, column=1)

        self.delete_object_button = tkinter.Button(self, text='delete_object', command = self.Delete_componets)#消去ボタン
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
        object_tags=[]
        list_object_id_string=tkinter.StringVar(value=self)
        #object_tags=[x[0] for x in self.object_coordinate_datas]
        self.object_list = tkinter.Listbox(self, listvariable=object_tags,width=28, height=15)
        self.object_list.grid(row=1,column=3,columnspan=2,rowspan=2)

        self.canvas = tkinter.Canvas(self, bg='white', width=320, height=240)
        self.canvas.grid(row=1, column=1, columnspan=2,rowspan=4)
        """self.test_canvas.bind('<B1-Motion>', self.draft)
        self.test_canvas.bind('<B1-Motion>',self.mouse_coordinate_viewer,"+")
        self.test_canvas.bind('<ButtonRelease-1>', self.draw)
        self.test_canvas.bind('<Motion>',self.mouse_coordinate_viewer)
        self.object_list.bind('<Double-1>',  self.object_property)"""

    def drawLine(self):
        print("")

    def drawRectangle(self):
        return 0



    def Canvas_reset(self):
        return 0

    def Delete_componets(self):
        return 0

    def export_canvas_components(self):
        Canvas_data={}
        component={}
        for id in canvas.find_all():
            image=""
            text=""
            fillColor=""
            outlineColor=""
            type = canvas.type(id)


            tag = canvas.itemcget(id,"tags")
            coordinate=canvas.coords(id)

            component["tag"]= tag
            component["coordinate"] = coordinate
            component["layer"]=layer[id]

            if(type=="line"):
                fillColor = canvas.itemcget(id,"fill")
                component["lineColor"]=fillColor

            #line or rectangle or triangleが塗りつぶしなのかどうか~~~~~
            #塗りつぶしなら、typeの前にfillを付ける
            elif(type=="rectangle" or type == "triangle" or type == "oval"):
                type = type[0].upper()+type[1:]#一番最初の文字を大文字に
                fillColor = canvas.itemcget(id,"fill")
                if(fillColor != ""):
                    component["fillColor"]= fillColor
                    type="fill"+type
                outlineColor = canvas.itemcget(id,"outline")
                if(outlineColor != ""):
                    component["outlineColor"]=outlineColor
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            elif(type=="text"):
                text = canvas.itemcget(id,"text")
                fillColor = canvas.itemcget(id,"fg")
                component["text"]=text
                component["fillColor"]=fillColor
            elif(type=="image"):
                image = canvas.itemcget(id,"image")

            component["type"]= type

            print(type,fillColor,coordinate,layer[id])

            Canvas_data[id]=component
        return Canvas_data


root = tkinter.Tk()
app = Uimaker(master=root)
app.mainloop()
