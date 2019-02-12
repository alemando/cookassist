from mensajes import Mensajes


class Usuario:

    ListUsuarios = []

    def __init__(
            self, tipo_usuario, nombre, identificacion, 
            fecha_nacimiento, contrasena):
        '''ATTRIBUTES
            self._tipo_usuario
            self._nombre
            self._identificacion
            self._fecha_nacimiento
            self._contrasena
        '''
        self._ListCalificaciones = []
        self._ListPedidos = []
        self.set_tipo_usuario(tipo_usuario)
        self.set_nombre(nombre)
        self.set_identificacion(identificacion)
        self.set_fecha_nacimiento(fecha_nacimiento)
        self.set_contrasena(contrasena)
        Usuario.ListUsuarios.append(self)

    def set_tipo_usuario(self, tipo_usuario):
        self._tipo_usuario = tipo_usuario

    def get_tipo_usuario(self):
        return self._tipo_usuario

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_identificacion(self, identificacion):
        self._identificacion = identificacion

    def get_identificacion(self):
        return self._identificacion

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento

    def set_contrasena(self, contrasena):
        self._contrasena = contrasena

    def get_contrasena(self):
        return self._contrasena

    def set_calificaciones(self, calificacion):
        self._ListCalificaciones.append(calificacion)

    def get_calificaciones(self):
        return self._ListCalificaciones

    def set_pedidos(self, pedido):
        self._ListPedidos.append(pedido)

    def get_pedidos(self):
        return self._ListPedidos

    def toString(self):
        Str = Mensajes.men.get('formatoUsuario') % (
                self.get_tipo_usuario(), self.get_nombre(), 
                self.get_identificacion(), self.get_fecha_nacimiento())
        return Str

    @staticmethod
    def get_usuario_by_identificacion(identificacion):
        for user in Usuario.ListUsuarios:
            if user.get_identificacion() == identificacion:
                return user
        return None

    @staticmethod
    def verificar_identificacion(identificacion):
        for user in Usuario.ListUsuarios:
            if user.get_identificacion() == identificacion:
                return False
        return True

    @staticmethod
    def get_posicion_lista(identificacion):
        for i in range(0,len(Usuario.ListUsuarios)):
            if Usuario.ListUsuarios[i].get_identificacion() == identificacion:
                return i
                break
        return -1

    @staticmethod
    def delete_element(posicion):
        Usuario.ListUsuarios.pop(posicion)

