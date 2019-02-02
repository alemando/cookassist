from datetime import datetime

class Pedido():

    _num_pedidos = 0
    _tot_pedidos = {}

    def __init__ (self,fecha,descripcion,detalle,usuario,chef):
        """Atributos:
        self._fecha 
        self._descripcion 
        self._ListDetalle 
        self._usuario 
        self._chef """
        self._ListDetalle = []
        self.setFecha(fecha) #Recordatorio: El metodo setFecha setea fecha con cualquier parametro, 
                             #se pone en la pestaña main
        self.setDescripcion(descripcion)
        self.setDetalle(detalle)
        self.setUsuario(usuario)
        self.setChef(chef)
        
        Pedido._num_pedidos += 1
        Pedido._tot_pedidos[self.getFecha()] = self.getUsuario()

    def setFecha(self,fecha):
        self._fecha = datetime.now()
        self._fecha = ("Fecha: "+str(self._fecha.day)+"-"+str(self._fecha.month)+"-"+str(self._fecha.year)+
            " Hora: "+str(self._fecha.hour)+":"+str(self._fecha.minute)+":"+str(self._fecha.second))

    def getFecha(self):
        return self._fecha

    def setDescripcion(self,descripcion):
        self._descripcion = descripcion

    def getDescripcion(self):
        return self._descripcion

    def setDetalle(self,detalle):
        self._ListDetalle.append(detalle)

    def getDetalle(self):
        return self._ListeDetalle

    def setUsuario(self,usuario):
        self._usuario = usuario

    def getUsuario(self):
        return self._usuario

    def setChef(self,chef):
        self._chef = chef

    def getChef(self):
        return self._chef

    def modifyAllValues(self,fecha,descripcion,detalle,usuario,chef):
        self.setFecha(fecha)
        self.setDescripcion(descripcion)
        self.setDetalle(detalle)
        self.setUsuario(usuario)
        self.setChef(chef)

    # Funcionalidades:   

    # Numero de pedidos totales
    def getNum_pedidos(self):
        return self._num_pedidos

    # Pedidos totales del dia
    def getTot_pedidos(self):
        return self._tot_pedidos

    # Obetener usuario por fecha de pedido
    # siendo 'key' una fecha
    def getUsuario_fecha(self,key):  
        return self._tot_pedidos.get(key) 
