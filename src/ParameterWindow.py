import tkinter
import tkinter.messagebox as tkm
class ParameterWindow:
    def __init__(self,parent,canvas,layer):
        self.layer={}
        self.layer=layer
        self.parent=parent
        self.canvas=canvas
        self.coodinate=[]
        self.save_mode=None
        self.numparts=0

    def makeWindow(self,id,mode):
        self.id=id
        self.save_mode=mode

        coordinate=self.canvas.coords(id)
        coordinate=[int(x) for x in coordinate ]

        self.parameterWindow = tkinter.Toplevel(self.parent)

        if(self.save_mode=="Line"):
            print("line mode running")
            color=self.canvas.itemcget(id,"fill")
            #tkinter.Label(self.parameterWindow,text="coordinate").grid(column=0,row=0)
            partsCoordinateX=0
            partsCoordinateY=1
            X0_Label = tkinter.Label(self.parameterWindow,text="X0")
            X0_Label.grid(column=partsCoordinateX,row=partsCoordinateY)
            Y0_Label = tkinter.Label(self.parameterWindow,text="Y0")
            Y0_Label.grid(column=partsCoordinateX,row=partsCoordinateY+1)
            X1_Label = tkinter.Label(self.parameterWindow,text="X1")
            X1_Label.grid(column=partsCoordinateX,row=partsCoordinateY+2)
            Y1_Label = tkinter.Label(self.parameterWindow,text="Y1")
            Y1_Label.grid(column=partsCoordinateX,row=partsCoordinateY+3)
            self.X0_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.X0_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY)
            self.Y0_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.Y0_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+1)
            self.X1_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.X1_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+2)
            self.Y1_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.Y1_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+3)
            #初期値の入力
            self.X0_entry.insert(tkinter.END,coordinate[0])
            self.Y0_entry.insert(tkinter.END,coordinate[1])
            self.X1_entry.insert(tkinter.END,coordinate[2])
            self.Y1_entry.insert(tkinter.END,coordinate[3])


            partsIdX = 0
            partsIdY = 0
            Label_Id = "ID :   " + str(id)
            tkinter.Label(self.parameterWindow,text=Label_Id).grid(column=partsIdX,row=partsIdY,padx=(10,0))


            partsColorX = 2
            partsColorY = 1
            tkinter.Label(self.parameterWindow,text="color :").grid(column=partsColorX,row=partsColorY,padx=(10,0))
            self.color_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.color_entry.grid(column=partsColorX+1,row=partsColorY,padx=(0,20))
            #初期値の入力
            self.color_entry.insert(tkinter.END,color)

            partsTagX = 2
            partsTagY = 2
            tkinter.Label(self.parameterWindow,text="tag :").grid(column=partsTagX,row=partsTagY,padx=(10,0))
            self.tag_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.tag_entry.grid(column=partsTagX+1,row=partsTagY,padx=(0,20))
            self.tag_entry.insert(tkinter.END,"part"+str(self.numparts))
            self.numparts=self.numparts+1



            partsLayerX = 2
            partsLayerY = 3
            tkinter.Label(self.parameterWindow,text="layer :").grid(column=partsLayerX,row=partsLayerY,padx=(10,0))
            self.layer_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.layer_entry.grid(column=partsLayerX+1,row=partsLayerY,padx=(0,20))

            self.layer_entry.insert(tkinter.END,"1")

            partsUpdatebuttonY = partsCoordinateY+4
            Update_button = tkinter.Button(self.parameterWindow,text="UPDATE",command=self.updateParameter)
            Update_button.grid(column=3,row=partsUpdatebuttonY)


            partsCancelbuttonY = partsCoordinateY+4
            Cancelbutton = tkinter.Button(self.parameterWindow,text="CANCEL",default=tkinter.ACTIVE,command=self.closeWindow)
            Cancelbutton.grid(column=2,row=partsUpdatebuttonY)

            partsOKbuttonY = partsCoordinateY+4
            ok_button = tkinter.Button(self.parameterWindow,text="  OK  ",default=tkinter.ACTIVE,command= self.saveParameterWindow)
            ok_button.grid(column=0,row=partsOKbuttonY,columnspan=2)

        elif(self.save_mode == "fillRectangle" or self.save_mode == "Rectangle"):
            color=None
            if(self.save_mode in "fill"):
                color=self.canvas.itemcget(id,"fill")
            else:
                color=self.canvas.itemcget(id,"outline")
            partsCoordinateX=0
            partsCoordinateY=1
            X0_Label = tkinter.Label(self.parameterWindow,text="X0")
            X0_Label.grid(column=partsCoordinateX,row=partsCoordinateY)
            Y0_Label = tkinter.Label(self.parameterWindow,text="Y0")
            Y0_Label.grid(column=partsCoordinateX,row=partsCoordinateY+1)
            X1_Label = tkinter.Label(self.parameterWindow,text="X1")
            X1_Label.grid(column=partsCoordinateX,row=partsCoordinateY+2)
            Y1_Label = tkinter.Label(self.parameterWindow,text="Y1")
            Y1_Label.grid(column=partsCoordinateX,row=partsCoordinateY+3)
            self.X0_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.X0_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY)
            self.Y0_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.Y0_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+1)
            self.X1_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.X1_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+2)
            self.Y1_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.Y1_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+3)
            #初期値の入力
            self.X0_entry.insert(tkinter.END,coordinate[0])
            self.Y0_entry.insert(tkinter.END,coordinate[1])
            self.X1_entry.insert(tkinter.END,coordinate[2])
            self.Y1_entry.insert(tkinter.END,coordinate[3])


            partsIdX = 0
            partsIdY = 0
            Label_Id = "ID :   " + str(id)
            tkinter.Label(self.parameterWindow,text=Label_Id).grid(column=partsIdX,row=partsIdY,padx=(10,0))


            partsColorX = 2
            partsColorY = 1
            tkinter.Label(self.parameterWindow,text="color :",fg=color).grid(column=partsColorX,row=partsColorY,padx=(10,0))
            self.color_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.color_entry.grid(column=partsColorX+1,row=partsColorY,padx=(0,20))
            #初期値の入力
            self.color_entry.insert(tkinter.END,color)

            partsTagX = 2
            partsTagY = 2
            tkinter.Label(self.parameterWindow,text="tag :").grid(column=partsTagX,row=partsTagY,padx=(10,0))
            self.tag_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.tag_entry.grid(column=partsTagX+1,row=partsTagY,padx=(0,20))
            self.tag_entry.insert(tkinter.END,"part"+str(self.numparts))
            self.numparts=self.numparts+1




            partsLayerX = 2
            partsLayerY = 3
            tkinter.Label(self.parameterWindow,text="layer :").grid(column=partsLayerX,row=partsLayerY,padx=(10,0))
            self.layer_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.layer_entry.grid(column=partsLayerX+1,row=partsLayerY,padx=(0,20))

            self.layer_entry.insert(tkinter.END,"1")

            partsUpdatebuttonY = partsCoordinateY+4
            Update_button = tkinter.Button(self.parameterWindow,text="UPDATE",command=self.updateParameter)
            Update_button.grid(column=3,row=partsUpdatebuttonY)


            partsCancelbuttonY = partsCoordinateY+4
            Cancelbutton = tkinter.Button(self.parameterWindow,text="CANCEL",default=tkinter.ACTIVE,command=self.closeWindow)
            Cancelbutton.grid(column=2,row=partsUpdatebuttonY)



            partsOKbuttonY = partsCoordinateY+4
            ok_button = tkinter.Button(self.parameterWindow,text="  OK  ",default=tkinter.ACTIVE,command= self.saveParameterWindow)
            ok_button.grid(column=0,row=partsOKbuttonY,columnspan=2)
        elif(self.save_mode == "fillOval" or self.save_mode == "Oval"):
            color=None
            if(self.save_mode in "fill"):
                color=self.canvas.itemcget(id,"fill")
            else:
                color=self.canvas.itemcget(id,"outline")
            partsCoordinateX=0
            partsCoordinateY=1
            X0_Label = tkinter.Label(self.parameterWindow,text="X0")
            X0_Label.grid(column=partsCoordinateX,row=partsCoordinateY)
            Y0_Label = tkinter.Label(self.parameterWindow,text="Y0")
            Y0_Label.grid(column=partsCoordinateX,row=partsCoordinateY+1)
            X1_Label = tkinter.Label(self.parameterWindow,text="X1")
            X1_Label.grid(column=partsCoordinateX,row=partsCoordinateY+2)
            Y1_Label = tkinter.Label(self.parameterWindow,text="Y1")
            Y1_Label.grid(column=partsCoordinateX,row=partsCoordinateY+3)
            self.X0_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.X0_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY)
            self.Y0_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.Y0_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+1)
            self.X1_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.X1_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+2)
            self.Y1_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.Y1_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+3)
            #初期値の入力
            self.X0_entry.insert(tkinter.END,coordinate[0])
            self.Y0_entry.insert(tkinter.END,coordinate[1])
            self.X1_entry.insert(tkinter.END,coordinate[2])
            self.Y1_entry.insert(tkinter.END,coordinate[3])

            partsIdX = 0
            partsIdY = 0
            Label_Id = "ID :   " + str(id)
            tkinter.Label(self.parameterWindow,text=Label_Id).grid(column=partsIdX,row=partsIdY,padx=(10,0))


            partsColorX = 2
            partsColorY = 1
            tkinter.Label(self.parameterWindow,text="color :").grid(column=partsColorX,row=partsColorY,padx=(10,0))
            self.color_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.color_entry.grid(column=partsColorX+1,row=partsColorY,padx=(0,20))
            #初期値の入力
            self.color_entry.insert(tkinter.END,color)

            partsTagX = 2
            partsTagY = 2
            tkinter.Label(self.parameterWindow,text="tag :").grid(column=partsTagX,row=partsTagY,padx=(10,0))
            self.tag_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.tag_entry.grid(column=partsTagX+1,row=partsTagY,padx=(0,20))
            self.tag_entry.insert(tkinter.END,"part"+str(self.numparts))
            self.numparts=self.numparts+1


            partsLayerX = 2
            partsLayerY = 3
            tkinter.Label(self.parameterWindow,text="layer :").grid(column=partsLayerX,row=partsLayerY,padx=(10,0))
            self.layer_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.layer_entry.grid(column=partsLayerX+1,row=partsLayerY,padx=(0,20))

            self.layer_entry.insert(tkinter.END,"1")


            partsUpdatebuttonY = partsCoordinateY+6
            Update_button = tkinter.Button(self.parameterWindow,text="UPDATE",command=self.updateParameter)
            Update_button.grid(column=3,row=partsUpdatebuttonY)


            partsCancelbuttonY = partsCoordinateY+6
            Cancelbutton = tkinter.Button(self.parameterWindow,text="CANCEL",default=tkinter.ACTIVE,command=self.closeWindow)
            Cancelbutton.grid(column=2,row=partsUpdatebuttonY)



            partsOKbuttonY = partsCoordinateY+6
            ok_button = tkinter.Button(self.parameterWindow,text="  OK  ",default=tkinter.ACTIVE,command= self.saveParameterWindow)
            ok_button.grid(column=0,row=partsOKbuttonY,columnspan=2)
        elif(self.save_mode == "fillTriangle"):
            color=None
            color=self.canvas.itemcget(id,"fill")
            partsCoordinateX=0
            partsCoordinateY=1
            X0_Label = tkinter.Label(self.parameterWindow,text="X0")
            X0_Label.grid(column=partsCoordinateX,row=partsCoordinateY)
            Y0_Label = tkinter.Label(self.parameterWindow,text="Y0")
            Y0_Label.grid(column=partsCoordinateX,row=partsCoordinateY+1)
            X1_Label = tkinter.Label(self.parameterWindow,text="X1")
            X1_Label.grid(column=partsCoordinateX,row=partsCoordinateY+2)
            Y1_Label = tkinter.Label(self.parameterWindow,text="Y1")
            Y1_Label.grid(column=partsCoordinateX,row=partsCoordinateY+3)
            X2_Label = tkinter.Label(self.parameterWindow,text="X2")
            X2_Label.grid(column=partsCoordinateX,row=partsCoordinateY+4)
            Y2_Label = tkinter.Label(self.parameterWindow,text="Y2")
            Y2_Label.grid(column=partsCoordinateX,row=partsCoordinateY+5)
            self.X0_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.X0_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY)
            self.Y0_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.Y0_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+1)
            self.X1_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.X1_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+2)
            self.Y1_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.Y1_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+3)
            self.X2_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.X2_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+4)
            self.Y2_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.Y2_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+5)
            #初期値の入力
            self.X0_entry.insert(tkinter.END,coordinate[0])
            self.Y0_entry.insert(tkinter.END,coordinate[1])
            self.X1_entry.insert(tkinter.END,coordinate[2])
            self.Y1_entry.insert(tkinter.END,coordinate[3])
            self.X2_entry.insert(tkinter.END,coordinate[4])
            self.Y2_entry.insert(tkinter.END,coordinate[5])

            partsIdX = 0
            partsIdY = 0
            Label_Id = "ID :   " + str(id)
            tkinter.Label(self.parameterWindow,text=Label_Id).grid(column=partsIdX,row=partsIdY,padx=(10,0))


            partsColorX = 2
            partsColorY = 1
            tkinter.Label(self.parameterWindow,text="color :").grid(column=partsColorX,row=partsColorY,padx=(10,0))
            self.color_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.color_entry.grid(column=partsColorX+1,row=partsColorY,padx=(0,20))
            #初期値の入力
            self.color_entry.insert(tkinter.END,color)

            partsTagX = 2
            partsTagY = 2
            tkinter.Label(self.parameterWindow,text="tag :").grid(column=partsTagX,row=partsTagY,padx=(10,0))
            self.tag_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.tag_entry.grid(column=partsTagX+1,row=partsTagY,padx=(0,20))
            self.tag_entry.insert(tkinter.END,"part"+str(self.numparts))
            self.numparts=self.numparts+1


            partsLayerX = 2
            partsLayerY = 3
            tkinter.Label(self.parameterWindow,text="layer :").grid(column=partsLayerX,row=partsLayerY,padx=(10,0))
            self.layer_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.layer_entry.grid(column=partsLayerX+1,row=partsLayerY,padx=(0,20))

            self.layer_entry.insert(tkinter.END,"1")

            partsUpdatebuttonY = partsCoordinateY+6
            Update_button = tkinter.Button(self.parameterWindow,text="UPDATE",command=self.updateParameter)
            Update_button.grid(column=3,row=partsUpdatebuttonY)

            partsCancelbuttonY = partsCoordinateY+6
            Cancelbutton = tkinter.Button(self.parameterWindow,text="CANCEL",default=tkinter.ACTIVE,command=self.closeWindow)
            Cancelbutton.grid(column=2,row=partsUpdatebuttonY)

            partsOKbuttonY = partsCoordinateY+6
            ok_button = tkinter.Button(self.parameterWindow,text="  OK  ",default=tkinter.ACTIVE,command= self.saveParameterWindow)
            ok_button.grid(column=0,row=partsOKbuttonY,columnspan=2)
        elif(self.save_mode=="text"):
            #color=self.canvas.itemcget(id,"fill")
            #tkinter.Label(self.parameterWindow,text="coordinate").grid(column=0,row=0)
            partsCoordinateX=0
            partsCoordinateY=1
            X0_Label = tkinter.Label(self.parameterWindow,text="X0")
            X0_Label.grid(column=partsCoordinateX,row=partsCoordinateY)
            Y0_Label = tkinter.Label(self.parameterWindow,text="Y0")
            Y0_Label.grid(column=partsCoordinateX,row=partsCoordinateY+1)

            self.X0_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.X0_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY)
            self.Y0_entry = tkinter.Entry(self.parameterWindow,width=10)
            self.Y0_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+1)

            #初期値の入力
            self.X0_entry.insert(tkinter.END,coordinate[0])
            self.Y0_entry.insert(tkinter.END,coordinate[1])

            name_Label = tkinter.Label(self.parameterWindow,text = "text")
            name_Label.grid(column=partsCoordinateX,row=partsCoordinateY+2)

            self.name_entry = tkinter.Entry(self.parameterWindow,width = 10)
            self.name_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+2)

            partsIdX = 0
            partsIdY = 0
            Label_Id = "ID :   " + str(id)
            tkinter.Label(self.parameterWindow,text=Label_Id).grid(column=partsIdX,row=partsIdY,padx=(10,0))

            partsColorX = 2
            partsColorY = 1
            tkinter.Label(self.parameterWindow,text="color :").grid(column=partsColorX,row=partsColorY,padx=(10,0))
            self.color_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.color_entry.grid(column=partsColorX+1,row=partsColorY,padx=(0,20))
            #初期値の入力
            color=self.canvas.itemcget(id,"fill")
            self.color_entry.insert(tkinter.END,color)

            partsTagX = 2
            partsTagY = 2
            tkinter.Label(self.parameterWindow,text="tag :").grid(column=partsTagX,row=partsTagY,padx=(10,0))
            self.tag_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.tag_entry.grid(column=partsTagX+1,row=partsTagY,padx=(0,20))
            self.tag_entry.insert(tkinter.END,"part"+str(self.numparts))
            self.numparts=self.numparts+1

            partsLayerX = 2
            partsLayerY = 3
            tkinter.Label(self.parameterWindow,text="layer :").grid(column=partsLayerX,row=partsLayerY,padx=(10,0))
            self.layer_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.layer_entry.grid(column=partsLayerX+1,row=partsLayerY,padx=(0,20))

            partsLayerX = 2
            partsLayerY = 4
            tkinter.Label(self.parameterWindow,text="font :").grid(column=partsLayerX,row=partsLayerY,padx=(10,0))
            self.font_entry = tkinter.Entry(self.parameterWindow,width=15)
            self.font_entry.grid(column=partsLayerX+1,row=partsLayerY,padx=(0,20))
            font=self.canvas.itemcget(id,"font")
            font = font.strip('Courier')
            font = font.strip('bold')
            font = font.strip()
            self.font_entry.insert(tkinter.END,font)

            self.layer_entry.insert(tkinter.END,"1")

            partsUpdatebuttonY = partsCoordinateY+4
            Update_button = tkinter.Button(self.parameterWindow,text="UPDATE",command=self.updateParameter)
            Update_button.grid(column=3,row=partsUpdatebuttonY)


            partsCancelbuttonY = partsCoordinateY+4
            Cancelbutton = tkinter.Button(self.parameterWindow,text="CANCEL",default=tkinter.ACTIVE,command=self.closeWindow)
            Cancelbutton.grid(column=2,row=partsUpdatebuttonY)

            partsOKbuttonY = partsCoordinateY+4
            ok_button = tkinter.Button(self.parameterWindow,text="  OK  ",default=tkinter.ACTIVE,command= self.saveParameterWindow)
            ok_button.grid(column=0,row=partsOKbuttonY,columnspan=2)

        else:
            print("Error:makeWindow no matching save_mode:",self.save_mode)

    def getParameter_fromEntry(self):
        parameter_dict={}
        coordinate=[]
        result=[]
        if(self.save_mode == "Line"):
            X0=self.X0_entry.get()
            Y0=self.Y0_entry.get()
            X1=self.X1_entry.get()
            Y1=self.Y1_entry.get()
            coordinate.append(X0)
            coordinate.append(Y0)
            coordinate.append(X1)
            coordinate.append(Y1)
            #coordinate=[int(x) for x in coordinate ]

            tag=self.tag_entry.get()
            color=self.color_entry.get()
            layer=int(self.layer_entry.get())
            #~~辞書データの生成　例:{'coords': ['70', '30', '180', '120'], 'tag': 'hello', 'color': '#000000', 'layer': '1'}~~~~~~~~~
            parameter_dict["id"]=self.id
            parameter_dict["coords"]=coordinate
            parameter_dict["tag"]=tag
            parameter_dict["color"]=color
            parameter_dict["layer"]=layer
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            result.append("line")
            result.append(parameter_dict)

        elif(self.save_mode == "fillRectangle" or self.save_mode == "Rectangle"):
            X0=self.X0_entry.get()
            Y0=self.Y0_entry.get()
            X1=self.X1_entry.get()
            Y1=self.Y1_entry.get()
            coordinate.append(X0)
            coordinate.append(Y0)
            coordinate.append(X1)
            coordinate.append(Y1)
            #coordinate=[int(x) for x in coordinate ]

            tag=self.tag_entry.get()
            color=self.color_entry.get()
            layer=int(self.layer_entry.get())
            #~~辞書データの生成　例:{'coords': ['70', '30', '180', '120'], 'tag': 'hello', 'color': '#000000', 'layer': '1'}~~~~~~~~~
            parameter_dict["id"]=self.id
            parameter_dict["coords"]=coordinate
            parameter_dict["tag"]=tag
            parameter_dict["color"]=color
            parameter_dict["layer"]=layer
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            result.append("line")
            result.append(parameter_dict)
        elif(self.save_mode == "fillOval" or self.save_mode == "Oval"):
            X0=self.X0_entry.get()
            Y0=self.Y0_entry.get()
            X1=self.X1_entry.get()
            Y1=self.Y1_entry.get()
            coordinate.append(X0)
            coordinate.append(Y0)
            coordinate.append(X1)
            coordinate.append(Y1)
            #coordinate=[int(x) for x in coordinate ]

            tag=self.tag_entry.get()
            color=self.color_entry.get()
            layer=int(self.layer_entry.get())
            #~~辞書データの生成　例:{'coords': ['70', '30', '180', '120'], 'tag': 'hello', 'color': '#000000', 'layer': '1'}~~~~~~~~~
            parameter_dict["id"]=self.id
            parameter_dict["coords"]=coordinate
            parameter_dict["tag"]=tag
            parameter_dict["color"]=color
            parameter_dict["layer"]=layer
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            result.append("line")
            result.append(parameter_dict)
        elif(self.save_mode == "fillTriangle"):
            X0=self.X0_entry.get()
            Y0=self.Y0_entry.get()
            X1=self.X1_entry.get()
            Y1=self.Y1_entry.get()
            X2=self.X2_entry.get()
            Y2=self.Y2_entry.get()
            coordinate.append(X0)
            coordinate.append(Y0)
            coordinate.append(X1)
            coordinate.append(Y1)
            coordinate.append(X2)
            coordinate.append(Y2)
            #coordinate=[int(x) for x in coordinate ]

            tag=self.tag_entry.get()
            color=self.color_entry.get()
            layer=int(self.layer_entry.get())
            #~~辞書データの生成　例:{'coords': ['70', '30', '180', '120'], 'tag': 'hello', 'color': '#000000', 'layer': '1'}~~~~~~~~~
            parameter_dict["id"]=self.id
            parameter_dict["coords"]=coordinate
            parameter_dict["tag"]=tag
            parameter_dict["color"]=color
            parameter_dict["layer"]=layer
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            result.append("line")
            result.append(parameter_dict)

        elif(self.save_mode == "text"):
            X0=self.X0_entry.get()
            Y0=self.Y0_entry.get()

            coordinate.append(X0)
            coordinate.append(Y0)
            #coordinate=[int(x) for x in coordinate ]

            text=self.name_entry.get()
            size=int(self.font_entry.get())
            tag=self.tag_entry.get()
            color=self.color_entry.get()
            layer=int(self.layer_entry.get())
            #~~辞書データの生成　例:{'coords': ['70', '30', '180', '120'], 'tag': 'hello', 'color': '#000000', 'layer': '1'}~~~~~~~~~
            parameter_dict["text"]=text
            parameter_dict["size"]=size
            parameter_dict["id"]=self.id
            parameter_dict["coords"]=coordinate
            parameter_dict["tag"]=tag
            parameter_dict["color"]=color
            parameter_dict["layer"]=layer
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            result.append("text")
            result.append(parameter_dict)
        else:
            print("Error:no matching savve_mode    getParameter_fromEntry()")
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
        elif(self.save_mode == "fillRectangle" or self.save_mode == "Rectangle" or self.save_mode=="Oval" or self.save_mode=="fillOval"):
            coordinate=parameter["coords"]
            self.canvas.coords(self.id,coordinate[0],coordinate[1],coordinate[2],coordinate[3])
            tag=parameter["tag"]
            self.canvas.itemconfig(self.id,tag=tag)
            color=parameter["color"]
            if(self.save_mode in "fill"):
                self.canvas.itemconfig(self.id,fill=color)
            else:
                self.canvas.itemconfig(self.id,outline=color)
            self.layer[self.id]=parameter["layer"]

        elif(self.save_mode == "fillTriangle"):
            coordinate=parameter["coords"]
            self.canvas.coords(self.id,coordinate[0],coordinate[1],coordinate[2],coordinate[3],coordinate[4],coordinate[5])
            tag=parameter["tag"]
            self.canvas.itemconfig(self.id,tag=tag)
            color=parameter["color"]
            if(self.save_mode in "fill"):
                self.canvas.itemconfig(self.id,fill=color)
            else:
                self.canvas.itemconfig(self.id,outline=color)
            self.layer[self.id]=parameter["layer"]
        elif(self.save_mode == "text"):
            coordinate=parameter["coords"]
            self.canvas.coords(self.id,coordinate[0],coordinate[1])
            tag=parameter["tag"]
            self.canvas.itemconfig(self.id,tag=tag)
            text=parameter["text"]
            self.canvas.itemconfig(self.id,text=text)
            size=parameter["size"]
            self.canvas.itemconfig(self.id,font=("Courier",size))
            color=parameter["color"]
            self.canvas.itemconfig(self.id,fill=color)
            self.layer[self.id]=parameter["layer"]
        else:
            print("Error:no matching save_mode    setParameter()")

    def updateParameter(self):
        parameter=self.getParameter_fromEntry()
        self.setParameter(parameter[0],parameter[1])

    def closeWindow(self):
        self.canvas.delete(self.id)
        self.parameterWindow.destroy()


    def saveParameterWindow(self):
        self.updateParameter()
        self.parameterWindow.destroy()
