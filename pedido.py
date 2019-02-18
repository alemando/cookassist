from datetime import datetime

class Pedido():

    _num_pedidos = 0 # Pedidos totales 
    _num_pedidos_eliminados = 0
    _list_pedidos = []

    def __init__ (self,descripcion,detalle,usuario,entregado = False):
        """Atributos:
        self._nombre
        self._fecha 
        self._descripcion 
        self._ListDetalle 
        self._usuario 
        self._chef 
        self._entregado (estado)
        """
        self._list_detalle = []
        self.set_codigo(Pedido._num_pedidos)
        self.set_fecha() # Recordatorio: El metodo set_fecha setea 
                              # fecha con cualquier parametro
        self.set_estado(entregado)
        self.set_detalle(detalle)
        self.set_descripcion(descripcion)
        self.set_usuario(usuario)

        Pedido._num_pedidos += 1
        Pedido._list_pedidos.append(self)

    def set_fecha(self):
            self._fecha = datetime.now()
            self._fecha = ("Fecha: "+str(self._fecha.day)+"-"+
                str(self._fecha.month)+"-"+str(self._fecha.year)+
                " Hora: "+str(self._fecha.hour)+":"+
                str(self._fecha.minute)+":"+str(self._fecha.second))

    def get_estado(self):
        return self._entregado

    def set_estado(self,entregado):
        self._entregado = entregado

    def get_fecha(self):
        return self._fecha

    def get_codigo(self):
        return self._codigo

    def set_codigo(self,codigo):
        self._codigo = codigo

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

    def delete_all_values(self):
        self.set_codigo(None)
        self.set_fecha(None)
        self.set_descripcion(None)
        self.set_detalle(None)
        self.set_usuario(None)
        self.set_chef(None)

    # Funcionalidades adicionales:   

    # Numero de pedidos totales
    def get_num_pedidos(self):
        return self._num_pedidos


    # Vaciar Todos los pedidos
    def del_tot_pedidos(self):
        Pedido._list_pedidos.clear()

    # retorna Primer pedido no entregado de la lista
    @staticmethod
    def get_primer_pedido():
        if(len(Pedido._list_pedidos)>0):
            for ped in Pedido._list_pedidos:
                if ped.get_estado == False :
                    return ped
                    break
        return None

    # Modificar todo
    def modify_all_values(self,nombre,fecha,descripcion,
                        detalle,usuario,chef):
        self.set_codigo(nombre)
        self.set_fecha(fecha)
        self.set_descripcion(descripcion)
        self.set_detalle(detalle)
        self.set_usuario(usuario)
        self.set_chef(chef)
