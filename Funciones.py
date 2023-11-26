import sqlite3
import tkinter
from tkinter import messagebox


class CONTRASEÑAS:

    def DatBas():
        conexion=sqlite3.connect("DatBas.db")
        try:
            conexion.execute("""create table CONTRASEÑAS ( ID integer primary key autoincrement,
                            URL text,
                            Usuario text,
                            Contraseña text,
                            Fecha text)""") 
            print("se creo la tabla articulos")
            conexion.close()
        except sqlite3.OperationalError:
            print("La tabla articulos ya existe")  

    def abrir(self):
        conexion=sqlite3.connect("D:\progr\PRODUCCION.PROPIA\Constantinople\DatBas.db")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into CONTRASEÑAS (URL,Usuario,Contraseña,Fecha)values (?,?,?,datetime('now'))"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select ID,URL,Usuario,Contraseña,Fecha from CONTRASEÑAS"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def baja(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from CONTRASEÑAS where ID=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas borradas
        except:
            cone.close()
    
    def modificacion(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update CONTRASEÑAS set URL=?, Usuario=?, Fecha=datetime('now') where ID=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas modificadas            
        except:
            cone.close()

    def validar ():
        conexion=sqlite3.Connection(database="Q:\KONSTANTINOPLE\key.db")
        cursor=conexion.execute("select ID,Usuario,Contraseña from CONTRASEÑAS")
        if conexion:True
        for fila in cursor:
            print(fila)
            fila=(1, 'CONSTANTINOPLE', 'U58K3Y.2023')
            if fila:True
            messagebox.showinfo(message="Se ha detectado el USB Key con éxito", title="Aviso")
            import Ventana



