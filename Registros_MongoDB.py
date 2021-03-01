import Sensores as s
from pymongo import MongoClient
from datetime import datetime as time

class RegistroMongo():
    def __init__(self):
        self.connection =[{"client" : "mongodb://127.0.0.1:27017/", "db" : "Bullsito", "valores" : "Valores"}]

    def addRegistro(self):
        cm = self.connection["client"]
        bd = self.connection["db"]
        coll = self.connection["valores"]
        v = s.SensoresObject()
        values = v.getValores()
        temperaturaid = str(v.sensores[0]["_id"])
        temperatura = values[1]
        humedadid = str(v.sensores[0]["_id"])
        humedad = values[0]
        ultrasonicoid = str(v.sensores[1]["_id"])
        ultrasonico = values[3]
        pirid = str(v.sensores[2]["_id"])
        sPIR = values[2]
        client = MongoClient(cm)
        db = client[bd]
        x = time.now()
        valores = db[coll]
        format = x.strftime("%c")
        nid = valores.find().sort("_id",-1).limit(1)
        for x in nid:
            f = int(x["_id"])+1
            valores.insert({ "_id": f , humedadid: humedad, temperaturaid: temperatura, pirid: sPIR, ultrasonicoid: ultrasonico, "Fecha": format})
        client.close()

