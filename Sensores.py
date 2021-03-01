import adafruit_dht as adafruit_dht
import  RPI.GPIO as GPIO
import time
<<<<<<< HEAD
import serialize as s
=======
>>>>>>> e34cf2b5a85f4010696ea98c08b1c18514a3feb5
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["Bullsito"]
sensor = db["Sensores"]
dht11 = sensor.find({"Sensor" : "dht11"})
for d in dht11:
    dht11id = d["_id"]
hc_sr04 = sensor.find({"Sensor" : "hc-sr04"})
for h in hc_sr04:
    hc_sr04id = h["_id"]
pir = sensor.find({"Sensor" : "pir"})
for p in pir:
    pirid = p["_id"]
    
class SensoresObject():
    def __init__(self):
        self.sensores = [{"_id":dht11id, "valor":0, "nombre":"dth11", "tipo": "", "puerto_1":6, "puerto_2":0},
        {"id":hc_sr04id, "valor":0, "nombre":"hc-sr04", "tipo": "", "puerto_1":23, "puerto_2":24},
        {"id":pirid, "valor":0, "nombre":"pir", "tipo": "", "puerto_1":21, "puerto_2":0}]
<<<<<<< HEAD
=======

>>>>>>> e34cf2b5a85f4010696ea98c08b1c18514a3feb5
        #for x in self.sensores:
         #   d = "insert into valores (sensor_id, x.tipo) values (x.valor, x.id)"
            #ejemplo del profe

    def getPir(self):
        pin = self.sensores[2]["puerto_1"]
        i = 0
        while i <= 5:
            print(i)
            i += 1
            try:
                GPIO.setwarnings(False)
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(pin, GPIO.IN)
                x=GPIO.input(pin)
                if x is not None:
                    return x
            except RuntimeError as error:
                print("error")
            exit = 0
            if x is None:
                return exit
        GPIO.cleanup()


    def getHc_sr04(self):
        TRIG = self.sensores[1]["puerto_1"]
        ECHO = self.sensores[1]["puerto_2"]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        i = 0
        while i <= 5:
            print(i)
            i += 1
            try:
                GPIO.output(TRIG, True)
                time.sleep(0.00001)
                GPIO.output(TRIG, False)
                time.sleep(2)
                GPIO.output(TRIG, GPIO.LOW)
                pulso_inicio = time.time()
                pulso_fin = time.time()
                while GPIO.input(ECHO) == 0:
                    pulso_inicio = time.time()
                while GPIO.input(ECHO) == 1:
                    pulso_fin = time.time()
                duracion = pulso_fin - pulso_inicio
                distancia = (34300 * duracion) / 2
                if distancia is not None:
                    return distancia
                exit = 0
            except RuntimeError as error:
                print("error")
        if distancia is None:
            return exit
        GPIO.cleanup()

    def getDth11(self):
        pin = self.sensores[0]["puerto_1"]
        i = 0
        arreglo = [ None, None]
        while i <= 5:
            print(i)
            i += 1
            try:
                humidity, temperature = adafruit_dht.read(11, pin)
                if humidity is not None or temperature is not None:
                    arreglo = [humidity, temperature]
                    return arreglo
            except RuntimeError as error:
                print("error")
        exit = 0
        if humidity is None or temperature is None:
            return exit
            
    def getValores(self):
        data = self.getTemp_Hum()
<<<<<<< HEAD
        sensores = s.serialize.leerArchivo("sensores")
=======
        sensores = []
>>>>>>> e34cf2b5a85f4010696ea98c08b1c18514a3feb5
        sPIR = self.getDistanciapir()
        ultrasonico = self.getDistancia()
        if data:
            for x in data:
                sensores.append(x)
        sensores.append(sPIR)
        sensores.append(ultrasonico)
<<<<<<< HEAD
        s.serialize.guardarEnArchivo("sensores",sensores)
=======
>>>>>>> e34cf2b5a85f4010696ea98c08b1c18514a3feb5
        return sensores