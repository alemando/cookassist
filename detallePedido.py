class Detalle_pedido():
    
    _list_detalle_pedido = []
    _codigo_d_p = 0

    def __init__(self,cantidad,receta,producto):
        """Atributos:
        self.codigo
        self.cantidad
        self.pedido
        self.receta
        self.producto
        """
        self.set_codigo(Detalle_pedido._codigo_d_p)
        self.set_cantidad(cantidad)
        self.set_receta(receta) 
        self.set_producto(producto)
        Detalle_pedido._list_detalle_pedido.append(self)
        Detalle_pedido._codigo_d_p += 1

    def set_codigo(self,codigo):
        self._codigo = codigo

    def get_codigo(self):
        return self._codigo

    def set_cantidad(self,cantidad):
        self._cantidad = cantidad

    def get_cantidad(self):
        return self._cantidad

    def set_pedido(self,pedido):
        self._pedido = pedido

    def get_pedido(self):
        return self._pedido

    def set_receta(self,receta):
        self._receta = receta

    def get_receta(self):
        return self._receta

    def set_producto(self,producto):
        self._producto = producto

    def get_producto(self):
        return self._producto

    def delete_detalle_pedido(self):
        self.set_cantidad(None)
        self.set_pedido(None)
        self.set_receta(None) 
        self.set_producto(None)



