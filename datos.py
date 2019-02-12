import random as r

#Clase para generar datos ficticios con ciertos valores combinandolos y utilizando la clase random
# @Alejandro

class Datos:

    '''
    id = [1,2,3,4,5,6,7]
    nombres = ["Carro", "Reloj", "Llaves", "Billetera", "Celular", "Vaso de vidrio", "Chocolatina"]
    descripcion = ["Muy Mala","Mala","Regular","Buena","Muy buena"]

    @staticmethod
    def generarArticulos():
        while (len(Datos.id)!=0) and (len(Datos.nombres)!=0):
            #Toma los valores de la lista aleatoriamente
            id = r.choice(Datos.id)
            nombre = r.choice(Datos.nombres)
            #entero de 0 a el valor que le ponga
            precio = r.randrange(30000)
            Datos.id.remove(id)
            Datos.nombres.remove(nombre)
            Articulo(id, nombre, precio)

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