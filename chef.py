from usuario import Usuario

class Chef(Usuario):

    ListChefs = []

    def __init__(
            self, tipo_usuario, nombre, identificacion, fecha_nacimiento, 
            contrasena):
        super().__init__(tipo_usuario, nombre, identificacion, fecha_nacimiento, 
            contrasena)
        self._ListCalificacionesChef = []
        self._ListPedidosChef = []
        Usuario.ListChefs.append(self)

    def set_calificaciones_chef(self, calificacion):
        self._ListCalificacionesChef.append(calificacion)

    def get_calificaciones_chef(self):
        return self._ListCalificacionesChef

    def set_pedidos_chef(self, pedido):
        self._ListPedidosChef.append(pedido)

    def get_pedidos_chef(self):
        return self._ListPedidosChef