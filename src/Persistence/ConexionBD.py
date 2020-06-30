import sqlite3 #Modulo de python para conexion con la base de datos de sqlite
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")

class ConexionBD(object):
    def __init__(self):
        self._nameBD = 'database.db'


    def getGeneralData(self,query,params = ()):
        with sqlite3.connect(self._nameBD) as init: #Creo conexio a base de datos
            cursor = init.cursor() #Creo un objeto que me permie hacer las consultas
            resultado = cursor.execute(query,params) #Metodo execute para usar senetencias sql
            init.commit()
        return resultado

    def getProducts(self):
        consulta = 'SELECT * FROM producto ORDER BY nombre '
        dbData = self.getGeneralData(consulta)
        print(dbData)

