import os

from mensajes import Mensajes
from datos import Datos
from usuario import Usuario
from chef import Chef
from calificacion import Calificacion
from receta import Receta
from producto import Producto
from pedido import Pedido
from detallePedido import Detalle_pedido
from detalleReceta import DetalleReceta

class CookAssist:

    #cambia si es chef o usuario
    user = None
    chef = False

    @staticmethod
    def enter():
        option = input(CookAssist.mensaje('enter', False))
        menu = {
            '1': CookAssist.login,
            '2': CookAssist.new_user,
            '3': CookAssist.close
        }
        menu.get(option)()
        
    @staticmethod
    def main():
        main_action = CookAssist.menu()
        print('')
        if main_action:
            ejecutar = True
            while ejecutar and (CookAssist.user is not None):
                action_menu = main_action()
                print('')
                if action_menu:
                    action_menu()
                else:
                    ejecutar = False
                
        else:
            CookAssist.sign_off()

    @staticmethod
    def menu():
        menu = {}
        option = None
        if CookAssist.chef:
            menu = {
                '1': CookAssist.menu_producto,
                '2': CookAssist.menu_receta,
                '3': CookAssist.menu_pedido,
                '4': CookAssist.menu_chef,
                '5': CookAssist.menu_usuario,
                '6': CookAssist.menu_language
            }
            option = input(CookAssist.mensaje('menu_main_chef', False))
        
        elif CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.menu_producto,
                '2': CookAssist.menu_receta,
                '3': CookAssist.menu_pedido,
                '4': CookAssist.menu_calificacion,
                '5': CookAssist.menu_chef,
                '6': CookAssist.menu_usuario,
                '7': CookAssist.menu_language,
                '8': CookAssist.menu_data
            }
            option = input(CookAssist.mensaje('menu_main_admin', False))
        else:
            menu = {
                '1': CookAssist.menu_producto,
                '2': CookAssist.menu_receta,
                '3': CookAssist.menu_pedido,
                '4': CookAssist.menu_calificacion,
                '5': CookAssist.menu_chef,
                '6': CookAssist.menu_usuario,
                '7': CookAssist.menu_language
                
            }
            option = input(CookAssist.mensaje('menu_main_user', False))
        
        return menu.get(option)


    @staticmethod
    def menu_language():
        option = input(CookAssist.mensaje('menu_language', False))
        menu = {
            '1': CookAssist.change_language
        }
        return menu.get(option)

    @staticmethod
    def change_language():
        option = input(CookAssist.mensaje('language', False))
        if option == '1':
            Mensajes.men = ES.spanish
        elif option == '2':
            Mensajes.men = EN.english
    
    @staticmethod
    def menu_data():
        option = input(CookAssist.mensaje('menu_data', False))
        menu = {
            '1': CookAssist.add_fictitious_data
        }
        return menu.get(option)

    @staticmethod
    def add_fictitious_data():
        Datos.generarProductos()

    '''if imprimir is True print a string
        if not return a string
    '''
    @staticmethod
    def mensaje(option, show=True):
        if show:
            print(Mensajes.men.get(option))
        else:
            return Mensajes.men.get(option)
    
    @staticmethod
    def sign_off():
        CookAssist.mensaje('sign_off')
        CookAssist.user = None
        CookAssist.chef = False

    @staticmethod
    def close():
        CookAssist.mensaje('close')
        os._exit(0)

    #Usuario
    @staticmethod
    def menu_usuario():
        menu = {}
        option = None
        if CookAssist.chef:
            menu = {
                '1': CookAssist.edit_my_user,
                '2': CookAssist.change_login_way
            }
            option = input(CookAssist.mensaje('menu_usuario_chef', False))
        elif CookAssist.user.get_admin():
            chef = Chef.get_chef_by_email(CookAssist.user.get_email())
            if chef:
                if chef.get_status_chef():
                    menu = {
                        '1': CookAssist.search_user,
                        '2': CookAssist.new_user,
                        '3': CookAssist.edit_my_user,
                        '4': CookAssist.change_to_admin,
                        '5': CookAssist.user_status,
                        '6': CookAssist.change_login_way
                    }
                    option = input(CookAssist.mensaje('menu_usuario_admin_is_chef', False))
                else:
                    menu = {
                        '1': CookAssist.search_user,
                        '2': CookAssist.new_user,
                        '3': CookAssist.edit_my_user,
                        '4': CookAssist.change_to_admin,
                        '5': CookAssist.user_status
                    }
                    option = input(CookAssist.mensaje('menu_usuario_admin', False))
            else:
                menu = {
                    '1': CookAssist.search_user,
                    '2': CookAssist.new_user,
                    '3': CookAssist.edit_my_user,
                    '4': CookAssist.change_to_admin,
                    '5': CookAssist.user_status
                }
                option = input(CookAssist.mensaje('menu_usuario_admin', False))
        else:
            chef = Chef.get_chef_by_email(CookAssist.user.get_email())
            if chef:
                if chef.get_status_chef():
                    menu = {
                        '1': CookAssist.edit_my_user,
                        '2': CookAssist.user_my_status,
                        '3': CookAssist.change_login_way
                    }
                    option = input(CookAssist.mensaje('menu_usuario_user_is_chef', False))
                else:
                    menu = {
                        '1': CookAssist.edit_my_user,
                        '2': CookAssist.user_my_status
                    }
                    option = input(CookAssist.mensaje('menu_usuario_user', False))
            else:
                menu = {
                    '1': CookAssist.edit_my_user,
                    '2': CookAssist.user_my_status
                }
                option = input(CookAssist.mensaje('menu_usuario_user', False))
        
        return menu.get(option)

    @staticmethod
    def login():
        email = input(CookAssist.mensaje('email', False))
        password = input(CookAssist.mensaje('password', False))
        CookAssist.user = Usuario.check_login(email, password)
        if CookAssist.user is None:
            CookAssist.mensaje('user_not_found')
        chef = Chef.get_chef_by_email(CookAssist.user.get_email())
        if chef:
            status = chef.get_status_chef()
            if status:
                CookAssist.change_login_way()

    @staticmethod
    def new_user():
        admin = False
        if CookAssist.user:
            if CookAssist.user.get_admin():
                adm = input(CookAssist.mensaje('admin', False))
                if adm == '1':
                    admin = True
        email = input(CookAssist.mensaje('email', False))
        name = input(CookAssist.mensaje('name', False))
        password = input(CookAssist.mensaje('password', False))
        born_date = input(CookAssist.mensaje('born_date', False))
        if Usuario.get_user_by_email(email) is None:
            Usuario(admin, email, name, password, born_date)
        else:
            CookAssist.mensaje('user_duplicated')
        
    @staticmethod
    def search_user():
        option = input(CookAssist.mensaje('search_user', False))
        if option == '1':
            email = input(CookAssist.mensaje('email', False))
            user = Usuario.get_user_by_email(email)
            if user:
                print(user)
                return user
            else:
                CookAssist.mensaje('user_not_found')
                return None
            
        elif option == '2':
            name = input(CookAssist.mensaje('name', False))
            users = Usuario.get_user_by_name(name)
            if len(users) != 0:
                CookAssist.mensaje('search_user_header')
                for i in range(len(users)):
                    num = str(i + 1)
                    print(num +' '+ users[i].get_email() +' '+ users[i].get_name())
                option = int(input(CookAssist.mensaje('option', False)))
                print(users[(option-1)])
                return users[(option-1)]
            else:
                CookAssist.mensaje('not_match')

    @staticmethod
    def edit_my_user():
        user = CookAssist.user
        option = input(CookAssist.mensaje('edit_my_user', False))
        value = None
        while option != '4':
            if option == '1':
                name = input(CookAssist.mensaje('name', False))
                user.set_name(name)
            elif option == '2':
                old_password = input(CookAssist.mensaje('old_password', False))
                new_password =  input(CookAssist.mensaje('new_password', False))
                if old_password == user.get_password():
                    password = new_password
                    user.set_password(password)
                else:
                    CookAssist.mensaje('wrong_password')
            elif option == '3':
                born_date = input(CookAssist.mensaje('born_date', False))
                user.set_born_date(born_date)
            option = option = input(CookAssist.mensaje('edit_my_user', False))
        
    @staticmethod
    def change_to_admin():
        user = CookAssist.search_user()
        if user:
            admin = False
            adm = input(CookAssist.mensaje('admin', False))
            if adm == '1':
                admin = True
            user.set_admin(admin)
    
    @staticmethod
    def user_status():
        user = CookAssist.search_user()
        if user:
            status = True
            option = input(CookAssist.mensaje('status', False))
            if option == '2':
                status = False
            user.set_status(status)

    @staticmethod
    def user_my_status():
        user = CookAssist.user
        option = input(CookAssist.mensaje('status_inactive', False))
        if option == '1':
            user.set_status(False)
            CookAssist.sign_off()
    
    @staticmethod
    def change_login_way():
        option = input(CookAssist.mensaje('login_way', False))
        if option == '1':
            CookAssist.chef = False
        else:
            CookAssist.chef = True

    #Chef
    @staticmethod
    def menu_chef():
        menu = {}
        option = None
        if CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.search_chef,
                '2': CookAssist.new_chef,
                '3': CookAssist.chef_status,
                '4': CookAssist.promote_to_chef,
                '5': CookAssist.see_best_chef
            }
            option = input(CookAssist.mensaje('menu_chef_admin', False))
        else:
            menu = {
                '1': CookAssist.see_best_chef
            }
            option = input(CookAssist.mensaje('menu_chef_user', False))
        return menu.get(option)

    #Metodo necesario?
    @staticmethod
    def search_chef():
        option = input(CookAssist.mensaje('search_chef', False))
        if option == '1':
            email = input(CookAssist.mensaje('email', False))
            chef = Chef.get_chef_by_email(email)
            if chef:
                print(chef.str_chef())
                return chef
            else:
                CookAssist.mensaje('chef_not_found')
                return None
            
        elif option == '2':
            name = input(CookAssist.mensaje('name', False))
            chefs = Chef.get_chef_by_name(name)
            if len(chefs) != 0:
                CookAssist.mensaje('search_user_header')
                for i in range(len(chefs)):
                    num = str(i + 1)
                    print(num +' '+ chefs[i].get_email() +' '+ chefs[i].get_name())
                option = int(input(CookAssist.mensaje('option', False)))
                print(chefs[(option-1)].str_chef())
                return chefs[(option-1)]
            else:
                CookAssist.mensaje('not_match')

    @staticmethod
    def new_chef():
        admin = False
        if CookAssist.user:
            if CookAssist.user.get_admin():
                adm = input(CookAssist.mensaje('admin', False))
                if adm == '1':
                    admin = True
        email = input(CookAssist.mensaje('email', False))
        name = input(CookAssist.mensaje('name', False))
        password = input(CookAssist.mensaje('password', False))
        born_date = input(CookAssist.mensaje('born_date', False))
        if Usuario.get_user_by_email(email) is None:
            if Chef.get_chef_by_email(email) is None:
                Chef(admin, email, name, password, born_date)
            else:
                CookAssist.mensaje('chef_duplicated')
        else:
            CookAssist.mensaje('user_duplicated')
    @staticmethod
    def chef_status():
        chef = CookAssist.search_chef()
        if chef:
            status = True
            option = input(CookAssist.mensaje('status', False))
            if option == '2':
                status = False
            chef.set_status_chef(status)

    @staticmethod
    def promote_to_chef():
        user = CookAssist.search_user()
        option = input(CookAssist.mensaje('chef_promote', False))
        if option == '1':
            admin = user.get_admin()
            email = user.get_email()
            name = user.get_name()
            password = user.get_password()
            born_date = user.get_born_date()
            chef = Chef(admin, email, name, password, born_date)
            chef.set_promote_calificaciones(user.get_calificaciones())
            chef.set_promote_pedidos(user.get_pedidos())
    
    @staticmethod
    def see_best_chef():
        pass

    #Calificacion TODO
    @staticmethod
    def menu_calificacion():
        menu = {}
        option = None
        if CookAssist.chef:
            menu_pedido = {
                '1': CookAssist.search_my_calificacion,
                '2': CookAssist.search_pedido,
                '3': CookAssist.edit_pedido,
                '4': CookAssist.delete_pedido,
                '5': CookAssist.take_pedido
            }
            option = input(CookAssist.mensaje('menu_pedido_chef', False))
        elif CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.search_my_pedido,
                '2': CookAssist.search_pedido,
                '3': CookAssist.new_pedido,
                '4': CookAssist.edit_pedido,
                '5': CookAssist.delete_pedido,
                '6': CookAssist.generate_a_summary_pedido
            }
            option = input(CookAssist.mensaje('menu_pedido_admin', False))
        else:
            menu = {
                '1': CookAssist.search_my_calificacion,
                '2': CookAssist.edit_my_calificacion,
                '2': CookAssist.new_pedido
            }
            option = input(CookAssist.mensaje('menu_pedido_user', False))
        return menu.get(option)
        

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
    def menu_receta():
        menu = {}
        option = None
        if CookAssist.chef: 
            menu = {
                '1': CookAssist.ver_receta,
                '2': CookAssist.agregar_receta,
                '3': CookAssist.editar_receta,
                '4': CookAssist.activar_desactivar_receta,
                '5': CookAssist.ver_mejores_recetas,
                }
            option = input(CookAssist.mensaje('menu_receta_chef', False))
        
        elif CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.ver_receta,
                '2': CookAssist.agregar_receta,
                '3': CookAssist.editar_receta,
                '4': CookAssist.activar_desactivar_receta,
                '5': CookAssist.ver_mejores_recetas,
                }
            option = input(CookAssist.mensaje('menu_receta_admin', False))
        else:
            menu = {
                '1': CookAssist.ver_todas_recetas,
                '2': CookAssist.ver_mejores_recetas,
                '3': CookAssist.ver_recetas_rapidas
                }
            option = input(CookAssist.mensaje('menu_receta_user', False))
        return menu.get(option)
    
    @staticmethod
    def menu_pedido(opcion):
        menu_pedido = {
            '1': CookAssist.ver_pedidos,
            '2': CookAssist.agregar_pedido,
            '3': CookAssist.editar_pedido,
            '4': CookAssist.eliminar_pedido,
            '5': CookAssist.vaciar_pedidos
        }
        return menu_pedido.get(opcion)

    @staticmethod
    def ver_receta():
        
        CookAssist.mensaje('opcionesVerReceta')
        opcion = input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            codigo = input(CookAssist.mensaje('codigo',False))
            receta= Receta.get_receta_by_codigo(codigo)
            print (receta.toString())
            return receta                                   
            if producto is not None:
                print(Receta.toString())
                return receta
            else:
                CookAssist.mensaje('CodeNotFound')
                return none

    @staticmethod
    def ver_todas_recetas():

        CookAssist.mensaje('opcionesVerTodasRecetas')
        for i in range(0, len(Receta.ListRecetas)):
            if (Receta.ListRecetas[i].get_estado() == True):
                receta=Receta.ListRecetas[i]
                print(receta.toString())
            
    @staticmethod
    def ver_mejores_recetas()
        pass


    @staticmethod
    def ver_recetas_rapidas():
        pass    


            
            
        

    @staticmethod
    def agregar_receta():
       
        nombre = input(CookAssist.mensaje('nombre', False))
        tiempo_preparacion = int(input(CookAssist.mensaje('tiempo', False)))
        estado = int(input(CookAssist.mensaje('estado', False)))
        CookAssist.mensaje('opcionesDetalleReceta1')
        opcion = input(CookAssist.mensaje('opcion', False))
        dr=[]
        while(opcion != '2'):
            if opcion == '1':
                producto = input(CookAssist.mensaje('producto', False))
                cantidad = input(CookAssist.mensaje('cantidad', False))
                receta = input(CookAssist.mensaje('receta', False))
                dr.append(DetalleReceta(producto, cantidad, receta))
            opcion = input(CookAssist.mensaje('opcion', False))

        vr=Receta(nombre, tiempo_preparacion, estado, dr)
        Receta.ListRecetas.append(vr) 
        enter = input(CookAssist.mensaje('Receta_Agregada', False))   

            
            
    @staticmethod
    def editar_receta():
        receta = CookAssist.ver_receta()
        CookAssist.mensaje('editar_receta')
        opcion = input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            nombre = input(CookAssist.mensaje('nombre', False))
            Receta.set_nombre(nombre)
        elif opcion == '2':
            tiempo = input(CookAssist.mensaje('tiempo_preparacion', False))
            Receta.set_tiempo_preparacion(tiempo)
        elif opcion == '3':
            '''
            CookAssist.mensaje('editar_DetalleReceta')
            opcion = input(CookAssist.mensaje('opcion', False)
            if opcion == '1':
                codigo = input(CookAssist.mensaje('codigo', False))
                producto = get_producto_by_codigo(codigo)           
                cantidad = input(CookAssist.mensaje('cantidad', False))
                DetalleReceta.set_cantidad(cantidad) 
                # se supone quedo saber que a que produto le estoy cambiando la cantidad           
            elif opcion == '2':
                pass
            '''    

                           
                           
            
    @staticmethod
    def activar_desactivar_receta():
        CookAssist.mensaje('opciones_activar_desactivar')
        opcion= input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            codigo = input(CookAssist.mensaje('codigo', False))
            receta= Receta.get_receta_by_codigo(codigo)
            if(receta.get_estado() == True):
                receta.set_estado(0)
        elif opcion == '2':
            codigo = input(CookAssist.mensaje('codigo', False))
            receta= Receta.get_receta_by_codigo(codigo)
            if(receta.get_estado() == False):
                receta.set_estado(1)                                        
        
    @staticmethod
    def ver_pedidos():
        if(len(Pedido._list_pedidos)>0):
            for ped in Pedido._list_pedidos:
                print (ped.get_nombre()," pedido por ",ped.get_usuario(), " con ",ped.get_fecha())
        else:
            CookAssist.mensaje('pedidos_not_found',True)

    def agregar_pedido():
        nombre = input(CookAssist.mensaje('agregar_pedido_1',False))
        descripcion = input(CookAssist.mensaje('agregar_pedido_2',False))
        usuario = input(CookAssist.mensaje('agregar_pedido_3',False))
        chef = input(CookAssist.mensaje('agregar_pedido_4',False))
        
        op1 = input(CookAssist.mensaje('agregar_detalle_pedido',False))
        dp = []

        while(op1 != '2'):
            if(op1 == '1'):
                d_codigo = input(CookAssist.mensaje('agregar_d_pedido_1',False))
                d_cant = input(CookAssist.mensaje('agregar_d_pedido_2',False))
                d_pedido = input(CookAssist.mensaje('agregar_d_pedido_3',False))
                d_receta = input(CookAssist.mensaje('agregar_d_pedido_4',False))
                d_prod = input(CookAssist.mensaje('agregar_d_pedido_5',False))
                dp.append(Detalle_pedido(d_codigo,d_cant,d_pedido,d_receta,d_prod))
            op1 = input(CookAssist.mensaje('agregar_detalle_pedido',False))
        if(len(dp)==0):
            dp.apend("Sin detalle")

        Pedido(nombre,'fecha',descripcion,dp,usuario,chef) 
        
        #Pedido() # Objeto de Pruebas

        enter = input(CookAssist.mensaje('pedido_agregado',False))


    def editar_pedido():
        op1 = int(input(CookAssist.mensaje('editar_pedido',False)))
        if(op1 == 1):
            fecha = "Fecha: "
            dia = input(CookAssist.mensaje('pedido_fecha_d',False))
            fecha += str(dia)
            mes = input(CookAssist.mensaje('pedido_fecha_m',False))
            fecha += ("-"+str(mes))
            año = input(CookAssist.mensaje('pedido_fecha_a',False))
            fecha += ("-"+str(año))
            hora = input(CookAssist.mensaje('pedido_fecha_h',False))
            fecha += (" Hora: " + hora)
            minuto = input(CookAssist.mensaje('pedido_fecha_min',False))
            fecha += (":"+minuto)
            seg = input(CookAssist.mensaje('pedido_fecha_s',False))
            fecha += (":"+seg)
            for f in Pedido._list_pedidos:
                if(f.get_fecha() == fecha):
                    CookAssist.mensaje('editar_pedido_2',True)
                    nombre = input(CookAssist.mensaje('agregar_pedido_1',False))
                    descripcion = input(CookAssist.mensaje('agregar_pedido_2',False))
                    usuario = input(CookAssist.mensaje('agregar_pedido_3',False))
                    chef = input(CookAssist.mensaje('agregar_pedido_4',False))
                    p1 = Pedido(nombre,'fecha',descripcion,'detalle',usuario,chef)
                    f.modify_all_values(nombre,'fecha',descripcion,'detalle',usuario,chef)
                else:
                    op_r = input(CookAssist.mensaje('fecha_not_found',False))
        elif(op1 == 2):
            pass
        else:
            CookAssist.mensaje('opcionNoValida',True)
        
    def eliminar_pedido():
        op1 = input(CookAssist.mensaje('eliminar_pedido',False))
        if(op1 == '1'):
            fecha = "Fecha: "
            dia = input(CookAssist.mensaje('pedido_fecha_d',False))
            fecha += str(dia)
            mes = input(CookAssist.mensaje('pedido_fecha_m',False))
            fecha += ("-"+str(mes))
            año = input(CookAssist.mensaje('pedido_fecha_a',False))
            fecha += ("-"+str(año))
            hora = input(CookAssist.mensaje('pedido_fecha_h',False))
            fecha += (" Hora: " + hora)
            minuto = input(CookAssist.mensaje('pedido_fecha_min',False))
            fecha += (":"+minuto)
            seg = input(CookAssist.mensaje('pedido_fecha_s',False))
            fecha += (":"+seg)
            for f in Pedido._list_pedidos:
                if(f.get_fecha() == fecha):
                    Pedido._list_pedidos.remove(f)
                    Pedido._num_pedidos_eliminados += 1
                    CookAssist.mensaje('pedido_eliminado',True)
                    break
        elif(op1 == '2'):
            Pedido._list_pedidos.pop()
            CookAssist.mensaje('pedido_eliminado',True)
        elif(op1 == '3'):
            pass
        else:
            CookAssist.mensaje('opcionNoValida',True)

    def vaciar_pedidos():
        Pedido._list_pedidos.clear()      
        Pedido._num_pedidos_eliminados += len(Pedido._list_pedidos)
        Detalle_pedido._list_detalle_pedido.clear()                       
        CookAssist.mensaje('pedido_eliminado',True)       
                                               
                                               
    @staticmethod
    def menu_producto(opcion):
        menu_producto = {
            '1': CookAssist.ver_producto,
            '2': CookAssist.agregar_producto,
            '3': CookAssist.editar_producto
        }
        return menu_producto.get(opcion)
    
    @staticmethod
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
            producto = Producto.get_producto_by_nombre(nombre1)
            if producto is not None:
                print(producto.toString())
                return producto
            else:
                CookAssist.mensaje('codeNotFound')
                return None
                
    @staticmethod
    def agregar_producto():
        pass

    @staticmethod
    def editar_producto():
        pass

    @staticmethod
    def run():

        Mensajes.men = Mensajes.spanish
        Chef(True, 'juanca5481999@gmail.com', 'Juan Jaramillo', '12345','7/11/1999')
        Chef(True, 'alemandoa@gmail.com', 'Alejandro Jiménez', '12345', '28/10/1999')
        Usuario(False, 'ejemplo@gmail.com', 'NN', '12345', '01/01/1963')
        while True:

            while CookAssist.user is None:
                CookAssist.enter()

            while CookAssist.user is not None:
                CookAssist.main()
            

if __name__ == '__main__':
    
    CookAssist.run()
