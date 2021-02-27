import Adafruit_DHT as adafruit_dht
import  RPi.GPIO as GPIO
import time

class Sensores():
    def __init__(self):
        self.ultrasonico = 0
        self.temperatura = 0
        self.humedad = 0
        self.pir = 0
        self.arreglo = [
            {"id":1, "valor":1, "nombre", "temp", "tipo": "flotante", "puerto":12},
            {"id":1, "valor":1, "nombre", "temp", "tipo": "flotante", "puerto":12},
        ] #ejemplo del profe

        for x as self.arreglo:
            d = "insert into valores (sensor_id, x.tipo) values (x.valor, x.id)"
            #ejemplo del profe
    
    def getDistanciapir(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(21, GPIO.IN)         #Read output from PIR motion sensor
        #GPIO.setup(3, GPIO.OUT)         #LED output pin
        i=GPIO.input(21)
        #GPIO.output(3, 1)  #Turn ON LED
        GPIO.cleanup()
        return (i)

    def getDistancia(self):
        sensorultra = Sensores() 
        TRIG = 23
        ECHO = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
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
            sensorultra.ultrasonico = distancia
            GPIO.cleanup()
            """if GPIO.input(ECHO) == GPIO.HIGH:
                pulso_fin = time.time()
                if GPIO.input(ECHO) == GPIO.LOW:
                    duracion = pulso_fin - pulso_inicio
                    distancia = (34300 * duracion) / 2
                    sensorultra.ultrasonico = distancia
                    """
            #print ("Distancia: %.2f cm" % distancia) 
            return(sensorultra.ultrasonico)
        except RuntimeError as error:
            print("error")

    def getTemp_Hum(self):
        sensortemyhum = Sensores()
        pin = 4
        i = 0
        arreglo = [ None, None]
        while i <= 5:
            print(i)
            i += 1
            try:
                humidity, temperature = adafruit_dht.read(11, pin)
                if humidity is not None and temperature is not None:
                    arreglo = [humidity, temperature]
                    return arreglo
            except RuntimeError as error:
                print("error")
            
    def getValores(self):
        valores = Sensores()
        datos = valores.getTemp_Hum()
        sensores = []
        sPIR = valores.getDistanciapir()
        ultrasonico = valores.getDistancia()
        if datos:
            for x in datos:
                sensores.append(x)
        sensores.append(sPIR)
        sensores.append(ultrasonico)
        return sensores
