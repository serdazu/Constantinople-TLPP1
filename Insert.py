import sqlite3

conexion=sqlite3.connect("DatBas.db")
conexion.execute("insert into CONTRASEÑAS (URL,Usuario,Contraseña,Fecha)values (?,?,?,datetime('now'))",
                  ("www.whatsappweb.com", "Zugasti", "789456",  ))

#inserta informacion en la base de datos

conexion.commit()
conexion.close()