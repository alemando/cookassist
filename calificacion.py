from receta import Receta
from chef import Chef
from mensajes import Mensajes

class Calificacion:
    
    ListCalificaciones = {}

    def __init__(
            self, usuario, puntaje, 
            descripcion, para):
        '''ATTRIBUTES
            self._usuario
            self._puntaje
            self._descripcion
            self._receta
            self._chef
        '''
        self.set_usuario(usuario)
        self.set_puntaje(puntaje)
        self.set_descripcion(descripcion)
        self._set_para(para)
        #Calificacion.ListCalificaciones[self.get_codigo()] = self

    def set_usuario(
            self, usuario):
        self._usuario = usuario

    def get_usuario(self):
        return self._usuario

    def set_puntaje(
            self, puntaje):
        self._puntaje = puntaje

    def get_puntaje(self):
        return self._puntaje

    def set_descripcion(
            self, descripcion):
        self._descripcion = descripcion

    def get_descripcion(self):
        return self._descripcion

    def set_receta(
            self, receta):
        self._receta = receta
        receta.set_calificaciones(self)

    def get_receta(self):
        return self._receta

    def set_chef(
            self, chef):
        self._chef = chef
        chef.set_calificaciones(self)

    def get_chef(self):
        return self._chef

    def _set_para(para):
        if para.isInstance(Receta):
            self.set_receta(para)
            
        else:
            self.set_chef(para)
            