import sqlite3

#Importo la librería SQLite

conexion=sqlite3.connect("key.db")

#Conecta y crea el archivo de base de datos

try:
    conexion.execute("""create table CONTRASEÑAS ( ID integer primary key autoincrement,
                     Usuario text,
                     Contraseña text)""")
    
#crea una base de datos (una table)

    print("se creo la tabla articulos")      

#En caso de tener exito imprime esto en consola
                  
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")   

#En caso de encontrar un error de cualquier índole, imprimirá que la tabla de atributos ya existe.

conexion.close()