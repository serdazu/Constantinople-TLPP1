import sqlite3


conexion=sqlite3.connect("DatBas.db")
cursor=conexion.execute("select ID,URL,Usuario,Contraseña,Fecha from CONTRASEÑAS")
for fila in cursor:
    print(fila)

#selecciona e imprime los valores de la tabla de datos

conexion.close()