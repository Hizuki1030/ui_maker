import tkinter
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
from PIL import Image, ImageDraw

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('UI maker')
        self.grid()
        self.setup()
        self.create_widgets()



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
        self.test_canvas.grid(row=1, column=1, columnspan=2,rowspan=4)
        self.test_canvas.bind('<B1-Motion>', self.draft)
        self.test_canvas.bind('<B1-Motion>',self.mouse_coordinate_viewer,"+")
        self.test_canvas.bind('<ButtonRelease-1>', self.draw)
        self.test_canvas.bind('<Motion>',self.mouse_coordinate_viewer)
        self.object_list.bind('<Double-1>',  self.object_property)

    def setup(self):
        self.start_x = 0
        self.start_y = 0
        self.old_x=None
        self.old_y=None
        self.now_x=0
        self.now_y=0
        self.start_canvas_draw_flag = False
        self.color = 'black'
        self.eraser_on = False
        self.object_coordinate_datas=[] #[[type,start_x,start_y,now_x,now_y]]
        self.line_object_index=0
        self.mode=None
        self.id=None
        self.drawing_id=None
        self.line_width=5
        self.list_object_id=[]
        self.object_tag_array=[]
        self.dash_color="blue"
        self.line_color="black"
        self.mouse_xaxis_id=0;
        self.mouse_yaxis_id=0;
        self.mouse_coordinate_x=0;
        self.mouse_coordinate_y=0;

    def object_property(self,event):
        print("object_property")
        root2=tkinter.Tk()


    def delete_object(self):
        itemIdxList=self.object_list.curselection()
        if(len(itemIdxList))==1:
            delete_target=str(self.object_tag_array[itemIdxList[0]])
            print("target TAG name:",delete_target)
            self.object_list.delete(itemIdxList[0])#itemIdxList:リストからインデックスを抽出して
            self.test_canvas.delete(delete_target)
            self.object_tag_array.pop(itemIdxList[0])
            self.list_object_id.pop(itemIdxList[0])
            print("object_tag_array",self.object_tag_array)

    def line_mode(self):
        self.mode="draw_line"

    def rectangle_mode(self):
        self.mode="draw_rect"

    def clear_canvas(self):
        self.test_canvas.delete(tkinter.ALL)



    def draft(self, event):
        self.line_width = int(self.line_width_entry.get())
        if(self.mode=="draw_line"):
            if(self.start_canvas_draw_flag==False):
                self.start_canvas_draw_flag=True
                self.start_x = self.mouse_coordinate_x
                self.start_y = self.mouse_coordinate_y
                self.old_x=self.start_x
                self.old_y=self.start_y
            else:
                self.now_x=int(self.mouse_coordinate_x)
                self.now_y=int(self.mouse_coordinate_y)
                if(self.now_x!=self.old_x or self.now_y!=self.old_y ):
                    self.test_canvas.delete(self.drawing_id)
                    self.drawing_id=self.test_canvas.create_line(self.start_x,self.start_y,self.now_x,self.now_y,width=self.line_width,dash=2)
                self.old_x=self.now_x
                self.old_y=self.now_y

        elif(self.mode=="draw_rect"):
            if(self.start_canvas_draw_flag==False):
                self.start_canvas_draw_flag=True
                self.start_x = self.mouse_coordinate_x
                self.start_y = self.mouse_coordinate_y
                self.old_x=self.start_x
                self.old_y=self.start_y
            else:
                self.now_x=self.mouse_coordinate_x
                self.now_y=self.mouse_coordinate_y
                if(self.now_x!=self.old_x or self.now_y!=self.old_y ):
                    self.test_canvas.delete(self.drawing_id)
                    self.drawing_id=self.test_canvas.create_rectangle(self.start_x,self.start_y,self.now_x,self.now_y,width=self.line_width,dash=2,outline=self.dash_color)
                self.old_x=self.now_x
                self.old_y=self.now_y

        #elif(self.mode=="move_object"):
        #    if(self.start_canvas_draw_flag==False):

    def draw(self,event):
        object_name_tag=""
        if(self.mode=="draw_line"):
            self.test_canvas.delete(self.drawing_id)
            object_name_tag=self.define_tag()
            self.id=self.test_canvas.create_line(self.start_x,self.start_y,self.now_x,self.now_y,width=self.line_width,fill=self.line_color,tag=object_name_tag)
            #print(self.id)
            line_coordinate=[object_name_tag,"line",self.start_x,self.start_y,self.now_x,self.now_y]
            self.object_coordinate_datas.append(line_coordinate)
            #print(self.object_coordinate_datas)
            self.line_object_index+=1
            self.start_canvas_draw_flag=False

        elif(self.mode=="draw_rect"):
            self.test_canvas.delete(self.drawing_id)
            object_name_tag=self.define_tag()
            self.id=self.test_canvas.create_rectangle(self.start_x,self.start_y,self.now_x,self.now_y,width=self.line_width,outline=self.line_color,tag=object_name_tag)
            rectangle_coordinate=["rect",self.start_x,self.start_y,self.now_y]
            self.object_coordinate_datas.append(rectangle_coordinate)
            self.line_object_index+=1
            self.start_canvas_draw_flag=False




        #print(self.object_tag_array)
        self.id=0

    def limit_coordinate(self):
        if(self.now_x > 320-self.line_width):
            self.now_x=320-self.line_width
        elif(self.now_x<1+self.line_width):
            self.now_x=1+self.line_width
        if(self.start_x>320-self.line_width):
            self.start_x=320-self.line_width
        elif(self.start_x<1+self.line_width):
            self.start_x=1+self.line_width

        if(self.now_y>240-self.line_width):
            self.now_y=240-self.line_width
        elif(self.now_y<1+self.line_width):
            self.now_y=1+self.line_width
        if(self.start_y>240-self.line_width):
            self.start_y=240-self.line_width
        elif(self.start_y<1+self.line_width):
            self.start_y=1+self.line_width

    def mouse_coordinate_viewer(self,event):
        self.test_canvas.delete(self.mouse_xaxis_id)
        self.test_canvas.delete(self.mouse_yaxis_id)
        self.mouse_coordinate_x=event.x
        self.mouse_coordinate_y=event.y
        self.limit_coordinate()
        self.mouse_xaxis_id=self.test_canvas.create_line(self.mouse_coordinate_x,0,self.mouse_coordinate_x,240,width=1,dash=2,fill="gray")
        self.mouse_yaxis_id=self.test_canvas.create_line(0,self.mouse_coordinate_y,320,self.mouse_coordinate_y,width=1,dash=2,fill="gray")
        self.mouse_coordinate_label_text.set(str(self.mouse_coordinate_x)+","+str(self.mouse_coordinate_y))

    def define_tag(self):
        flag=""
        object_name_tag=""
        while(flag!="decided"):
            object_name_tag = simpledialog.askstring("TAG", "タグの名前を入力",)
            print("Tag:",object_name_tag)
            if(object_name_tag in self.object_tag_array or object_name_tag== ""):
                pass
            else:
                    flag="decided"

        self.object_list.insert("end",object_name_tag)
        """self.object_tag_array.append(object_name_tag)
        print(self.object_coordinate_datas)"""
        return object_name_tag





root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
