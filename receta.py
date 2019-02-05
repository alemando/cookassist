

class Receta:

	ListRecetas = []
    auto_increment_codigo = 0

    def __init__(
        self, nombre, 
        tiempo_preparacion):
        '''ATTRIBUTES
            self._codigo
            self._nombre
            self._tiempo_preparacion
        '''
        auto_increment_codigo += 1
        self.set_codigo(str(auto_increment_codigo))
        self.set_nombre(nombre)
        self.set_tiempo_preparacion(tiempo_preparacion)
        self._ListDetalleRecetas = []
        self._ListDetallePedidos = []
        self._ListCalificaciones = []

    def set_codigo(self, codigo):
        self._codigo = codigo

    def get_codigo(self):
        return self._codigo

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_tiempo_preparacion(self, tiempo_preparacion):
        self._tiempo_preparacion = tiempo_preparacion

    def get_tiempo_preparacion(self):
        return self._tiempo_preparacion

    def set_detalle_recetas(self, detalle_recetas):
        self._ListDetalleRecetas.append(detalle_recetas)

    def get_detalle_recetas(self):
        return self._ListDetalleRecetas

    def set_detalle_pedidos(self, detalle_pedido):
        self._ListDetallePedidos.append(detalle_pedido)

    def get_detalle_pedidos(self):
        return self._ListDetallePedidos

    def set_calificaciones(self, calificacion):
        self._ListCalificaciones.append(calificacion)

    def get_calificaciones(self):
        return self._ListCalificaciones

    def toString(self):
        Str = Mensajes.men.get('formatoReceta') % (
            self.get_codigo(), self.get_nombre(),
            self.get_tiempo_preparacion())
        #concatenado el detalle receta
        return Str

    @staticmethod
    def get_receta_by_codigo(codigo):
        for receta in Receta.ListRecetas:
            if receta.get_codigo() == codigo:
                return receta
        return None

    @staticmethod
    def get_posicion_lista(codigo):
        for i in range(0,len(Receta.ListReceta)):
            if Receta.ListRecetas[i].get_codigo() == codigo:
                return i
                break
        return -1

    @staticmethod
    def delete_element(posicion):
        Receta.ListRecetas.pop(posicion)
