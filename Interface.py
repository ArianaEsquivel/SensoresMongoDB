import Sensores as s
import Registros_MongoDB as rm
import sys 
import time
from pymongo import MongoClient
import Registros_MySQL

def read():
    x = input()
    if x == "a" or x == "A": 
        values()
        menu()
    if x == "b" or x == "B":
        #r = rm.RegistroMongo
        #r.addRegistro()
        #sensores = s.Sensores()
        #data = sensores.getValores()
        #rr = Registros_MySQL
        #rr.addRegistroMysql(data)
        #rr.addDatosMysql(data)
        menu()
    if x == "c" or x == "C":
        while True:
            print("Guardando............................")
            time.sleep(60) 
    if x == "d" or x == "D": 
       print("Adios")
       sys.exit()

def menu():
    print("----------------Menú-----------------")
    print("a) Ver sensores......................")
    print("b) Guardar valores (una sola vez)....")
    print("c) Guardar valores (cada minuto).....")
    print("d) Salir.............................")
    read()

def values():
    print("----------------Sensores-------------")
    #sensores = s.Sensores()
    #data = sensores.getValores()
    print("............Valores.............")
    #print("Temperatura:",data[0])
    #print("Humedad:",data[1])
    #print("PIR:",data[2])
    #print("Ultrasonico:",data[3])

menu()