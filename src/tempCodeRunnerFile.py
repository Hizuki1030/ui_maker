command = self.selectObject_func)#オブジェクト選択モード
        self.export_button.grid(row=0, column=7,columnspan=1,rowspan=1)

        self.export_button = tkinter.Button(self, text='info', command = self.infomationObject)#選択されたオブジェクトのパラメータ設定ウィンドウを開く
        self.export_button.grid(row=1, column=7,columnspan=1,rows