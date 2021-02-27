import Sensores as s
import Registros_MongoDB
import sys 
import time
from pymongo import MongoClient
import Registros_MySQL

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["Bullsito"]
sensores = db["Sensores"]
nid = sensores.find()
list = []
for x in nid:
    nids = x["_id"]
    #print(nids)
    list.append(nids)
def read():
    x = input()
    if x == "a" or x == "A": 
        values()
        menu()
    if x == "b" or x == "B":
        #values()
        r = Registros_MongoDB
        r.addRegistro(list)
        sensores = s.Sensores()
        data = sensores.getValores()
        rr = Registros_MySQL
        rr.addRegistroMysql(data)
        #rr.addDatosMysql(data)
        menu()
    if x == "c" or x == "C": 
       print("Adios")
       sys.exit()

def menu():
    print("----------------Menú-----------------")
    print("a) Ver sensores......................")
    print("b) Guardar valores...................")
    print("c) Salir.............................")
    read()

def values():
    print("----------------Sensores-------------")
    sensores = s.Sensores()
    data = sensores.getValores()
    print("............Valores.............")
    print("Temperatura:",data[0])
    print("Humedad:",data[1])
    print("PIR:",data[2])
    print("Ultrasonico:",data[3])

menu()