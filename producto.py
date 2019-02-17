from mensajes import Mensajes

class Producto:

    ListProductos = []
    auto_increment_codigo = 0
    

    def __init__(
            self, nombre, categoria, cantidad,
            medicion, necesario, estado):
        '''ATTRIBUTES
            self._id
            self._nombre
            self._cantidad
            self._categoria
            self._medicion
            self._necesario
            self._estado
        '''
        self._ListDetallePedidos = []
        self._ListDetalleRecetas = []
        self.set_codigo()
        self.set_nombre(nombre)
        self.set_categoria(categoria)
        self.set_cantidad(cantidad)
        self.set_medicion(medicion)
        self.set_necesario(necesario)
        self.set_estado(estado)
        Producto.ListProductos.append(self)

    def set_codigo(self, auto_increment_codigo):
        Producto.auto_increment_codigo +=1
        self._codigo = str(Producto.auto_increment_codigo)

    def get_codigo(self):
        return self._codigo

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_categoria(self):
        return self._categoria

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

    def get_estdo(self):
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
            self.get_codigo(), self.get_nombre(), self.get_categoria(),
            self.get_cantidad(), self.get_medicion(), self.get_necesario())
        return Str

    @staticmethod
    def get_producto_by_codigo(codigo):
        for producto in Producto.ListProductos:
            if producto.get_codigo() == codigo:
                return producto.toString()
        return None
    
    
    @staticmethod
    def get_producto_by_nombre(nombre1):
        for producto in Producto.ListProductos:
            if producto.get_nombre() == nombre1:
                return producto.toString()
        return None
    
    
    @staticmethod
    def get_posicion_lista(codigo):
        for i in range(0,len(Producto.ListProductos)):
            if Producto.ListProductos[i].get_codigo() == codigo:
                return i
                break
        return -1

    @staticmethod
    def delete_element(codigo):
        pos = get_posicion_lista(codigo)
        Producto.ListProductos.pop(pos)
        