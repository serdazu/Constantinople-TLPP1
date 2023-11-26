import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import messagebox
from tkinter import scrolledtext as st
import sqlite3

def Validar():
       import Ventana


def abrir():
        try:
               conexion=sqlite3.Connection(database="Q:\KONSTANTINOPLE\key.db")
               cursor=conexion.execute("select ID,Usuario,Contraseña from CONTRASEÑAS")
               for fila in cursor:
                   print(fila)
                   fila=(1, 'CONSTANTINOPLE', 'U58K3Y.2023')
                   if fila:True, messagebox.showinfo(message="Se ha detectado el USB Key con éxito", title="Aviso"), Validar()
        
        except sqlite3.OperationalError:
               messagebox.showinfo(message="No se ha detectado el USB Key", title="Aviso")
               
        

def cerrar():
        root.destroy()


root = tk.Tk()
root.geometry("760x360")
root.title("Constantinople")
img_boton = tk.PhotoImage(file="D:\progr\PRODUCCION.PROPIA\Constantinople\Ico2.png")
boton = ttk.Button(image=img_boton, command=lambda:[cerrar(), abrir()])
boton.place(x=0, y=0)

root.mainloop()