import sqlite3 #Modulo de python para conexion con la base de datos de sqlite

class ConexionBD:

    def __init__(self):
        self._nameBD = 'database.db'
        self._insertQuery = 'INSERT INTO producto VALUES(null,?,?);'
        self._getQuery = 'SELECT * FROM producto ORDER BY nombre; '
        self._deleteQuery = 'DELETE FROM producto WHERE nombre = ?;'
       

    def getInsertQuery(self):
        return self._insertQuery

    def getDeleteQuery(self):
        return self._deleteQuery

    def getGeneralData(self,query,params = ()):
        with sqlite3.connect(self._nameBD) as init: #Creo conexio a base de datos
            cursor = init.cursor() #Creo un objeto que me permie hacer las consultas
            resultado = cursor.execute(query,params) #Metodo execute para usar senetencias sql
            init.commit()
        return resultado

    def insertQuery(self,query,params = ()):
        with sqlite3.connect(self._nameBD) as init: 
            cursor = init.cursor() 
            cursor.execute(query,params) 
            init.commit() 

    def getProducts(self):
        dbData = self.getGeneralData(self._getQuery)
        return dbData

        

    

