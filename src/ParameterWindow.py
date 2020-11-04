import tkinter
import tkinter.messagebox as tkm
class ParameterWindow:
    def __init__(self,parent,canvas,layer):
        self.layer=layer
        self.parent=parent
        self.canvas=canvas
        self.coodinate=[]
        self.save_mode=None

    def makeWindow(self,id,mode):
        self.id=id
        self.save_mode=mode

        coordinate=self.canvas.coords(id)
        coordinate=[int(x) for x in coordinate ]

        parentFrame = tkinter.Toplevel(self.parent)

        if(self.save_mode=="Line"):
            color=self.canvas.itemcget(id,"fill")
            #tkinter.Label(parentFrame,text="coordinate").grid(column=0,row=0)
            partsCoordinateX=0
            partsCoordinateY=1
            X1_Label = tkinter.Label(parentFrame,text="X1")
            X1_Label.grid(column=partsCoordinateX,row=partsCoordinateY)
            Y1_Label = tkinter.Label(parentFrame,text="Y1")
            Y1_Label.grid(column=partsCoordinateX,row=partsCoordinateY+1)
            X2_Label = tkinter.Label(parentFrame,text="X2")
            X2_Label.grid(column=partsCoordinateX,row=partsCoordinateY+2)
            Y2_Label = tkinter.Label(parentFrame,text="Y2")
            Y2_Label.grid(column=partsCoordinateX,row=partsCoordinateY+3)
            self.X1_entry = tkinter.Entry(parentFrame,width=10)
            self.X1_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY)
            self.Y1_entry = tkinter.Entry(parentFrame,width=10)
            self.Y1_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+1)
            self.X2_entry = tkinter.Entry(parentFrame,width=10)
            self.X2_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+2)
            self.Y2_entry = tkinter.Entry(parentFrame,width=10)
            self.Y2_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+3)
            #初期値の入力
            self.X1_entry.insert(tkinter.END,coordinate[0])
            self.Y1_entry.insert(tkinter.END,coordinate[1])
            self.X2_entry.insert(tkinter.END,coordinate[2])
            self.Y2_entry.insert(tkinter.END,coordinate[3])


            partsIdX = 0
            partsIdY = 0
            Label_Id = "ID :   " + str(id)
            tkinter.Label(parentFrame,text=Label_Id).grid(column=partsIdX,row=partsIdY,padx=(10,0))


            partsColorX = 2
            partsColorY = 1
            tkinter.Label(parentFrame,text="color :").grid(column=partsColorX,row=partsColorY,padx=(10,0))
            self.color_entry = tkinter.Entry(parentFrame,width=15)
            self.color_entry.grid(column=partsColorX+1,row=partsColorY,padx=(0,20))
            #初期値の入力
            self.color_entry.insert(tkinter.END,color)

            partsTagX = 2
            partsTagY = 2
            tkinter.Label(parentFrame,text="tag :").grid(column=partsTagX,row=partsTagY,padx=(10,0))
            self.tag_entry = tkinter.Entry(parentFrame,width=15)
            self.tag_entry.grid(column=partsTagX+1,row=partsTagY,padx=(0,20))


            partsLayerX = 2
            partsLayerY = 3
            tkinter.Label(parentFrame,text="layer :").grid(column=partsLayerX,row=partsLayerY,padx=(10,0))
            self.layer_entry = tkinter.Entry(parentFrame,width=15)
            self.layer_entry.grid(column=partsLayerX+1,row=partsLayerY,padx=(0,20))


            partsUpdatebuttonY = partsCoordinateY+4
            Update_button = tkinter.Button(parentFrame,text="UPDATE",command=self.updateParameter)
            Update_button.grid(column=3,row=partsUpdatebuttonY)


            partsCancelbuttonY = partsCoordinateY+4
            Cancelbutton = tkinter.Button(parentFrame,text="CANCEL",default=tkinter.ACTIVE)
            Cancelbutton.grid(column=2,row=partsUpdatebuttonY)



            partsOKbuttonY = partsCoordinateY+4
            ok_button = tkinter.Button(parentFrame,text="  OK  ",default=tkinter.ACTIVE)
            ok_button.grid(column=0,row=partsOKbuttonY,columnspan=2)

        elif(self.save_mode == "fillRectangle"):
            color=self.canvas.itemcget(id,"fill")
            #tkinter.Label(parentFrame,text="coordinate").grid(column=0,row=0)
            partsCoordinateX=0
            partsCoordinateY=1
            X1_Label = tkinter.Label(parentFrame,text="X1")
            X1_Label.grid(column=partsCoordinateX,row=partsCoordinateY)
            Y1_Label = tkinter.Label(parentFrame,text="Y1")
            Y1_Label.grid(column=partsCoordinateX,row=partsCoordinateY+1)
            X2_Label = tkinter.Label(parentFrame,text="X2")
            X2_Label.grid(column=partsCoordinateX,row=partsCoordinateY+2)
            Y2_Label = tkinter.Label(parentFrame,text="Y2")
            Y2_Label.grid(column=partsCoordinateX,row=partsCoordinateY+3)
            self.X1_entry = tkinter.Entry(parentFrame,width=10)
            self.X1_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY)
            self.Y1_entry = tkinter.Entry(parentFrame,width=10)
            self.Y1_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+1)
            self.X2_entry = tkinter.Entry(parentFrame,width=10)
            self.X2_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+2)
            self.Y2_entry = tkinter.Entry(parentFrame,width=10)
            self.Y2_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+3)
            #初期値の入力
            self.X1_entry.insert(tkinter.END,coordinate[0])
            self.Y1_entry.insert(tkinter.END,coordinate[1])
            self.X2_entry.insert(tkinter.END,coordinate[2])
            self.Y2_entry.insert(tkinter.END,coordinate[3])


            partsIdX = 0
            partsIdY = 0
            Label_Id = "ID :   " + str(id)
            tkinter.Label(parentFrame,text=Label_Id).grid(column=partsIdX,row=partsIdY,padx=(10,0))


            partsColorX = 2
            partsColorY = 1
            tkinter.Label(parentFrame,text="color :").grid(column=partsColorX,row=partsColorY,padx=(10,0))
            self.color_entry = tkinter.Entry(parentFrame,width=15)
            self.color_entry.grid(column=partsColorX+1,row=partsColorY,padx=(0,20))
            #初期値の入力
            self.color_entry.insert(tkinter.END,color)

            partsTagX = 2
            partsTagY = 2
            tkinter.Label(parentFrame,text="tag :").grid(column=partsTagX,row=partsTagY,padx=(10,0))
            self.tag_entry = tkinter.Entry(parentFrame,width=15)
            self.tag_entry.grid(column=partsTagX+1,row=partsTagY,padx=(0,20))


            partsLayerX = 2
            partsLayerY = 3
            tkinter.Label(parentFrame,text="layer :").grid(column=partsLayerX,row=partsLayerY,padx=(10,0))
            self.layer_entry = tkinter.Entry(parentFrame,width=15)
            self.layer_entry.grid(column=partsLayerX+1,row=partsLayerY,padx=(0,20))


            partsUpdatebuttonY = partsCoordinateY+4
            Update_button = tkinter.Button(parentFrame,text="UPDATE",command=self.updateParameter)
            Update_button.grid(column=3,row=partsUpdatebuttonY)


            partsCancelbuttonY = partsCoordinateY+4
            Cancelbutton = tkinter.Button(parentFrame,text="CANCEL",default=tkinter.ACTIVE)
            Cancelbutton.grid(column=2,row=partsUpdatebuttonY)



            partsOKbuttonY = partsCoordinateY+4
            ok_button = tkinter.Button(parentFrame,text="  OK  ",default=tkinter.ACTIVE)
            ok_button.grid(column=0,row=partsOKbuttonY,columnspan=2)

    def updateParameter(self):
        parameter=self.getParameter_fromEntry()
        self.setParameter(parameter[0],parameter[1])




    def getParameter_fromEntry(self):
        parameter_dict={}
        coordinate=[]
        result=[]
        if(self.save_mode == "Line"):
            X1=self.X1_entry.get()
            Y1=self.Y1_entry.get()
            X2=self.X2_entry.get()
            Y2=self.Y2_entry.get()
            coordinate.append(X1)
            coordinate.append(Y1)
            coordinate.append(X2)
            coordinate.append(Y2)
            #coordinate=[int(x) for x in coordinate ]

            tag=self.tag_entry.get()
            color=self.color_entry.get()
            layer=self.layer_entry.get()
            #~~辞書データの生成　例:{'coords': ['70', '30', '180', '120'], 'tag': 'hello', 'color': '#000000', 'layer': '1'}~~~~~~~~~
            parameter_dict["id"]=self.id
            parameter_dict["coords"]=coordinate
            parameter_dict["tag"]=tag
            parameter_dict["color"]=color
            parameter_dict["layer"]=layer
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            result.append("line")
            result.append(parameter_dict)

        elif(self.save_mode == "fillRectangle"):
            X1=self.X1_entry.get()
            Y1=self.Y1_entry.get()
            X2=self.X2_entry.get()
            Y2=self.Y2_entry.get()
            coordinate.append(X1)
            coordinate.append(Y1)
            coordinate.append(X2)
            coordinate.append(Y2)
            #coordinate=[int(x) for x in coordinate ]

            tag=self.tag_entry.get()
            color=self.color_entry.get()
            layer=self.layer_entry.get()
            #~~辞書データの生成　例:{'coords': ['70', '30', '180', '120'], 'tag': 'hello', 'color': '#000000', 'layer': '1'}~~~~~~~~~
            parameter_dict["id"]=self.id
            parameter_dict["coords"]=coordinate
            parameter_dict["tag"]=tag
            parameter_dict["color"]=color
            parameter_dict["layer"]=layer
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            result.append("line")
            result.append(parameter_dict)
        return result



    def setParameter(self,mode,parameter):#parameterの型はdict 例:{'coords': ['70', '30', '180', '120'], 'tag': 'hello', 'color': '#000000', 'layer': '1'}
        if(self.save_mode == "Line"):
            coordinate=parameter["coords"]
            self.canvas.coords(self.id,coordinate[0],coordinate[1],coordinate[2],coordinate[3])
            tag=parameter["tag"]
            self.canvas.itemconfig(self.id,tag=tag)
            color=parameter["color"]
            self.canvas.itemconfig(self.id,fill=color)
            self.layer[self.id]=parameter["layer"]
        elif(self.save_mode == "fillRectangle"):
            coordinate=parameter["coords"]
            self.canvas.coords(self.id,coordinate[0],coordinate[1],coordinate[2],coordinate[3])
            tag=parameter["tag"]
            self.canvas.itemconfig(self.id,tag=tag)
            color=parameter["color"]
            self.canvas.itemconfig(self.id,fill=color)
            self.layer[self.id]=parameter["layer"]
