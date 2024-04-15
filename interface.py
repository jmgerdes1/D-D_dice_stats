import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
import numpy as np
import scipy.signal

LARGEFONT = ("Verdana",35)

class tkinterApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

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
    
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    def run(self,str):
        os.system(str)

############
#START PAGE#
############

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

    ############
    #PAGE LABEL#
    ############

        label = ttk.Label(self,text="Dice Math",font = LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)

    ############################################
    #CHECKBOXES FOR SHARPSHOOTER AND STEADY AIM#
    ############################################

        varShSh = tk.IntVar()

        varStAi = tk.IntVar()

        cb_sharp = tk.Checkbutton(self, text="Use Sharpshooter", variable=varShSh, onvalue=1, offvalue=0)
        cb_sharp.grid(row=2, column=0, padx=10, pady=10)

        cb_steady = tk.Checkbutton(self, text="Use Steady Aim", variable=varStAi, onvalue=1, offvalue=0)
        cb_steady.grid(row=3, column=0, padx=10, pady=10)

    ###########################
    #BUTTON TO GO TO TEMP PAGE#
    ###########################

        button1 = ttk.Button(self, text = "Go to Temp Page", command = lambda : controller.show_frame(Page1))
        button1.grid(row=1, column=0, padx=10, pady=10)

    #######################
    #DAMAGE DICE SELECTION#
    #######################

        varNum = tk.IntVar()
        varFaces = tk.IntVar()

        NUMOPTIONS = [1, 2]
        FACEOPTIONS = [4, 6, 8, 10, 12]

        tk.Label(self, text="Damage Dice:").grid(row=4, column=0, padx=5, pady=10)

        om_num = OptionMenu(self, varNum, *NUMOPTIONS)
        om_num.grid(row=4, column=1, padx=1, pady=10)

        tk.Label(self, text="d").grid(row=4, column=2, padx=1, pady=10)

        om_faces = OptionMenu(self, varFaces, *FACEOPTIONS)
        om_faces.grid(row=4, column=3, padx=1, pady=10)

    ##############
    #TEST BUTTONS#
    ##############

        def print_vars():
            print(varShSh.get())
            print(varStAi.get())
            print(varNum.get())
            print(varFaces.get())

        button_test = ttk.Button(self,text = "Test Button: Print Vars:", command = print_vars)
        button_test.grid(row=10, column=0, padx=10, pady=10)



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
        label.grid(row=0, column=1, padx=10, pady=10)


app=tkinterApp()
app.mainloop()
