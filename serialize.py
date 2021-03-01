import pickle as pi
from os import path
class serialize(object):

    @staticmethod
    def guardarEnArchivo(titulo,objetos):
        archivo=open(titulo,"wb")
        pi.dump(objetos,archivo)
        archivo.close()

    @staticmethod
    def leerArchivo(titulo):
        objetos=[]
        if path.exists(titulo):
            archivo=open(titulo,"rb")
            objetos=pi.load(archivo)
            archivo.close()
        return objetos