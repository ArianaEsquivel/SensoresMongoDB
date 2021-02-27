from pymongo import MongoClient
from datetime import datetime as time


x = time.now()
format = x.strftime("%c")
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["Bullsito"]
sensores = db["Sensores"]
#tempyhum = sensores.find({"Sensor":"Temperatura y humedad"})
#for x in tempyhum:
 #   temperaturaid = x["_id"]
  #  print(temperaturaid)
#ultra = sensores.find({"Sensor":"Ultrasonico"})
#for x in ultra:
 #   print(x["_id"])
  #  pir = sensores.find({"Sensor":"PIR"})
#for x in pir:
 #   print(x["_id"])
sensores.insert({"_id": 3, "Sensor": "pir", "Fecha": format})