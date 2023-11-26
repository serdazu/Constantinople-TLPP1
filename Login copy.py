import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import Funciones


root = tk.Tk()
root.geometry("760x360")
root.title("Constantinople")
img_boton = tk.PhotoImage(file="D:\progr\PRODUCCION.PROPIA\Constantinople\Ico2.png")
boton = ttk.Button(image=img_boton, command=root.destroy)
boton.place(x=0, y=0)
root.mainloop()

class LOGIN:
    def __init__():
        ventana1=tk.Tk()
        ventana1.title("Constantinople")
        cuaderno1 = ttk.Notebook(ventana1)   
        cuaderno1.grid(column=0, row=0, padx=20, pady=10)
        ventana1.mainloop()

 


        

aplicacion1=LOGIN()
