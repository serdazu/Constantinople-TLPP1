import sqlite3

conexion=sqlite3.connect("DatBas.db")
ID=int(input("Ingrese el código de un artículo:"))
cursor=conexion.execute("select URL, Usuario, Contraseña, Fecha where CONTRASEÑAS=?", (ID, ))
fila=cursor.fetchone()
if fila!=None:
    print(fila)
else:
    print("No existe un artículo con dicho código.")
conexion.close()