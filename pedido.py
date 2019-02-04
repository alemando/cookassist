from datetime import datetime

class Pedido():

    _num_pedidos = 0
    _fechas_pedidos = []
    _nombres_pedidos = []
    _usuarios_pedidos = []

    def __init__ (self,nombre="Defecto",fecha="Defecto",descripcion="Defecto",
                detalle="Defecto",usuario="Defecto",chef="Defecto"):
        """Atributos:
        self._nombre
        self._fecha 
        self._descripcion 
        self._ListDetalle 
        self._usuario 
        self._chef """
        self._list_detalle = []
        self.set_nombre(nombre)
        self.set_fecha(fecha) # Recordatorio: El metodo setFecha setea 
                             # fecha con cualquier parametro
        self.set_descripcion(descripcion)
        self.set_detalle(detalle)
        self.set_usuario(usuario)
        self.set_chef(chef)

        Pedido._num_pedidos += 1
        Pedido._fechas_pedidos.append(self.get_fecha())
        Pedido._nombres_pedidos.append(self.get_nombre())
        Pedido._usuarios_pedidos.append(self.get_usuario())

    def set_fecha(self,fecha):
        self._fecha = datetime.now()
        self._fecha = ("Fecha: "+str(self._fecha.day)+"-"+
            str(self._fecha.month)+"-"+str(self._fecha.year)+
            " Hora: "+str(self._fecha.hour)+":"+
            str(self._fecha.minute)+":"+str(self._fecha.second))

    def get_fecha(self):
        return self._fecha

    def get_nombre(self):
        return self._nombre

    def set_nombre(self,nombre):
        self._nombre = nombre

    def set_descripcion(self,descripcion):
        self._descripcion = descripcion

    def get_descripcion(self):
        return self._descripcion

    def set_detalle(self,detalle):
        self._list_detalle.append(detalle)

    def get_detalle(self):
        return self._list_detalle

    def set_usuario(self,usuario):
        self._usuario = usuario

    def get_usuario(self):
        return self._usuario

    def set_chef(self,chef):
        self._chef = chef

    def get_chef(self):
        return self._chef

    def modify_all_values(self,nombre,fecha,descripcion,
                        detalle,usuario,chef):
        self.set_nombre(nombre)
        self.set_fecha(fecha)
        self.set_descripcion(descripcion)
        self.set_detalle(detalle)
        self.set_usuario(usuario)
        self.set_chef(chef)

    # Funcionalidades:   

    # Numero de pedidos totales
    def get_num_pedidos(self):
        return self._num_pedidos

    # Pedidos totales del dia (fechas)
    def get_fechas_pedidos(self):
        for i in self._fechas_pedidos:
            return i
        return None

    # Pedidos totales del dia (usuarios)
    def get_usuarios_pedidos(self,key):  
        for i in self._usuarios_pedidos:
            return i
        return None

    # Pedidos totales del dia (nombres)
    def get_nombres_pedidos(self,key):  
        for i in self._nombres_pedidos:
            return i
        return None

    # Vaciar Todos los pedidos
    def del_tot_pedidos(self):
        self._fechas_pedidos.clear()
        self._nombres_pedidos.clear()
        self._usuarios_pedidos.clear()
        Pedido._num_pedidos = 0

    # Ultimo pedido 
    def get_ultimo_pedido(self):
        if(Pedido._num_pedidos>0):
            a = (str(self._nombres_pedidos[len(self._nombres_pedidos)-1])+" - "+
            str(self._usuarios_pedidos[len(self._usuarios_pedidos)-1])+" - "+
            str(self._fechas_pedidos[len(self._fechas_pedidos)-1]))
            return a
        return None
