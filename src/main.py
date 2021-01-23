import tkinter
from tkinter import colorchooser
import database_manage
import numpy as np
import math
import logging
import ParameterWindow as PW
import tkinter.font as tkFont
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
        self.minimum_pixelX=10
        self.minimum_pixelY=10
        self.func_B1_Motion_mode=""
        self.func_B1_mode=""
        self.adjointBox_id=None
        self.selectObjectNum=-1
        self.selectObjectMax=0

        self.layer={}#描画する度にレイヤー辞書にidとレイヤーをいれてい置く

        self.label_mouse_coordinate=tkinter.StringVar()

        self.MainColor="#000000"
        self.previewColor="#000000"

        self.TextMoveFlag = False



        logging.disable(logging.CRITICAL)




    def create_widgets(self):
        self.make_canvas(320,240)
        #各ツールのアイコン画像を取得
        self.text_pic=tkinter.PhotoImage(file=r'./picture/text_pic.png')
        self.fillTriangle_pic=tkinter.PhotoImage(file=r'./picture/fillTriangle_pic.png')
        self.fillOval_pic=tkinter.PhotoImage(file=r'./picture/fillOval_pic.png')
        self.fillRectangle_pic=tkinter.PhotoImage(file=r'./picture/fillRectangle_pic.png')
        self.Oval_pic=tkinter.PhotoImage(file=r'./picture/Oval_pic.png')
        self.Rectangle_pic=tkinter.PhotoImage(file=r'./picture/Rectangle_pic.png')
        self.Line_pic=tkinter.PhotoImage(file=r'./picture/Line_pic.png')

        fontStyle = tkFont.Font(family="Lucida Grande", size=10)
        self.mouse_coordinate_label=tkinter.Label(self,textvariable=self.label_mouse_coordinate,font=fontStyle,width=6)#マウス座標確認用
        self.mouse_coordinate_label.grid(row=0, column=0,columnspan=1,rowspan=1)
        #現在動作なし==========================
        object_tags=[]
        list_object_id_string=tkinter.StringVar(value=self)
        #object_tags=[x[0] for x in self.object_coordinate_datas]
        #======================================
        self.object_list = tkinter.Listbox(self, listvariable=object_tags,width=28, height=15)
        self.object_list.grid(row=1,column=6,columnspan=1,rowspan=7)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.draw_line_button = tkinter.Button(self, text='line',command = self.drawLine,image= self.Line_pic)#直線描画ツールボタン
        self.draw_line_button.grid(row=1, column=0,sticky=tkinter.W)

        self.draw_rectangle_button = tkinter.Button(self, text='rect',command = self.drawRectangle ,image=self.Rectangle_pic)#長方形描画ツール（塗りつぶしなし）ボタン
        self.draw_rectangle_button.grid(row=3, column=0,sticky=tkinter.W)

        self.draw_oval_button = tkinter.Button(self, text='oval',command = self.drawOval ,image=self.Oval_pic)#楕円描画ツール（塗りつぶしなし）ボタン
        self.draw_oval_button.grid(row=2, column=0,sticky=tkinter.W)

        self.draw_fillrectangle_button = tkinter.Button(self, text='fill rect',command = self.fillRectangle ,image=self.fillRectangle_pic)#長方形描画ツール（塗りつぶし）ボタン
        self.draw_fillrectangle_button.grid(row=4, column=0,sticky=tkinter.W)

        self.draw_filloval_button = tkinter.Button(self, text='fill oval',command = self.fillOval ,image=self.fillOval_pic)#楕円描画ツール（塗りつぶし）ボタン
        self.draw_filloval_button.grid(row=5, column=0,sticky=tkinter.W)

        self.draw_filltriangle_button = tkinter.Button(self,text = "",command=self.fillTriangle,image=self.fillTriangle_pic)#三角形描画ツールボタン
        self.draw_filltriangle_button.grid(row=6,column =0,sticky=tkinter.W)

        self.draw_text_button = tkinter.Button(self,text="",image=self.text_pic,command=self.drawText)#テキストツールボタン
        self.draw_text_button.grid(row=7,column =0,sticky=tkinter.W)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


        self.clear_button = tkinter.Button(self, text='clear all',command= self.Canvas_reset)#キャンバスリセット
        self.clear_button.grid(row=0, column=1,columnspan=1,rowspan=1)


        self.color_label = tkinter.Label(self, text='Color :')
        self.color_label.grid(row=0, column=3,columnspan=1,rowspan=1,sticky=tkinter.E)

        self.Main_Color_button = tkinter.Button(self, text='main', command = self.ChangeMainColor)#描画される色の指定
        self.Main_Color_button.grid(row=0, column=4,columnspan=1,rowspan=1)

        self.previewLineColor_button = tkinter.Button(self, text='preview', command = self.ChangePreviewColor)#previewで表示される色
        self.previewLineColor_button.grid(row=0, column=5,columnspan=1,rowspan=1)

        self.export_button = tkinter.Button(self, text='save', command = self.export_xmlfile)#保存ボタン
        self.export_button.grid(row=0, column=6,columnspan=1,rowspan=1)

        self.export_button = tkinter.Button(self, text='select', command = self.selectObject_func)#オブジェクト選択モード
        self.export_button.grid(row=0, column=7,columnspan=1,rowspan=1)

        self.export_button = tkinter.Button(self, text='info', command = self.infomationObject)#選択されたオブジェクトのパラメータ設定ウィンドウを開く
        self.export_button.grid(row=1, column=7,columnspan=1,rowspan=1)

        self.export_button = tkinter.Button(self, text='move', command = self.ObjectMove_func)#選択されたオブジェクトのパラメータ設定ウィンドウを開く
        self.export_button.grid(row=2, column=7,columnspan=1,rowspan=1)
        self.export_button.focus_set()

        self.canvas.bind('<B1-Motion>', self.func_B1_Motion)
        self.canvas.bind('<ButtonRelease-1>', self.draw)
        self.canvas.bind('<Motion>',self.set_mouse_coordinate)
        self.canvas.bind("<Button-1>",self.func_B1)
        self.canvas.bind('<MouseWheel>',self.func_shift)
        self.master.bind("<s>",self.selectObject_func)
        self.master.bind("<w>",self.ObjectMove_func)
        self.master.bind("<q>",self.delete_adjoint)
        self.master.bind("<e>",self.infomationObject)
        self.master.bind("<d>",self.Delete_object)        
        
        
        #self.canvas.bind("<MouseWheel>", self.zoomer)
        #self.object_list.bind('<Double-1>',  self.object_property)


        self.parameterApp=PW.ParameterWindow(self,self.canvas,self.layer)



#描画ツール
    def drawLine(self):
        self.func_B1_Motion_mode="preview"
        self.preview_mode="Line"
        logging.warning("drawline mode")
    def drawRectangle(self):
        self.func_B1_Motion_mode="preview"
        self.preview_mode="Rectangle"
        logging.warning("drawRectangle mode")
    def fillRectangle(self):
        self.func_B1_Motion_mode="preview"
        self.preview_mode="fillRectangle"
        logging.warning("fillRectangle")
    def drawOval(self):
        self.func_B1_Motion_mode="preview"
        self.preview_mode="Oval"
    def fillOval(self):
        self.func_B1_Motion_mode="preview"
        self.preview_mode="fillOval"
    def fillTriangle(self):
        self.func_B1_Motion_mode="preview"
        self.preview_mode="fillTriangle"
    def drawText(self):
        self.func_B1_Motion_mode="preview"
        self.preview_mode="text"
        return 0
    def drawPicture(self):
        self.func_B1_Motion_mode="preview"
        return 0

#～～～～～～～～～～～～～～～～～～～～～～～
    def make_canvas(self,Width,Height):
        self.width=Width
        self.height=Height
        self.canvas = tkinter.Canvas(self, bg='white', width=Width, height=Height)
        self.canvas.grid(row=1, column=1, columnspan=5,rowspan=7)

    def ChangePreviewColor(self):
        color = colorchooser.askcolor(title="preview color")
        self.previewColor=color[1]

    def ChangeMainColor(self):
        color = colorchooser.askcolor(title="Main color")
        self.MainColor=color[1]

    def selectObject_func(self,evnet):
        print("called")
        self.func_B1_Motion_mode = ""
        self.func_B1_mode="selectObject"

    def infomationObject(self,event):
        self.func_B1_Motion_mode = ""
        self.func_B1_mode="selectObject"
        type_attach={"rectangle":"Rectangle","oval":"Oval","line":"Line","polygon":"Triangle","text":"text"}
        type=self.canvas.type(self.selectObject)
        fill=self.canvas.itemcget(self.selectObject,"fill")
        type=type_attach[type]
        if(len(fill) >0 ):
            type="fill"+type
        self.parameterApp.makeWindow(self.selectObject,type)

    def ObjectMove_func(self,event):
        print("called")
        self.func_B1_mode= ""
        self.func_B1_Motion_mode="ObjectMove"


    def func_B1(self,event):
        if(self.func_B1_mode == "selectObject"):
            self.canvas.delete(self.adjointBox_id)

            self.selectObject_x,self.selectObject_y=event.x,event.y
            x,y = self.selectObject_x,self.selectObject_y

            Objects = self.canvas.find_overlapping(x-2,y-2,x+2,y+2)
            self.selectObjectMax=len(Objects)
            if(self.selectObjectMax > 0):
                self.selectObject=Objects[-1]#一番上にあるオブジェクトを選択
                print(self.selectObject) # ['en_1 current']
                selectObjectCoordinate=self.canvas.bbox(self.selectObject)
                self.adjointBox_id=self.canvas.create_rectangle(selectObjectCoordinate[0]-2
                                                ,selectObjectCoordinate[1]-2
                                                ,selectObjectCoordinate[2]+2
                                                ,selectObjectCoordinate[3]+2
                                                ,width=1
                                                ,dash=2
                                                ,outline=self.previewColor)

    def func_shift(self,event):
        if(self.func_B1_mode == "selectObject"):
            self.canvas.delete(self.adjointBox_id)
            x,y = self.selectObject_x,self.selectObject_y
            self.selectObjectNum=self.selectObjectNum+1
            if(self.selectObjectNum==self.selectObjectMax):
                self.selectObjectNum=-1
            Objects = self.canvas.find_overlapping(x-2,y-2,x+2,y+2)
            self.selectObject=Objects[self.selectObjectNum]#一番上にあるオブジェクトを選択
            print(self.selectObject) # ['en_1 current']
            selectObjectCoordinate=self.canvas.bbox(self.selectObject)
            self.adjointBox_id=self.canvas.create_rectangle(selectObjectCoordinate[0]-2
                                                ,selectObjectCoordinate[1]-2
                                                ,selectObjectCoordinate[2]+2
                                                ,selectObjectCoordinate[3]+2
                                                ,width=1
                                                ,dash=2
                                                ,outline=self.previewColor)
        return 0

    def func_B1_Motion(self,event):
        if(self.func_B1_Motion_mode == "preview"):
            if(self.preview_flag==False):#マウスを右クリックし始めたcanvas上の座標を取得
                self.preview_flag=True
                self.initial_x = self.change_nearestCoordinateX(event.x,self.minimum_pixelX)
                self.initial_y = self.change_nearestCoordinateY(event.y,self.minimum_pixelY)
                self.id=None
            if(self.preview_mode=="Line"):
                self.final_x=self.change_nearestCoordinateX(event.x,self.minimum_pixelX)
                self.final_y=self.change_nearestCoordinateY(event.y,self.minimum_pixelY)
                self.canvas.delete(self.id)
                self.id=self.canvas.create_line(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1,dash=1,fill=self.previewColor)
            elif(self.preview_mode=="Rectangle"):
                self.final_x=self.change_nearestCoordinateX(event.x,self.minimum_pixelX)
                self.final_y=self.change_nearestCoordinateY(event.y,self.minimum_pixelY)
                self.canvas.delete(self.id)
                self.id=self.canvas.create_rectangle(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1,dash=1,outline=self.previewColor)
            elif(self.preview_mode=="Oval"):
                self.final_x=self.change_nearestCoordinateX(event.x,self.minimum_pixelX)
                self.final_y=self.change_nearestCoordinateY(event.y,self.minimum_pixelY)
                self.canvas.delete(self.id)
                self.id=self.canvas.create_oval(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1,dash=1,outline=self.previewColor)
            elif(self.preview_mode=="fillRectangle"):
                self.final_x=self.change_nearestCoordinateX(event.x,self.minimum_pixelX)
                self.final_y=self.change_nearestCoordinateY(event.y,self.minimum_pixelY)
                self.canvas.delete(self.id)
                self.id=self.canvas.create_rectangle(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1,dash=1,fill=self.previewColor,outline=self.previewColor)
            elif(self.preview_mode=="fillOval"):
                self.final_x=self.change_nearestCoordinateX(event.x,self.minimum_pixelX)
                self.final_y=self.change_nearestCoordinateY(event.y,self.minimum_pixelY)
                self.canvas.delete(self.id)
                self.id=self.canvas.create_oval(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1,dash=1,fill=self.previewColor,outline=self.previewColor)
            elif(self.preview_mode=="fillTriangle"):
                self.final_x=self.change_nearestCoordinateX(event.x,self.minimum_pixelX)
                self.final_y=self.change_nearestCoordinateY(event.y,self.minimum_pixelY)
                self.canvas.delete(self.id)
                self.id=self.canvas.create_polygon(self.initial_x,self.initial_y,self.final_x,self.initial_y,(self.initial_x+self.final_x)/2,self.final_y,width=1,outline=self.previewColor)
            elif(self.preview_mode == "text"):
                self.final_x=self.change_nearestCoordinateX(event.x,self.minimum_pixelX)
                self.final_y=self.change_nearestCoordinateY(event.y,self.minimum_pixelY)
                self.canvas.delete(self.id)
                self.id=self.canvas.create_rectangle(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1,dash=1,fill=self.previewColor,outline=self.previewColor)
        elif(self.func_B1_Motion_mode == "ObjectMove"):
            self.func_B1_mode = ""
            x,y=event.x,event.y
            x=self.change_justCoordinateX(x,self.minimum_pixelX/2)
            y=self.change_justCoordinateY(y,self.minimum_pixelY/2)
            Object_coordinate=self.canvas.coords(self.selectObject)
            adjointBox_coordinate = self.canvas.coords(self.adjointBox_id)
            type=self.canvas.type(self.selectObject)
            if(type == "rectangle" or type == "line" or type == "oval"):
                dx=Object_coordinate[2]-Object_coordinate[0]
                dy=Object_coordinate[3]-Object_coordinate[1]
                self.canvas.coords(self.selectObject,x-dx/2,y-dy/2,x+dx/2,y+dy/2)
                self.canvas.coords(self.adjointBox_id,(x-dx/2)-2,(y-dy/2)-2,(x+dx/2)+2,(y+dy/2)+2)
            if(type == "text"):
                adjoint_x = adjointBox_coordinate[0]
                adjoint_y = adjointBox_coordinate[1]
                adjoint_dx=adjointBox_coordinate[2]-adjointBox_coordinate[0]
                adjoint_dy=adjointBox_coordinate[3]-adjointBox_coordinate[1]
                if not(self.TextMoveFlag):
                    self.TextMoveFlag = True
                    self.MousetoText_dx = Object_coordinate[0] - x  
                    self.MousetoText_dy = Object_coordinate[1] - y
                else:
                    self.canvas.coords(self.selectObject, x+self.MousetoText_dx , y+self.MousetoText_dy)
                    self.canvas.coords(self.adjointBox_id, x+self.MousetoText_dx-(adjoint_dx/2) , y+self.MousetoText_dy-(adjoint_dy/2), x+self.MousetoText_dx+(adjoint_dx/2) , y+self.MousetoText_dy+(adjoint_dy/2))
                    
                





#~~~~~~~~~クリックを離すとdrawが呼ばれるようになっている~~~~~~~~~~

    def draw(self,event):
        self.TextMoveFlag = False
        if(self.func_B1_Motion_mode == "preview"):
            if(self.preview_flag==True):
                self.canvas.delete(self.id)
                if(self.preview_mode == "Line"):
                    self.id=self.canvas.create_line(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1,fill=self.MainColor)
                elif(self.preview_mode == "Rectangle"):
                    self.id=self.canvas.create_rectangle(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1,outline=self.MainColor)
                elif(self.preview_mode == "Oval"):
                    self.id=self.canvas.create_oval(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1,outline=self.MainColor)
                elif(self.preview_mode == "fillTriangle"):
                    self.id=self.canvas.create_polygon(self.initial_x,self.initial_y,self.final_x,self.initial_y,(self.initial_x+self.final_x)/2,self.final_y,fill=self.MainColor)
                elif(self.preview_mode == "fillRectangle"):
                    self.id=self.canvas.create_rectangle(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1,fill=self.MainColor,outline=self.MainColor)
                elif(self.preview_mode == "fillOval"):
                    self.id=self.canvas.create_oval(self.initial_x,self.initial_y,self.final_x,self.final_y,width=1,fill=self.MainColor,outline=self.MainColor)
                elif(self.preview_mode == "text"):
                    fontSize=abs(self.final_y-self.initial_y)
                    x=(self.initial_x+self.final_x)/2
                    y=(self.initial_y+self.final_y)/2
                    self.id=self.canvas.create_text( x , y ,text=" ",font=("Courier", fontSize , "bold"),fill=self.MainColor)
                else :
                    print("Error: preview is not define")

                self.parameterApp.makeWindow(self.id,self.preview_mode)
                self.preview_flag=False


    def Canvas_reset(self):#未実装
        self.sortComponentsLayer()

    def Delete_object(self,event):#未実装
        self.canvas.delete(self.selectObject)
        self.layer.pop(self.selectObject)
        
    def set_mouse_coordinate(self,event):
        mouse_X=event.x
        mouse_Y=event.y
        coordinate = str(event.x)+","+str(event.y)
        self.label_mouse_coordinate.set(coordinate)

    def export_xmlfile(self):
        target_Database=database_manage.Database_manage(r"C:\Users\81909\Documents\GitHub\ui_maker\src\components_test.xml")
        Canvas_data= self.export_canvas_components()
        target_Database.export_Database_as_xml(Canvas_data)
        for i in target_Database.get_UiCode("m5stack"):
            print(i)

    def export_canvas_components(self):
        Canvas_data={}
        self.delete_adjoint(None)
        for id in self.canvas.find_all():
            component={}
            image=""
            text=""
            fillColor=""
            outlineColor=""
            type = self.canvas.type(id)
            if(type == "polygon"):#tkinterのpolygonを三角形としてつかう
                type="triangle"

            tag = self.canvas.itemcget(id,"tags")
            coordinate=self.canvas.coords(id)

            component["tag"]= tag
            component["coordinate"] = coordinate
            component["layer"]=self.layer[id]

            if(type=="line"):
                fillColor = self.canvas.itemcget(id,"fill")
                component["lineColor"]=fillColor

            #line or rectangle or triangleが塗りつぶしなのかどうか~~~~~~~~~~~~~~~~~~~~
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
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



            elif(type=="text"):
                text = self.canvas.itemcget(id,"text")
                fillColor = self.canvas.itemcget(id,"fill")
                component["text"]=text
                component["fillColor"]=fillColor
            elif(type=="image"):
                image = self.canvas.itemcget(id,"image")

            component["type"]= type
            Canvas_data[id]=component

        return Canvas_data

    def change_nearestCoordinateX(self,coordinate,minimum_pixel):#minimum_pixelを最小単位として指定する座標を選択する
        if(coordinate > self.width):
            coordinate=self.width
        elif(coordinate < 0):
            coordinate=0
        else:
            x=np.arange(0,self.width+minimum_pixel,minimum_pixel)
            index=int(coordinate/minimum_pixel)
            coordinate =  x[index]
        return coordinate

    def change_nearestCoordinateY(self,coordinate,minimum_pixel):#minimum_pixelを最小単位として指定する座標を選択する
        if(coordinate > self.height):
            coordinate=self.height
        elif(coordinate < 0):
            coordinate=0
        else:
            y=np.arange(0,self.height+minimum_pixel,minimum_pixel)
            index=int(coordinate/minimum_pixel)
            coordinate = y[index]
        return coordinate

    def change_justCoordinateX(self,coordinate,minimum_pixel):
        if(coordinate > self.width):
            coordinate=self.width
        elif(coordinate < 0):
            coordinate=0
        else:
            x=np.arange(0,self.width+minimum_pixel,minimum_pixel)
            index=int(coordinate/minimum_pixel)
            coordinate =  x[index]

        return coordinate

    def change_justCoordinateY(self,coordinate,minimum_pixel):
        if(coordinate > self.height):
            coordinate=self.height
        elif(coordinate < 0):
            coordinate=0
        else:
            y=np.arange(0,self.height+minimum_pixel,minimum_pixel)
            index=int(coordinate/minimum_pixel)
            coordinate = y[index]

        return coordinate

    def sortComponentsLayer(self):
        for layer in np.arange(1,max(self.layer.values())+1):
            keys_id = [k for k, v in self.layer.items() if v == layer]
            for id in keys_id:
                self.canvas.lower(id)#layer順にオブジェクトを再配置

    def delete_adjoint(self,event):
        self.canvas.delete(self.adjointBox_id)#補助線を消去s

    def StopFunc_select(self):
        return 0;

    def AllModeOff(self):
        self.func_B1_Motion_mode=""
        self.func_B1_mode=""
        




root = tkinter.Tk()
app = Uimaker(master=root)
app.mainloop()
