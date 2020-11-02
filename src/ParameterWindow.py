import tkinter
import tkinter.messagebox as tkm
class ParameterWindow:
    def __init__(self,parent,canvas):
        self.parent=parent
        self.canvas=canvas
        self.coodinate=[]
        self.save_mode=None

    def LineWindow(self,id):
        self.save_mode="line"
        coordinate=self.canvas.coords(id)
        color=self.canvas.itemcget(id,"fill")
        parentFrame = tkinter.Toplevel(self.parent)
        parentFrame.geometry("300x200")


        tkinter.Label(parentFrame,text="coordinate").grid(column=0,row=0)
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
        X1_entry = tkinter.Entry(parentFrame,width=10)
        X1_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY)
        Y1_entry = tkinter.Entry(parentFrame,width=10)
        Y1_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+1)
        X2_entry = tkinter.Entry(parentFrame,width=10)
        X2_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+2)
        Y2_entry = tkinter.Entry(parentFrame,width=10)
        Y2_entry.grid(column=partsCoordinateX+1,row=partsCoordinateY+3)
        #初期値の入力
        X1_entry.insert(tkinter.END,coordinate[0])
        Y1_entry.insert(tkinter.END,coordinate[1])
        X2_entry.insert(tkinter.END,coordinate[2])
        Y2_entry.insert(tkinter.END,coordinate[3])


        partsColorX = 2
        partsColorY = 0
        tkinter.Label(parentFrame,text="color:").grid(column=partsColorX,row=partsColorY,padx=(10,0))
        color = tkinter.Entry(parentFrame,width=10)
        color.grid(column=partsColorX+1,row=partsColorY)



        partsOKbuttonY = partsCoordinateY+4
        ok_button = tkinter.Button(parentFrame,text="OK",command=self.saveParameter,default=tkinter.ACTIVE)
        ok_button.grid(column=0,row=partsOKbuttonY)



    def saveParameter(self):
        return 0
