import mysql.connector
class Basedato:
    def __init__(self):
        self.miBD=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="prueba",
            port="3306"
        )
    def _select(self,query,whereTupla):
        cursor=self.miBD.cursor()
        if len(whereTupla)>0:
            cursor.execute(query,whereTupla)
        else:
            cursor.execute(query)
        return cursor.fetchall()
        
    def _transacciones(self,queryInsert,tuplaInsert):
        cursor=self.miBD.cursor()
        cursor.execute(queryInsert,tuplaInsert)   
        self.miBD.commit()    
