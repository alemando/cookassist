import random as r
from producto import Producto

#Clase para generar datos ficticios con ciertos valores combinandolos y utilizando la clase random
# @Alejandro

class Datos:
    @staticmethod
    def generarProductos():
        archivo = open('producto_data.txt','r')
        for nuevo in archivo.readlines():
            producto = nuevo.split(',')
            Producto(producto[0], int(producto[1]), producto[2], bool(producto[3]))
        archivo.close()
