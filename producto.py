from mensajes import Mensajes

class Producto:

    ListProductos = {}
    auto_increment_codigo = 0
    

    def __init__(
            self, nombre, cantidad,
            medicion, estado):
        '''ATTRIBUTES
            self._id
            self._nombre
            self._cantidad
            self._medicion
            self._necesario
            self._estado
        '''
        self._ListDetallePedidos = []
        self._ListDetalleRecetas = []
        self.set_codigo()
        self.set_nombre(nombre)
        self.set_cantidad(cantidad)
        self.set_medicion(medicion)
        self.set_estado(estado)
        Producto.ListProductos[self.get_codigo()] = self
        archivo = open('producto_data.txt', 'a+')
        my_producto ='\n'+ self.get_nombre()+','+str(self.get_cantidad())+','+self.get_medicion()+','+str(self.get_estado())
        escribir = True
        archivo.seek(0)
        for item in archivo.readlines():
            if item.strip() == my_producto.strip():
                escribir = False
        
        if escribir:
            archivo.write(my_producto)
        archivo.close()

    def set_codigo(self):
        Producto.auto_increment_codigo +=1
        self._codigo = str(Producto.auto_increment_codigo)

    def get_codigo(self):
        return self._codigo

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def get_cantidad(self):
        return self._cantidad

    def set_medicion(self, medicion):
        self._medicion = medicion

    def get_medicion(self):
        return self._medicion

    def set_estado(self, estado):
        self._estado = estado

    def get_estado(self):
        return self._estado

    def set_detalle_pedidos(self, detalle_pedido):
        self._ListDetallePedidos.append(detalle_pedido)

    def get_detalle_pedidos(self):
        return self._ListDetallePedidos

    def set_detalle_recetas(self, receta):
        self._ListDetalleRecetas.append(receta)

    def get_detalle_recetas(self):
        return self._ListDetalleRecetas
    
    def cambiar_cantidad(self, cantidad):
        suma= (self.get_cantidad())+(cantidad)
        self.set_cantidad(suma)

    def actualizar_en_txt(self):
        archivo = open('producto_data.txt', 'r')
        my_archivo = archivo.readlines()
        my_producto_name = self.get_nombre()
        my_producto ='\n'+ self.get_nombre()+','+str(self.get_cantidad())+','+self.get_medicion()+','+str(self.get_estado())
        print(my_producto)
        for x in range(len(my_archivo)):
            if my_archivo[x].strip().find(my_producto_name) != -1:
                my_archivo[x] = my_producto
        
        print(my_archivo)
        archivo = open('producto_data.txt', 'w+')
        archivo.writelines(my_archivo)
        archivo.close()

    def __str__(self):
        Str = Mensajes.men.get('formatoProducto') % (
            self.get_codigo(), self.get_nombre(),
            self.get_cantidad(), self.get_medicion(), self.get_estado())
        return Str


##    @staticmethod
##    def desactivar_producto(codigo):
##        pro = Producto.ListProductos.get(codigo)
##        if pro.get_estado() ==  True:
##            pro.set_estado(False)
##        else:
##            pass
              

    @staticmethod
    def get_producto_by_codigo(codigo):
        pro = Producto.ListProductos.get(codigo)
        return pro
    
    
    @staticmethod
    def get_producto_by_nombre(nombre1):
        listaCoincidencias= []
        for producto in Producto.ListProductos.values():
            if producto.get_nombre().lower().find(nombre1.lower())!= -1:
                listaCoincidencias.append(producto)
        return listaCoincidencias

    @staticmethod
    def lista_de_compras():
        lista_compras=[]
        for i in Producto.ListProductos.values():
            if int(i.get_cantidad()) < 5:
                lista_compras.append(i)
        return lista_compras 
    
    @staticmethod
    def productos_disponibles():
        lista_disponibles = []
        for i in Producto.ListProductos.values():
            if i.get_estado() and i.get_cantidad() !=0:
                lista_disponibles.append(i)
            else:
                pass
        return lista_disponibles