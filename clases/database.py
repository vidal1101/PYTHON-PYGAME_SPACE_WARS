""" arichvo donde se crea la conxion de la base de datos y se inserta los datos """
import sqlite3




"""guarda las partidas de cada ronda  """
def guardarJugadas(pTiros, pBajas):
    try:
        # crear data base y conexion
        conexion = sqlite3.connect('Space_WarsV1.db')
        cursor = conexion.cursor() 
        # crear table si no existe
        cursor.execute("create table IF NOT EXISTS Juego(idronda INTEGER PRIMARY KEY AUTOINCREMENT,bajas TEXT, tirosJugador TEXT)")
        cursor.execute("INSERT INTO Juego(bajas,tirosJugador) VALUES(" +str(pBajas)+ ",'" +str(pTiros)+ "')")
        # guardar dtos 
        conexion.commit()
        print('guardado')
        mostrarDatos()
        return 'Datos Guardados con Exito'
    except Exception as error:
            return error


"""muestra los datos de las partidas
y se guarda en una lista para luego retornarla  """
def mostrarDatos():
    
    try:
        
        lista=[]
        conexion = sqlite3.connect('Space_WarsV1.db')
        cursor = conexion.cursor()
    
        for row in cursor.execute('SELECT * FROM Juego'):
            #print(row)
            lista.append(row)
        
        return lista    
       
    except Exception :
        print('')
    
        
   
    
       
