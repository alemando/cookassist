from mensajes import Mensajes

class Producto:

    ListProductos = {}
    auto_increment_codigo = 0
    

    def __init__(
            self, nombre, cantidad,
            medicion, necesario, estado):
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
        self.set_necesario(necesario)
        self.set_estado(estado)
        Producto.ListProductos[self.get_codigo()] = self

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

    def set_necesario(self, necesario):
        self._necesario = necesario

    def get_necesario(self):
        return self._necesario

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
    
    def agregar_cantidad(self, cantidad):
        suma= (self.get_cantidad())+cantidad
        self.set_cantidad(suma)

    def toString(self):
        Str = Mensajes.men.get('formatoProducto') % (
            self.get_codigo(), self.get_nombre(),
            self.get_cantidad(), self.get_medicion(), self.get_necesario())
        return Str


    @staticmethod
    def desactivar_producto(codigo):
        pro = Producto.ListProductos.get(codigo)
        if pro.get_estado() ==  True:
            pro.set_estado(False)
        else:
            pass
              

    @staticmethod
    def get_producto_by_codigo(codigo):
        pro = Producto.ListProductos.get(codigo)
        return pro.toString()
    
    
    @staticmethod
    def get_producto_by_nombre(nombre1):
        listaCoincidencias= []
        for producto in Producto.ListProductos.values():
            if producto.get_nombre().lower().find(nombre1.lower())!= -1:
                listaCoincidencias.append(producto)
        return listaCoincidencias
        
        