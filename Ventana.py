import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import Funciones

class FormularioCONTRASEÑAS:
    def __init__(self):
        self.articulo1=Funciones.CONTRASEÑAS()
        self.ventana1=tk.Tk()
        self.ventana1.attributes('-topmost', True)
        self.ventana1.title("Constantinople")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.carga_datos()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=20, pady=10)
        self.ventana1.mainloop()

    def carga_datos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de Datos")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Ingrese los datos solicitados")        
        self.labelframe1.grid(column=0, row=0, padx=10, pady=15)

        self.label1=ttk.Label(self.labelframe1, text="URL:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.urlcarga=tk.StringVar()
        self.entryuser=ttk.Entry(self.labelframe1, textvariable=self.urlcarga)
        self.entryuser.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe1, text="Usuario:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.usercarga=tk.StringVar()
        self.entryuser=ttk.Entry(self.labelframe1, textvariable=self.usercarga)
        self.entryuser.grid(column=1, row=1, padx=4, pady=4)

        self.label1=ttk.Label(self.labelframe1, text="Contraseña:")
        self.label1.grid(column=0, row=2, padx=4, pady=4)
        self.contracarga=tk.StringVar()
        self.entryuser=ttk.Entry(self.labelframe1, textvariable=self.contracarga)
        self.entryuser.grid(column=1, row=2, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def agregar(self):
        datos=(self.urlcarga.get(), self.usercarga.get(), self.contracarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        
        self.urlcarga.set("")
        self.usercarga.set("")
        self.contracarga.set("")


    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3)
        self.labelframe3.grid(column=0, row=0, padx=15, pady=15)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=10, pady=10)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=20)
        self.scrolledtext1.grid(column=0,row=1, padx=15, pady=15)

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END,
                                            "ID:"+str(fila[0])+
                                            "\nURL:"+str(fila[1])+
                                            "\nUsuario:"+str(fila[2])+
                                            "\nContraseña:"+str(fila[3])+
                                            "\nFecha:"+str(fila[4])+"\n\n")

    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de Datos")
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Datos a eliminar")        
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe4, text="ID:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe4, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe4, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos=(self.codigoborra.get(), )
        cantidad=self.articulo1.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró el usuario con dicho código")
        else:
            mb.showinfo("Información", "No existe un usuario con dicho código")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar Datos")
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Datos a modificar")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe5, text="ID:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe5, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe5, text="Usuario:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcionmod=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe5, textvariable=self.descripcionmod)
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe5, text="Contraseña:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe5, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

    def modifica(self):
        datos=(self.descripcionmod.get(), self.preciomod.get(), self.codigomod.get())
        cantidad=self.articulo1.modificacion(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el artículo")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")


aplicacion1=FormularioCONTRASEÑAS()
