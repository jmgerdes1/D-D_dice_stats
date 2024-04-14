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

tempvar = 5

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        label = ttk.Label(self,text="Dice Math",font = LARGEFONT)

        label.grid(row=0, column=0, padx=10, pady=10)

        varShSh = tk.IntVar()
        varStAi = tk.IntVar()

        e1_var = tk.IntVar()

        def input_to_var():
                e1_var.get()
                return(e1_var)

        def print_var():
            print(e1_var)

        c1 = tk.Checkbutton(self, text="Use Sharpshooter", variable=varShSh, onvalue=1, offvalue=0)
        c1.grid(row=1, column=0, padx=10, pady=10)

        c2 = tk.Checkbutton(self, text="Use Steady Aim", variable=varStAi, onvalue=1, offvalue=0)
        c2.grid(row=2, column=0, padx=10, pady=10)

        button1 = ttk.Button(self, text = "Go to Temp Page", command = lambda : controller.show_frame(Page1))
        button1.grid(row=3, column=0, padx=10, pady=10)

        tk.Label(self, text="Number of Faces:").grid(row=4, column=0, padx=10, pady=10)

        e1 = tk.Entry(self, textvariable=e1_var)
        e1.grid(row=4, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Enter", command=input_to_var)
        button2.grid(row=4, column=2, padx=10, pady=10)

        button3 = tk.Button(self, text = "Print", command=print_var)
        button3.grid(row=5, column=0, padx=10, pady=10)



class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Temp Page", font = LARGEFONT)
        label.grid(row=0, column=1, padx=10, pady=10)

        def print_var():
            print(tempvar)

        button1 = tk.Button(self, text = "<-", command = lambda : controller.show_frame(StartPage))
        button1.grid(row=0, column=0, padx=10, pady=10)

        button2 = tk.Button(self, text = "Print", command=print_var)
        button2.grid(row=1, column=0, padx=10, pady=10)


app=tkinterApp()
app.mainloop()