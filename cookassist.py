import os

from mensajes import Mensajes
#from datos import Datos
#from usuario import Usuario
#from calificacion import Calificacion
<<<<<<< HEAD
from receta import Receta
=======
from Receta import Receta
>>>>>>> a1668c2b5ff36f28fbf3573d31c8e453420b36c6
from producto import Producto


class CookAssist:

    def __init__(self):
        pass

    @staticmethod
    def menu(opcion):
        menu = {
            '1': CookAssist.menu_usuario,
            '2': CookAssist.menu_chef,
            '3': CookAssist.menu_calificacion,
            '4': CookAssist.menu_datos,
            '5': CookAssist.menu_idioma,
            '6': CookAssist.menu_receta,
            '7': CookAssist.menu_producto,
            '8': CookAssist.salir
        }
        return menu.get(opcion)

    @staticmethod
    def menu_usuario(opcion):
        menu_usuario = {
            '1': CookAssist.ver_usuario,
            '2': CookAssist.crear_usuario,
            '3': CookAssist.editar_usuario,
            '4': CookAssist.eliminar_usuario
        }
        return menu_usuario.get(opcion)

    @staticmethod
    def menu_chef(opcion):
        menu_chef = {
            '1': CookAssist.ver_chef,
            '2': CookAssist.agregar_chef,
            '3': CookAssist.editar_chef,
            '4': CookAssist.eliminar_chef
        }
        return menu_chef.get(opcion)

    @staticmethod
    def menu_calificacion(opcion):
        menu_calificacion = {
            '1': CookAssist.ver_calificacion,
            '2': CookAssist.agregar_calificacion,
            '3': CookAssist.editar_calificacion,
            '4': CookAssist.eliminar_calificacion
        }
        return menu_calificacion.get(opcion)

    @staticmethod
    def menu_datos(opcion):
        menu_datos = {
            '1': CookAssist.agregar_datos_ficticios
        }
        return menu_datos.get(opcion)

    @staticmethod
    def menu_idioma(opcion):
        menu_idioma = {
            '1': CookAssist.cambiar_idioma
        }
        return menu_idioma.get(opcion)

    @staticmethod
    def menu_receta(opcion):
        menu_calificacion = {
            '1': CookAssist.ver_receta,
            '2': CookAssist.agregar_receta,
            '3': CookAssist.editar_receta,
            '4': CookAssist.eliminar_receta,
            '5': CookAssist.editar_calificacion,
            '6': CookAssist.eliminar_calificacion
        }
        return menu_calificacion.get(opcion)

    '''if imprimir is True print a string
        if not return a string
    '''
    @staticmethod
    def mensaje(opcion, imprimir=True):
        if imprimir:
            print(Mensajes.men.get(opcion))
        else:
            return Mensajes.men.get(opcion)
        

    @staticmethod
<<<<<<< HEAD
    def cambiar_idioma(opcion):
=======
    def cambiar_idioma():
>>>>>>> a1668c2b5ff36f28fbf3573d31c8e453420b36c6
        opcion = input(Mensajes.texto_idioma)
        if opcion == '1':
            Mensajes.men = Mensajes.español
        elif opcion == '2':
            Mensajes.men = Mensajes.ingles
        else:
            print(CookAssist.mensaje('opcionNoValida', False).format(opcion))

    @staticmethod
    def salir():
        CookAssist.mensaje('salir')
        os._exit(0)

    @staticmethod
    def ver_usuario():
        pass
        '''
        id = int(input(CookAssist.mensaje('id', False)))
        user = Usuario.get_usuario_by_identificacion(id)
        if user is not None:
            print(user.toString())
            return user
        else:
            CookAssist.mensaje('userNotFound')
            return None
            '''


    @staticmethod
    def crear_usuario():
        pass
        '''
        #TODO: Tipo usuario
        user_type = 'cliente'
        nombre = input(CookAssist.mensaje('nombre', False))
        id = int(input(CookAssist.mensaje('id', False)))
        while not Usuario.verificar_identificacion(id):
            CookAssist.mensaje('idFound', False)
            id = input(CookAssist.mensaje('id', False))
        fecha_nac = input(CookAssist.mensaje('fecha_nac', False))
        contrasena = input(CookAssist.mensaje('contrasena', False))
        Usuario(user_type, nombre, id, fecha_nac, contrasena)
        '''

    @staticmethod
    def editar_usuario():
        pass
        '''
        #TODO: Cambiar tipo usuario
        user = CookAssist.ver_usuario()
        CookAssist.mensaje('editar_usuario')
        opcion = input(CookAssist.mensaje('opcion', False))
        while opcion is not '4':
            if opcion is '1':
                nombre = input(CookAssist.mensaje('nombre', False))
                user.set_nombre(nombre)
            elif opcion is '2':
                fecha_nac = input(CookAssist.mensaje('fecha_nac', False))
                user.set_fecha_nacimiento(fecha_nac)
            elif opcion is '3':
                vieja_contrasena = input(CookAssist.mensaje('oldContrasena', False))
                nueva_contrasena =  input(CookAssist.mensaje('newContrasena', False))
                if vieja_contrasena == user.get_contrasena():
                    user.set_contrasena = nueva_contrasena
                else:
                    CookAssist.mensaje('wrongContrasena')
            CookAssist.mensaje('editar_usuario')
            opcion = input(CookAssist.mensaje('opcion', False))
        '''
                    
    @staticmethod
    def eliminar_usuario():
        pass
        '''
        id = int(input(CookAssist.mensaje('id', False)))
        pos = Usuario.get_posicion_lista(id)
        opcion = input(CookAssist.mensaje('yesNo', False))
        if opcion == '1':
            Usuario.delete_element(pos)
        '''
    
    #TODO: CHEF METODOS
    @staticmethod
    def ver_chef():
        pass

    @staticmethod
    def agregar_chef():
        pass

    @staticmethod
    def editar_chef():
        pass

    @staticmethod
    def eliminar_chef():
        pass

    @staticmethod
    def ver_calificacion():
        pass

    @staticmethod
    def agregar_calificacion():
        pass

    @staticmethod
    def editar_calificacion():
        pass

    @staticmethod
    def eliminar_calificacion():
        pass

    @staticmethod
    def agregar_datos_ficticios():
        pass


    @staticmethod
    def ver_receta():
        
        CookAssist.mensaje('opcionesVerReceta')
        opcion = input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            codigo = input(CookAssist.mensaje('codigo',False))
            receta= Receta.get_receta_by_codigo(codigo)
            return receta                                   
            if producto is not None:
                print(Receta.toString())
                return receta
<<<<<<< HEAD
            else: 
=======
            else 
>>>>>>> a1668c2b5ff36f28fbf3573d31c8e453420b36c6
                CookAssist.mensaje('CodeNotFound')
                return none
            
            
        

    @staticmethod
    def agregar_receta():
       
        nombre = input(CookAssist.mensaje('nombre', False))
        tiempo_preparacion = int(input(CookAssist.mensaje('tiempo', False)))
        receta = Receta(nombre, tiempo_preparacion)
        CookAssist.mensaje('opcionesDetalleReceta')
        opcion = input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            producto = input(CookAssist.mensaje('producto', False))
            cantidad = input(CookAssist.mensaje('cantidad', False))
            DetalleReceta(producto, cantidad)
            
            
    @staticmethod
    def editar_receta():
<<<<<<< HEAD
        receta = CookAssist.ver_receta()
=======
        receta = CookAssist.ver_receta():
>>>>>>> a1668c2b5ff36f28fbf3573d31c8e453420b36c6
        CookAssist.mensaje('editar_receta')
        opcion = input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            nombre = input(CookAssist.mensaje('nombre', False))
            Receta.set_nombre(nombre)
<<<<<<< HEAD
        elif opcion == '2':
            tiempo = input(CookAssist.mensaje('tiempo_preparacion', False))
            Receta.set_tiempo_preparacion(tiempo)
        elif opcion == '3':
            CookAssist.mensaje('editar_DetalleReceta')
            opcionReceta = input(CookAssist.mensaje('opcion', False))
            if opcionReceta =='1':
=======
       elif opcion == '2':
            tiempo = input(CookAssist.mensaje('tiempo_preparacion', False))
            Receta.set_tiempo_preparacion(tiempo)
       elif opcion == '3':
            CookAssist.mensaje('editar_DetalleReceta')
            opcion = input(CookAssist.mensaje('opcion', False)
            if opcion =='1':
>>>>>>> a1668c2b5ff36f28fbf3573d31c8e453420b36c6
                codigo = input(CookAssist.mensaje('codigo', False))
                producto = get_producto_by_codigo(codigo)           
                cantidad = input(CookAssist.mensaje('cantidad', False))
                DetalleReceta.set_cantidad(cantidad) 
                # se supone quedo saber que a que produto le estoy cambiando la cantidad           
<<<<<<< HEAD
            elif opcionReceta == '2':
                pass

=======
            if opcion == '2':
                pass           
                           
                           
            
>>>>>>> a1668c2b5ff36f28fbf3573d31c8e453420b36c6
    @staticmethod
    def eliminar_receta():
        codigo = input(CookAssist.mensaje('codigo', False))
        pop = Receta.get_posicion_lista(codigo)
        opcion = input(CookAssist.mensaje('yesNo', False))
        if opcion == '1':
            Receta.delete_element(pop)                                        
        
                                               
                                               
                                               
                                               
    @staticmethod
<<<<<<< HEAD
    def menu_producto(opcion):
=======
    def menu_producto():
>>>>>>> a1668c2b5ff36f28fbf3573d31c8e453420b36c6
        menu_producto = {
            '1': CookAssist.ver_producto,
            '2': CookAssist.agregar_producto,
            '3': CookAssist.editar_producto
        }
        return menu_producto.get(opcion)
    
<<<<<<< HEAD
    @staticmethod
=======
     @staticmethod
>>>>>>> a1668c2b5ff36f28fbf3573d31c8e453420b36c6
    def ver_producto():
        CookAssist.mensaje('ver_producto')
        opcion = input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            codigo = input(CookAssist.mensaje('codigo', False))
            producto = Producto.get_producto_by_codigo(codigo)
            if producto is not None:
                print(producto.toString())
                return producto
            else:
                CookAssist.mensaje('codeNotFound')
                return None
            
        elif opcion == '2':
            nombre1 = input(CookAssist.mensaje('nombre', False))
            producto = Producto.get_producto_ny_nombre(nombre1)
            if producto is not None:
                print(producto.toString())
                return producto
            else:
                CookAssist.mensaje('codeNotFound')
                return None
<<<<<<< HEAD

            
=======
                           
>>>>>>> a1668c2b5ff36f28fbf3573d31c8e453420b36c6

    @staticmethod
    def agregar_producto():
        pass

    @staticmethod
    def editar_producto():
        pass

    @staticmethod
    def run():

        Mensajes.men = Mensajes.español

        while True:
            CookAssist.mensaje('menu')
            opcion_principal = input(CookAssist.mensaje('opcion', False))
            print('')
            action_principal = CookAssist.menu(opcion_principal)
            if action_principal:
                ejecutar = True

                action_string = str(action_principal)
                action_slice_start = action_string.find('.') + 1
                action_slice_last = action_string.index(' ', action_slice_start)
                action = action_string[action_slice_start:action_slice_last]
                print (action)
                if action == 'salir':
                    action_principal()

                while ejecutar:
                    
                    CookAssist.mensaje(action)
                    opcion_menu = input(CookAssist.mensaje('opcion', False))
                    print('')
                    action_menu = action_principal(opcion_menu)
                    if action_menu:
                        action_menu()
                    else:
                        ejecutar = False
                    
                    
            else:
                print(CookAssist.mensaje('opcionNoValida', False).format(opcion))
            

if __name__ == '__main__':
    
    CookAssist.run()
