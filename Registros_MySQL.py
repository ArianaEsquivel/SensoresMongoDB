import mysql.connector
from mysql.connector import Error
from datetime import datetime as time
import Registros_MongoDB

class ConexionMySQL:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='root', 
                                    password='',
                                    host='127.0.0.1',
                                    database='Bullsito')
            
            if self.cnx.is_connected():
                print("Conectado a mysql")
                self.cursor = self.cnx.cursor()
        except Error as ex:
            print("Error", ex)
        finally:
            if self.cnx.is_connected():
                self.cnx.close()
    
    def insertarRegistro(self, sentencia):
        try:
            self.cnx = mysql.connector.connect(user='admin', 
                                    password='123',
                                    host='127.0.0.1',
                                    database='Bullsito')
            if self.cnx.is_connected():
                self.cursor = self.cnx.cursor()
                self.cursor.execute(sentencia)
                self.cnx.commit()
        except Error as ex:
            print("Error", ex)
        finally:
            if self.cnx.is_connected():
                self.cnx.close()

    def consulta(self, sentencia):
        try:
            self.cnx = mysql.connector.connect(user='admin', 
                                    password='123',
                                    host='127.0.0.1',
                                    database='Bullsito')
            if self.cnx.is_connected():
                self.cursor = self.cnx.cursor()
                self.cursor.execute(sentencia)
                self.resultados = self.cursor.fetchall()
                return self.resultados
        except Error as ex:
            """print("Error", ex)"""
        finally:
            if self.cnx.is_connected():
                self.cnx.close()
                
cnxmy = ConexionMySQL()

def addDatosMysql(datos):
    print(datos)
    #cnxmy.insertarRegistro("INSERT INTO valores (sensor_id, boolaneo) VALUES (1,"+datos[0]+")") #humedad
    #cnxmy.insertarRegistro("INSERT INTO valores (sensor_id, flotante) VALUES (2,"+datos[1]+")") #temperatura
    cnxmy.insertarRegistro("INSERT INTO valores (sensor_id, flotante) VALUES (3,"+str(datos[2])+")") #pir
    cnxmy.insertarRegistro("INSERT INTO valores (sensor_id, flotante) VALUES (4,"+str(datos[3])+")") #ultrasonico

def addRegistroMysql(datos):
    #print("DATOS")
    #print(datos)
    ids = cnxmy.consulta("SELECT id FROM sensores")
    #1 hum
    #2 tem
    #3 pir
    #4 ult
    cam = ""
    for s in ids:
        #print(s[0])
        ins = s[0]-1
        #print(type(datos[ins]))
        if type(datos[ins]) != type(None):
            #print("if",datos[ins])
            if s[0] == 1:
                cam = "boolaneo"
            else:
                cam = "flotante"
            cnxmy.insertarRegistro("INSERT INTO valores (sensor_id,"+cam+") VALUES ("+str(s[0])+","+str(datos[ins])+")")

