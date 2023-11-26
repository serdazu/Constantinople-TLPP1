import sqlite3

conexion=sqlite3.connect("key.db")
conexion.execute("insert into CONTRASEÑAS (Usuario,Contraseña)values (?,?)",
                  ("CONSTANTINOPLE", "U58K3Y.2023"))

#inserta informacion en la base de datos

conexion.commit()
conexion.close()