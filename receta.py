
class Receta:

    ListRecetas = []
    auto_increment_codigo = 0

    def __init__(
        self, nombre, 
        tiempo_preparacion, estado, DetalleReceta):
        '''ATTRIBUTES
            self._codigo
            self._nombre
            self._tiempo_preparacion
            self._disponibilidad
        '''
        Receta.auto_increment_codigo += 1
        self.set_codigo(str(Receta.auto_increment_codigo))
        self.set_nombre(nombre)
        self.set_tiempo_preparacion(str(tiempo_preparacion))
        self.set_estado(estado)
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

    def get_estado(self):
        return self._estado

    def set_estado(self, estadoInput):
        if (estadoInput == 1):
            self._estado = True        
        else:
            self._estado = False        

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
        Str =('codigo: '+self.get_codigo() +' nombre: '+ self.get_nombre()
            +' tiempo_de_preparacion: '+self.get_tiempo_preparacion())
        #concatenado el detalle receta
        return Str

    @staticmethod
    def get_receta_by_codigo(codigo):
        for i in range(0,len(Receta.ListRecetas)):
            if Receta.ListRecetas[i].get_codigo() == codigo:
                return Receta.ListRecetas[i]
        return None
        
    @staticmethod
    def get_posicion_lista(codigo):
        for i in range(0,len(Receta.ListRecetas)):
            if Receta.ListRecetas[i].get_codigo() == codigo:
                return i
                break
        return -1
