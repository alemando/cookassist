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
'''
    @staticmethod
    def generarComentarios(cant):
        #Cantidad de comentarios que quiero generar aleatoriamente
        while cant > 0:
            puntuacion = r.randint(1, 5)
            #Tomo los valores de la descripcion segun la puntuacion el -1 para ajustar el tamaño de la lista
            descripcion = Datos.descripcion[(puntuacion-1)]
            art = r.choice(Articulo.listaArticulos)
            Comentario(descripcion,puntuacion,art);
            cant = cant - 1
'''