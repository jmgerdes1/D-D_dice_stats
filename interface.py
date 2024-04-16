import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
import numpy as np
import scipy.signal
import convolve as conv

LARGEFONT = ("Verdana",35)


class tkinterApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        self.geometry("%dx%d" % (self.winfo_screenwidth(), self.winfo_screenheight()))

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (StartPage,Page1):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)

        self.createMenu()
        self.config(menu=self.menuBar)
        self.build_divider()

######################################################################################################
    
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    def run(self,str):
        os.system(str)

##############################################
#CREATES DIVIDER THAT SCALES WITH SCREEN SIZE#
##############################################

    def build_divider(self):
        self.divider = Canvas(self, width = self.winfo_screenwidth(), height = 1)
        self.divider.place(x=0,y=75)
        self.divider.create_line(0,1,self.winfo_screenwidth(),1, fill="black", width=3)

####################
#CREATE TOP MENUBAR#
####################

    def createMenu(self):
        self.menuBar = Menu(master=self)

    #####################
    #PAGE SELECTION MENU#
    #####################

        self.pageselect = Menu(self.menuBar, tearoff=0)
        self.pageselect.add_command(label="Home", command = lambda : self.show_frame(StartPage))
        self.pageselect.add_command(label="Test", command = lambda : self.show_frame(Page1))
        self.menuBar.add_cascade(label="Page Select", menu=self.pageselect)



############
#START PAGE#
############

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

    ############
    #PAGE LABEL#
    ############

        label = ttk.Label(self,text="Expected DPR Calculator",font = LARGEFONT)
        label.place(x=25, y=5)

    ############################################
    #CHECKBOXES FOR SHARPSHOOTER AND STEADY AIM#
    ############################################

        varShSh = tk.IntVar()

        varStAi = tk.IntVar()

        cb_sharp = tk.Checkbutton(self, text="Use Sharpshooter", variable=varShSh, onvalue=1, offvalue=0)
        cb_sharp.place(x=25, y=100)

        cb_steady = tk.Checkbutton(self, text="Use Steady Aim", variable=varStAi, onvalue=1, offvalue=0)
        cb_steady.place(x=25, y=125)

    #######################
    #DAMAGE DICE SELECTION#
    #######################

        varNum = tk.IntVar()
        varFaces = tk.IntVar()

        NUMOPTIONS = [1, 2]
        FACEOPTIONS = [4, 6, 8, 10, 12]

        tk.Label(self, text="Damage Dice:").place(x=25, y=150)

        om_num = OptionMenu(self, varNum, *NUMOPTIONS)
        om_num.place(x=110, y=150)

        tk.Label(self, text="d").place(x=160, y=150)

        om_faces = OptionMenu(self, varFaces, *FACEOPTIONS)
        om_faces.place(x=170, y=150)

    ###############################
    #CHARACTER AND ENEMY VARIABLES#
    ###############################

        tk.Label(self, text="Target AC:").place(x=300, y=100)

        e_AC = tk.Entry(self, width=10)
        e_AC.place(x=375, y=100)
        
        tk.Label(self, text="DEX Mod:").place(x=300, y=125)

        e_AM = tk.Entry(self, width=10)
        e_AM.place(x=375, y=125)

        tk.Label(self, text="PROF Mod:").place(x=300, y=150)

        e_PM = tk.Entry(self, width=10)
        e_PM.place(x=375, y=150)

        tk.Label(self, text="# of Attacks").place(x=300, y=175)

        e_nAtk = tk.Entry(self, width=10)
        e_nAtk.place(x=375,y=175)

    ###################
    #EDPR CALCULATIONS#
    ###################
        EDPR = float
        def run_EDPR():
            EDPR = conv.calc_EDPR(float(e_AC.get()), float(e_AM.get()), float(e_PM.get()), varShSh.get(), varStAi.get(), float(e_nAtk.get()), varFaces.get(), varNum.get())
            print(EDPR)
            textEDPR.set(str(round(EDPR,2)))

        textEDPR = StringVar()
        
        b_EDPR = tk.Button(self, text='Calculate Effective Damage/Round', command = run_EDPR)
        b_EDPR.place(x=25,y=500)

        tk.Label(self, textvariable=textEDPR, font=('Segoe UI',15)).place(x=100,y=540)

    ##############
    #TEST BUTTONS#
    ##############

        def print_vars():
            print(varShSh.get())
            print(varStAi.get())
            print(varNum.get())
            print(varFaces.get())
            print(e_AC.get())
            print(e_AM.get())
            print(e_PM.get())

        button_test = ttk.Button(self, text = "Test Button: Print Vars:", command = print_vars)
        button_test.place(x=5, y=1000)



###########
#TEMP PAGE#
###########

class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

    ############
    #PAGE LABEL#
    ############

        label = ttk.Label(self, text ="Temp Page", font = LARGEFONT)
        label.place(x=25, y=5)


app=tkinterApp()
app.mainloop()
