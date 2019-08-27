# Python 3
# -*- coding: UTF-8 -*-
#
# 03/21/19 Porting to gLinux, UI optimization. Added CHT/ENG mode switch
# 02/19/19 New simple version with Google Translate
# 08/29/18 added auto translattion, always on top.
# 08/27/18 added tkinter, cht-chs translation font chaged, changed md5 locatoin to enable continuous translation.
# 08/27/18 created based on yodao API engine, dummy UI.
#=======================================================
import pyperclip
import hashlib
import random
import requests
import time
import json
from tkinter import *
from PIL import Image, ImageTk
import threading
from googletrans import Translator

root = Tk() # create master windows
T = Text(root, height=25, width=200,font=("新細明體",12,"normal"))
T.pack()
T.insert(END,"將翻譯文字拷貝至剪貼簿再執行智能翻譯\n")
T.insert(END,"Copy text to clipboard and start translation\n")

# Moved btn text to global
autoSwitchBtn_text = StringVar()# Python 3
bilinSwitchBtn_text = StringVar()
# for CHT/ENG switch
chtSwitchBtn_text = StringVar()

s = requests.Session()
m = hashlib.md5()

##++ tkinter ==================================================
class Window(Frame):
    # init windows
    def __init__(self, master=None):
        # Frame init with maser windows.
        Frame.__init__(self, master)
        # reference to tk windows master
        self.master = master

        #執行init_window()
        self.init_window()
        self._isAuto = False
        self._isBilingual = False
        self._isCHT = True
        self._lastTranslated = ""

    #init_window（） and init windows control
    def init_window(self):
        # Change window title
        self.master.title("My Google Translator - Gauss Mindworks Inc")
        # pack widget into container
        self.pack(fill=BOTH, expand=1)
        # create button
        translateButton = Button(self, text="Translate(智能翻譯)",command=self.client_translate)

        global autoSwitchBtn_text
        global bilinSwitchBtn_text
        global chtSwitchBtn_text

        autoSwitchButton = Button(self, textvariable=autoSwitchBtn_text,command=self.client_auto_switch)
        autoSwitchBtn_text.set("Auto Translation On")

        bilinSwitchButton = Button(self,textvariable=bilinSwitchBtn_text,command=self.client_auto_bilingual)
        bilinSwitchBtn_text.set("Binlingual On")

        # added CHT/ENG switch button
        chtSwitchButton = Button(self,textvariable=chtSwitchBtn_text,command=self.client_auto_chteng)
        chtSwitchBtn_text.set("中文")

        quitButton = Button(self, text="Quit",command=self.client_exit)
        # place button in window
        translateButton.place(x=00,y=0)
        autoSwitchButton.place(x=300, y=0)
        bilinSwitchButton.place(x=600, y=0)
        chtSwitchButton.place(x=900, y=0)
        quitButton.place(x=1100, y=0)

    def client_translate(self):
        ## global dic
        global root

        #T.delete(0,END)
        print("Start Translate\n")
        #pyperclip.copy("""今天天氣# Python 3

        msg = pyperclip.paste()
        if msg == "" :
            msg = """今天天氣如何"""# Python 3
# -*- coding: UTF-8 -*-
#
# 03/21/19 Porting to gLinux, UI optimization. Added CHT/ENG mode switch
# 02/19/19 New simple version with Google Translate
# 08/29/18 added auto translattion, always on top.
# 08/27/18 added tkinter, cht-chs translation font chaged, changed md5 locatoin to enable continuous translation.
# 08/27/18 created based on yodao API engine, dummy UI.
#=======================================================

        if self._lastTranslated==msg:
            if self._isAuto == True:
                # keep doing auto translation
                self._timer = threading.Timer(2.0,self.client_translate)
                self._timer.start()
            return

        T.delete(1.0,END)
        translator = Translator()

        if self._isCHT==True:
            translation = translator.translate(msg,dest='zh-tw')
        else:
            translation = translator.translate(msg,dest='en')

        print(translation.origin, ' -> ', translation.text)
        chtMsg = translation.text

        self._lastTranslated = msg
        if self._isBilingual==True:
            T.insert(END,msg+"\n========\n")

        T.insert(END,chtMsg)

        if self._isAuto == True:
            # keep doing auto translation
            self._timer = threading.Timer(2.0,self.client_translate)
            self._timer.start()

    def client_auto_switch(self):
        global autoSwitchBtn_text
        global bilinSwitchBtn_text

        if self._isAuto == False:
            self._timer = threading.Timer(2.0,self.client_translate)
            self._timer.start()
            self._isAuto = True
            autoSwitchBtn_text.set("Auto Translation OFF")
            print("start auto translation\n")
        else:
            self._isAuto = False
            self._timer.cancel()
            autoSwitchBtn_text.set("Auto Translation On")

        #global root
        #root.lift()

    def client_auto_bilingual(self):
        global autoSwitchBtn_text
        global bilinSwitchBtn_text
        if self._isBilingual == False:
            self._isBilingual = True
            bilinSwitchBtn_text.set("Binlingual OFF")
            print("bilingual ON")
        else:
            self._isBilingual = False
            bilinSwitchBtn_text.set("Binlingual On")
            print("binlingual OFF")

    def client_auto_chteng(self):
        global autoSwitchBtn_text
        global chtSwitchBtn_text
        if self._isCHT == False:
            self._isCHT = True
            chtSwitchBtn_text.set("中文")
            print("CHT mode")
        else:
            self._isCHT = False
            chtSwitchBtn_text.set("ENG")
            print("ENG mode")

    def client_exit(self):
        if self._isAuto == True:
            self._isAuto = False
            self._timer.cancel()
            autoSwitchBtn_text.set("Auto Translation On")
        exit()

msg = pyperclip.paste()
#gWindows settings.
#root.geometry("640x480")

#gLinux resolution
root.geometry("1280x1000")    #Set windows size
app = Window(root)          #create window
root.configure(background='gold')
#root.lift()
root.attributes('-topmost', 'true')
root.mainloop()             #mainloop
