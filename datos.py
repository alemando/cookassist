import random as r
from producto import Producto

#Clase para generar datos ficticios con ciertos valores combinandolos y utilizando la clase random
# @Alejandro

class Datos:
    @staticmethod
    def generarProductos():
        Producto('Huevos', 100, 'Unidades', True)
        Producto('Leche', 8, 'L', True)
        Producto('Papas', 25, 'KG', True)
        Producto('Sal', 6, 'KG', True)
        Producto('Azucar', 20, 'KG', True)
        Producto('Pastas', 20, 'Unidades', True)
        Producto('Tomate', 8, 'KG', True)
        Producto('Aceite', 15, 'L', True)
        Producto('Cebolla', 6, 'KG', True)
        Producto('Gaseosa 350ml', 30, 'Unidades', True)
        Producto('Gaseosa Mega', 14, 'Unidades', True)
        Producto('Papas paquete', 18, 'Unidades', True)
        Producto('Arroz', 16, 'KG', True)
        Producto('Huevos', 100, 'Unidades', True)
        Producto('Huevos', 100, 'Unidades', True)
        Producto('Huevos', 100, 'Unidades', True)
        Producto('Huevos', 100, 'Unidades', True)
        Producto('Huevos', 100, 'Unidades', True)
        Producto('Huevos', 100, 'Unidades', True)
        Producto('Huevos', 100, 'Unidades', True)
        Producto('Huevos', 100, 'Unidades', True)
        Producto('Huevos', 100, 'Unidades', True)


        pass
        #Usuario(True, 'CC', '1238938010', 'Alejandro Jiménez', '12345', '28/10/1999')
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