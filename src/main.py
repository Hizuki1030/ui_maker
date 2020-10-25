import tkinter
import database_manage

class Uimaker(tkinter.Frame):


    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('UI maker')
        self.grid()
        self.setup()
        self.create_widgets()
        #self.preview("line","black")

    def setup(self):

        self.preview_flag=False
        self.id=None
        self.initial_x=None
        self.initail_y=None
        self.final_x=None
        self.final_y=None
        self.preview_mode=None

        self.layer={}#描画する度にレイヤー辞書にidとレイヤーをいれてい置く

        self.label_mouse_coordinate=tkinter.StringVar()




    def create_widgets(self):
        self.make_canvas()

        self.mouse_coordinate_label=tkinter.Label(self,textvariable=self.label_mouse_coordinate)
        self.mouse_coordinate_label.grid(row=0, column=0,columnspan=1,rowspan=1)
        object_tags=[]
        list_object_id_string=tkinter.StringVar(value=self)
        #object_tags=[x[0] for x in self.object_coordinate_datas]
        self.object_list = tkinter.Listbox(self, listvariable=object_tags,width=28, height=15)
        self.object_list.grid(row=1,column=3,columnspan=1,rowspan=3)

        self.draw_line_button = tkinter.Button(self, text='drawline',command = self.drawLine)#直線描画ツール
        self.draw_line_button.grid(row=1, column=0,columnspan=1,rowspan=1)

        self.draw_rectangle_button = tkinter.Button(self, text='draw rect',command = self.drawRectangle )#長方形描画ツール（塗りつぶしなし）
        self.draw_rectangle_button.grid(row=3, column=0,columnspan=1,rowspan=1)

        self.draw_oval_button = tkinter.Button(self, text='draw oval',command = self.drawOval )#長方形描画ツール（塗りつぶしなし）
        self.draw_oval_button.grid(row=2, column=0,columnspan=1,rowspan=1)

        self.clear_button = tkinter.Button(self, text='clear all',command= self.Canvas_reset)#キャンバスリセット
        self.clear_button.grid(row=0, column=1,columnspan=1,rowspan=1)

        self.delete_object_button = tkinter.Button(self, text='delete_object', command = self.Delete_componets)#消去ボタン
        self.delete_object_button.grid(row=0, column=2,columnspan=1,rowspan=1)






        self.canvas.bind('<B1-Motion>', self.preview)
        self.canvas.bind('<ButtonRelease>', self.draw)
        self.canvas.bind('<Motion>',self.set_mouse_coordinate)
        #self.object_list.bind('<Double-1>',  self.object_property)



#描画ツール
#   def drawLine(self):
#        return 0
    def drawLine(self):
        self.preview_mode="Line"
        return 0

    def drawRectangle(self):
        self.preview_mode="Rectangle"
    def fillRectangle(self):
        return 0
    def drawOval(self):
        self.preview_mode="Oval"
    def fillOval(self):
        return 0
    def drawTriangle(self):
        return 0
    def fillTriangle(self):
        return 0
    def drawText(self):
        return 0
    def drawPicture(self):
        return 0

#～～～～～～～～～～～～～～～～～～～～～～～
    def make_canvas(self):
        self.canvas = tkinter.Canvas(self, bg='white', width=320, height=240)
        self.canvas.grid(row=1, column=1, columnspan=2,rowspan=3)

    def preview(self,event):
        if(self.preview_mode=="Line"):
            if(self.preview_flag==False):
                self.preview_flag=True
                self.initial_x = event.x
                self.initial_y = event.y
                self.id=self.canvas.create_line(self.initial_x,self.initial_y,self.initial_x+1,self.initial_y+1,width=1,dash=1,fill='#FF4500')#初期のid作成のために
            else:
                self.final_x=event.x
                self.final_y=event.y
                self.canvas.delete(self.id)
                self.id=self.canvas.create_line(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1,dash=1,fill='#FF4500')
        elif(self.preview_mode=="Rectangle"):
            if(self.preview_flag==False):
                self.preview_flag=True
                self.initial_x = event.x
                self.initial_y = event.y
                self.id=self.canvas.create_rectangle(self.initial_x,self.initial_y,self.initial_x+1,self.initial_y+1,width=1,dash=1,fill='#FF4500')#初期のid作成のために
            else:
                self.final_x=event.x
                self.final_y=event.y
                self.canvas.delete(self.id)
                self.id=self.canvas.create_rectangle(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1,dash=1,outline='#FF4500')

        elif(self.preview_mode=="Oval"):
            if(self.preview_flag==False):
                self.preview_flag=True
                self.initial_x = event.x
                self.initial_y = event.y
                self.id=self.canvas.create_oval(self.initial_x,self.initial_y,self.initial_x+1,self.initial_y+1,width=1,dash=1,fill='#FF4500')#初期のid作成のために
            else:
                self.final_x=event.x
                self.final_y=event.y
                self.canvas.delete(self.id)
                self.id=self.canvas.create_oval(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1,dash=1,outline='#FF4500')

        #~~~~~~~~~クリックを離すとdrawが呼ばれるようになっている~~~~~~~~~~

    def draw(self,event):
        if(self.preview_flag==True):
            self.canvas.delete(self.id)
            if(self.preview_mode == "Line"):
                self.id=self.canvas.create_line(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1)
            elif(self.preview_mode == "Rectangle"):
                self.id=self.canvas.create_rectangle(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1)
            elif(self.preview_mode == "Oval"):
                self.id=self.canvas.create_oval(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1)
            self.layer[self.id]="1"
            self.preview_flag=False




    def Canvas_reset(self):
        return 0

    def Delete_componets(self):
        self.export_xmlfile()

    def set_mouse_coordinate(self,event):
        mouse_X=event.x
        mouse_Y=event.y
        coordinate = str(event.x)+","+str(event.y)
        self.label_mouse_coordinate.set(coordinate)

    def get_mouse_coordinate(self,event):
        coordinate=[]
        coordinate.append(event.x)
        coordinate.append(event.y)
        return coordinate


    def export_xmlfile(self):
        target_Database=database_manage.Database_manage(r"C:\Users\81909\Documents\python\ui_maker\src\components_test.xml")
        Canvas_data= self.export_canvas_components()
        target_Database.export_Database_as_xml(Canvas_data)


    def export_canvas_components(self):
        Canvas_data={}
        for id in self.canvas.find_all():
            component={}
            image=""
            text=""
            fillColor=""
            outlineColor=""
            type = self.canvas.type(id)


            tag = self.canvas.itemcget(id,"tags")
            coordinate=self.canvas.coords(id)

            component["tag"]= tag
            component["coordinate"] = coordinate
            component["layer"]=self.layer[id]

            if(type=="line"):
                fillColor = self.canvas.itemcget(id,"fill")
                component["lineColor"]=fillColor

            #line or rectangle or triangleが塗りつぶしなのかどうか~~~~~
            #塗りつぶしなら、typeの前にfillを付ける
            elif(type=="rectangle" or type == "triangle" or type == "oval"):
                type = type[0].upper()+type[1:]#一番最初の文字を大文字に
                fillColor = self.canvas.itemcget(id,"fill")
                if(fillColor != ""):
                    component["fillColor"]= fillColor
                    type="fill"+type
                outlineColor = self.canvas.itemcget(id,"outline")
                if(outlineColor != ""):
                    component["outlineColor"]=outlineColor
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            elif(type=="text"):
                text = self.canvas.itemcget(id,"text")
                fillColor = self.canvas.itemcget(id,"fg")
                component["text"]=text
                component["fillColor"]=fillColor
            elif(type=="image"):
                image = self.canvas.itemcget(id,"image")

            component["type"]= type



            Canvas_data[id]=component

        return Canvas_data


root = tkinter.Tk()
app = Uimaker(master=root)
app.mainloop()
