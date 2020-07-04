import sqlite3 #Modulo de python para conexion con la base de datos de sqlite

class ConexionBD:

    def __init__(self):
        self._nameBD = 'database.db'
        self._insertQuery = 'INSERT INTO producto VALUES(null,?,?)'

    def getInsertQuery(self):
        return self._insertQuery

    def getGeneralData(self,query,params = ()):
        with sqlite3.connect(self._nameBD) as init: #Creo conexio a base de datos
            cursor = init.cursor() #Creo un objeto que me permie hacer las consultas
            resultado = cursor.execute(query,params) #Metodo execute para usar senetencias sql
            init.commit()
        return resultado

    def insertData(self,query,params = ()):
        with sqlite3.connect(self._nameBD) as init: 
            cursor = init.cursor() 
            cursor.execute(query,params) 
            init.commit() 

    def getProducts(self):
        consulta = 'SELECT * FROM producto ORDER BY nombre '
        dbData = self.getGeneralData(consulta)
        return dbData

        

    

