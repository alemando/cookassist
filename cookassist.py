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
                '5': CookAssist.ver_todas_recetas,
                }
            option = input(CookAssist.mensaje('menu_receta_chef', False))
        
        elif CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.ver_receta,
                '2': CookAssist.agregar_receta,
                '3': CookAssist.editar_receta,
                '4': CookAssist.activar_desactivar_receta,
                '5': CookAssist.ver_todas_recetas,
                }
            option = input(CookAssist.mensaje('menu_receta_admin', False))
        else:
            menu = {
                '1': CookAssist.ver_todas_recetas,
                
                }
            option = input(CookAssist.mensaje('menu_receta_user', False))
        return menu.get(option)

    


    @staticmethod
    def ver_receta():
        
        CookAssist.mensaje('opcionesVerReceta1')
        opcion = input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            codigo = input(CookAssist.mensaje('codigo',False))
            receta= Receta.get_receta_by_codigo(codigo)
            if receta is not None:
                print(receta.toString())
                #for rec in rec.get_detalle_recetas():
                            #print(rec.get_codigo(),' Producto: ',rec2.get_producto(), 'cantidad', rec2.get_cantidad())           

                return receta
            else:
                CookAssist.mensaje('codeNotFound')
                return None
        
        elif opcion == '2':
            nombre = input(CookAssist.mensaje('nombre', False))
            receta = Receta.get_receta_by_nombre(nombre)
            for receta1 in receta:
                if receta1 is not None:
                    print(receta1.toString())
                    return receta1
                
                else:
                    CookAssist.mensaje('CodeNotFound')
                    return None

    @staticmethod
    def ver_todas_recetas():

        CookAssist.mensaje('opcionesVerTodasRecetas')
        opcion = input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            for i in Receta.ListRecetas.values():
                if (i.get_estado() == True):
                    print(i.toString())

        elif opcion == '2':
            for i in Receta.ListRecetas.values():
                if (i.get_estado() == False):
                    print(i.toString())


            


            
            
        

    @staticmethod
    def agregar_receta():
       
        nombre = input(CookAssist.mensaje('nombre', False))
        tiempo_preparacion = int(input(CookAssist.mensaje('tiempo', False)))
        estado = int(input(CookAssist.mensaje('estado', False)))
        CookAssist.mensaje('opcionesDetalleReceta1')
        opcion = input(CookAssist.mensaje('opcion', False))
        vr_receta=Receta(nombre, tiempo_preparacion, estado, [])
        dr=[]
        while(opcion != '2'):
            d_producto = None
            if opcion == '1':
                op2 = input(CookAssist.mensaje('agregar_d_receta_producto',False)) #Producto
                find = False
                while(op2 != '3'):
                    if op2 == '1':
                        CookAssist.ver_productos_disponibles()
                    elif op2 == '2':
                        cod_producto = input(CookAssist.mensaje('cod_producto', False))
                        for p in Producto.ListProductos:
                            if(p == cod_producto): 
                                d_producto = Producto.ListProductos[p]
                                find = True
                                print("Agregado") ## Organizar
                        if(not find):
                            CookAssist.mensaje('producto_not_found',True)
                    
                    else:
                        CookAssist.mensaje('producto_opcion_no_valida',False)
                    op2 = input(CookAssist.mensaje('agregar_d_receta_producto',False))
                cantidad = input(CookAssist.mensaje('cantidad', False))    
                vr_codigo = vr_receta.get_codigo() + d_producto.get_codigo()
                dr.append(DetalleReceta(vr_codigo, cantidad, d_producto, vr_receta))
            opcion = input(CookAssist.mensaje('opcion', False))

        vr_receta.set_detalle_recetas(dr)
        #Receta.ListRecetas[(self.get_codigo())] = vr 
        enter = input(CookAssist.mensaje('Receta_Agregada', False))   

            
            
    @staticmethod
    def editar_receta():
        CookAssist.ver_todas_recetas()
        codigo = input(CookAssist.mensaje('cod_rece_edit', False))
        receta = Receta.get_receta_by_codigo(codigo)
        CookAssist.mensaje('editar_receta')
        opcion = input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            nombre = input(CookAssist.mensaje('nombre', False))
            receta.set_nombre(nombre)
        elif opcion == '2':
            tiempo = input(CookAssist.mensaje('tiempo_preparacion', False))
            receta.set_tiempo_preparacion(tiempo)
        elif opcion == '3':
            CookAssist.mensaje('editar_DetalleReceta1')
            opcion1 = input(CookAssist.mensaje('opcion', False))
            if opcion1 == '1':
                codigo = input(CookAssist.mensaje('cod_producto', False))
                producto = Producto.get_producto_by_codigo(codigo)           
                for rec in receta._ListDetalleRecetas:
                    for i in range(0, len(rec)):
                        if (rec[i].get_producto() == producto):
                            cantidad = input(CookAssist.mensaje('cantidad', False))
                            rec[i].set_cantidad(cantidad)
            
            elif opcion1 == '2':
                codigo = input(CookAssist.mensaje('codigo_detalle', False))
                posicion = DetalleReceta.get_posicion_lista(codigo)
                vr_detalle=DetalleReceta.delete_element(posicion)
                receta.delete_detalle_recetas()
                receta.set_detalle_recetas(vr_detalle)


                
                

                           
                           
            
    @staticmethod
    def activar_desactivar_receta():

        CookAssist.mensaje('opciones_activar_desactivar')
        opcion = input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            CookAssist.mensaje('opciones_desactivar_receta')
            opcion = input(CookAssist.mensaje('opcion', False))
            if opcion == '1':
                codigo = input(CookAssist.mensaje('codigo', False))
                receta= Receta.get_receta_by_codigo(codigo)
                if(receta.get_estado() == True):
                    receta.set_estado(0)
            elif opcion == '2':
                nombre = input(CookAssist.mensaje('nombre', False))
                receta= Receta.get_receta_by_nombre(nombre)
                for receta1 in receta:
                    if receta1 is not None:
                        if(receta1.get_estado() == True):
                            receta1.set_estado(0)
        elif opcion == '2':
            CookAssist.mensaje('opciones_activar_receta')
            opcion = input(CookAssist.mensaje('opcion', False))
            if opcion == '1':
                codigo = input(CookAssist.mensaje('codigo', False))
                receta= Receta.get_receta_by_codigo(codigo)
                if(receta.get_estado() == False):
                    receta.set_estado(1)
            elif opcion == '2':
                nombre = input(CookAssist.mensaje('nombre', False))
                receta= Receta.get_receta_by_nombre(nombre)
                for receta1 in receta:
                    if receta1 is not None:
                        if(receta1.get_estado() == False):
                            receta1.set_estado(1)
                            
    @staticmethod
    def set_chef_pedido():
        option = input(CookAssist.mensaje('set_chef_pedido', False))
        while option != '3':
            if option == '1':
                if(Pedido.get_primer_pedido() != None):
                    CookAssist.user.set_pedidos_chef(Pedido.get_primer_pedido())
                else:
                    CookAssist.mensaje('pedidos_false_not_found',True)
            elif option == '2':
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
                for p in Pedido._list_pedidos:
                    if(p.get_fecha() == fecha and p.get_estado() == False):
                        CookAssist.user.set_pedidos_chef(p)
                    else:
                        CookAssist.mensaje('pedidos_false_not_found',True)
            option = input(CookAssist.mensaje('set_chef_pedido', False))

    @staticmethod
    def menu_pedido():
        menu = {}
        option = None
        if CookAssist.chef:  # Ver Pedidos, Asignar pedidos
            menu = {
                '1': CookAssist.ver_pedidos,
                '2': CookAssist.set_chef_pedido
            }
            option = input(CookAssist.mensaje('pedido_chef', False))
        
        elif CookAssist.user.get_admin(): # ver, editar, eliminar
            menu = {
                '1': CookAssist.ver_pedidos,
                '2': CookAssist.editar_pedido,
                '3': CookAssist.eliminar_pedido
            }
            option = input(CookAssist.mensaje('pedido_admin', False))
        else: # hacer pedidos , ver mis pedidos
            menu = {
                '1': CookAssist.ver_pedidos,
                '2': CookAssist.agregar_pedido
            }
            option = input(CookAssist.mensaje('pedido_user', False))
        
        return menu.get(option)

    @staticmethod
    def ver_pedidos():
        if(CookAssist.chef):
            if(len(Pedido._list_pedidos)>0):
                for ped in Pedido._list_pedidos:
                    if(ped.get_estado()):
                        for ped2 in ped.get_detalle():
                            if(ped2.get_producto()==None):
                                print(ped.get_codigo(),' Receta: ',ped2.get_receta(),' Entregado')
                            else:
                                print(ped.get_codigo(),' Producto: ',ped2.get_producto(),' Entregado')
                    else:
                        for ped2 in ped.get_detalle():
                            if(ped2.get_producto()==None):
                                print(ped.get_codigo(),' Receta: ',ped2.get_receta(),' No Entregado')
                            else:
                                print(ped.get_codigo(),' Producto: ',ped2.get_producto(),' No Entregado')
            else:
                CookAssist.mensaje('pedidos_not_found',True)
        elif(CookAssist.user.get_admin()):
            if(len(Pedido._list_pedidos)>0):
                for ped in Pedido._list_pedidos:
                    for ped2 in ped.get_detalle():
                        if(ped2.get_producto()==None):
                            print(ped.get_codigo(),' Receta: ',ped2.get_receta(),' ',ped.get_usuario().get_email())
                        else:
                            print(ped.get_codigo(),' Producto: ',ped2.get_producto(),' ',ped.get_usuario().get_email())
            else:
                CookAssist.mensaje('pedidos_not_found',True)
        else:
            if(len(CookAssist.user._ListPedidos)>0):
                option = input(CookAssist.mensaje('ver_solo_codigo',False))
                while(option != '3'):
                    if(option == '1'):
                        for ped in CookAssist.user._ListPedidos:                  
                            if(CookAssist.user._ListPedidos[ped].get_estado()):
                                print (CookAssist.user._ListPedidos[ped].get_codigo(),' Entregado')
                                
                            else:
                                print(CookAssist.user._ListPedidos[ped].get_codigo(), ' No entregado')

                    elif option == '2':
                        code = int(input(CookAssist.mensaje('pedido_code',False)))
                        for ped in CookAssist.user._ListPedidos: 
                            if CookAssist.user._ListPedidos[ped].get_codigo() == code:
                                for ped2 in CookAssist.user._ListPedidos[ped].get_detalle():
                                    for ped3 in ped2:
                                        if(ped3.get_producto()==None):
                                            print(code,' Receta: ',ped3.get_receta().get_nombre())
                                            #h = str(datetime.now().hour).zfill(2)
                                            #m = str(datetime.now().minute).zfill(2)
                                            #s = str(datetime.now().second).zfill(2)
                                            #hour = h+':'+m+':'+s
                                            #print ("Pedido hace: ",CookAssist.user._ListPedidos[ped].restar_hora(hour,CookAssist.user._ListPedidos[ped].get_tiempo()))
                                        else:
                                            print(code,' Producto: ',ped3.get_producto().get_nombre())
                                            #h = str(datetime.now().hour).zfill(2)
                                            #m = str(datetime.now().minute).zfill(2)
                                            #s = str(datetime.now().second).zfill(2)
                                            #hour = h+':'+m+':'+s
                                            #print ("Pedido hace: ",CookAssist.user._ListPedidos[ped].restar_hora(hour,CookAssist.user._ListPedidos[ped].get_tiempo()))
                            else:
                                CookAssist.mensaje('code_not_found',True)
                                
                    option = input(CookAssist.mensaje('ver_solo_codigo',False))


            else:
                CookAssist.mensaje('pedidos_not_found',True)

    @staticmethod
    def agregar_pedido():

        usuario = CookAssist.user
        
        op1 = input(CookAssist.mensaje('agregar_detalle_pedido',False))
        dp = []

        rec_ya = True
        ped_ya = True

        no_rec_prod = False

        d_receta = None
        d_prod = None
        d_cant = 0

        while(op1 != '3' and (rec_ya or ped_ya)): #Detalle
            if(op1 == '1'):
                op2 = input(CookAssist.mensaje('agregar_d_pedido_5',False)) #Producto
                while(op2 != '3'):
                    if op2 == '1':
                        CookAssist.ver_producto()
                    elif op2 == '2':
                        d_prod_code = str(input(CookAssist.mensaje('pedido_code',False)))#.zfill(6)
                        for p in Producto.ListProductos:
                            if(Producto.ListProductos[p].get_codigo() == d_prod_code): 
                                d_prod = Producto.ListProductos[p]
                                ped_ya = False
                                d_cant = input(CookAssist.mensaje('agregar_d_pedido_2',False))
                                CookAssist.mensaje('pedido_rp_agregado',True)
                            else:
                                CookAssist.mensaje('producto_not_found',True)
                    elif op2 == '3':
                        pass
                    else:
                        CookAssist.mensaje('pedido_opcion_no_valida',False)

                    op2 = input(CookAssist.mensaje('agregar_d_pedido_5',False))

            elif(op1 == '2'):
                op2 = input(CookAssist.mensaje('agregar_d_pedido_3',False)) #Receta
            
                while(op2 != '3'):
                    if op2 == '1':
                        CookAssist.ver_todas_recetas()
                    elif op2 == '2':
                        d_receta_code = str(input(CookAssist.mensaje('pedido_code',False)))#.fill(6)
                        if((Receta.get_receta_by_codigo(d_receta_code)).get_codigo() == (d_receta_code)):
                            d_receta = Receta.get_receta_by_codigo(d_receta_code).get_codigo()
                            d_cant = input(CookAssist.mensaje('agregar_d_pedido_2',False))
                            CookAssist.mensaje('pedido_rp_agregado',True)
                            rec_ya = False
                        else:
                            CookAssist.mensaje('receta_not_found',True)
                    elif op2 == '3':
                        pass
                    else:
                        CookAssist.mensaje('pedido_opcion_no_valida',True)

                    op2 = input(CookAssist.mensaje('agregar_d_pedido_3',False))

                    

            elif op1 == '3':
                pass
                    
            else:
                CookAssist.mensaje('pedido_opcion_no_valida',True)
                
            dp.append(Detalle_pedido(d_cant,d_receta,d_prod))

            if(rec_ya or ped_ya): # Por si ya hay producto o receta no aparezca esta opcion
                op1 = input(CookAssist.mensaje('agregar_detalle_pedido',False))

        if(d_receta != None or d_prod != None):
            no_rec_prod = True
        if(no_rec_prod):
            descripcion = input(CookAssist.mensaje('agregar_pedido_2',False))
            
            while descripcion == '?':
                CookAssist.mensaje('pedido_ayuda_des',True)
                descripcion = input(CookAssist.mensaje('agregar_pedido_2',False))

            d_pedido = Pedido(descripcion,dp,usuario) 
            CookAssist.user.set_pedidos(d_pedido)
            for d_p in dp:
                d_p.set_pedido(d_pedido)

            enter = input(CookAssist.mensaje('pedido_agregado',False))

        else:
            print('Pedido No Agregado, no hay seleccion')

    @staticmethod
    def editar_pedido(): #Admin 
        op1 = input(CookAssist.mensaje('editar_pedido',False))
        while(op1 != '2'):
            if op1 == '1':
                code = str(input(CookAssist.mensaje('pedido_code',False))).zfill(6)
                for ped in Pedido._list_pedidos:
                    if ped.get_codigo == code:
                        
                        edited_rec = False
                        edited_prod = False

                        op3 = input(CookAssist.mensaje('editar_p_o_r',False))
                        while(op3 != '1' or op3 != '2'):
                            CookAssist.mensaje('pedido_opcion_no_valida',True)
                            op3 = input(CookAssist.mensaje('editar_p_o_r',False))

                        if(op3 == '1'):
                            edited_rec = True
                        elif(op3 == '2'):
                            edited_prod = True

                        if(edited_rec): 
                            op2 = input('editar_por_codigo_rec',False) 
                            while op2 != '2':
                                if(op2 == '1'):
                                    for d_rec in ped.get_detalle():
                                        if(d_rec.get_producto() == None):
                                            print(d_rec.get_receta().get_nombre(),' : ',d_rec.get_receta().get_codigo())
                                op2 = input('editar_por_codigo_rec',False) 
                            if op2 == '2':
                                code = str(CookAssist.mensaje('pedido_code',False)).zfill(6)
                                for d_rec in ped.get_detalle():
                                    if d_rec.get_producto() == None and d_rec.get_receta().get_codigo() == code:
                                        code2 = str(input(CookAssist.mensaje('detalle_editar_receta',False)))
                                        d_rec.set_receta(Receta.ListRecetas[code2])
                                        CookAssist.mensaje('ped_rec_edit',True) #Receta Editada correctyamente
                                        d_rec.set_cantidad(input('pedido_editar_cant',False))
                                    else:
                                        CookAssist.mensaje('receta_not_found',True)

                        if(edited_prod):
                            op2 = input('editar_por_codigo_prod',False) 
                            while op2 != '2':
                                if(op2 == '1'):
                                    for d_prod in ped.get_detalle():
                                        if(d_prod.get_receta() == None):
                                            print(d_prod.get_producto().get_nombre(),' : ',d_rec.get_producto().get_codigo())
                                op2 = input('editar_por_codigo_prod',False) 
                            if op2 == '2':
                                code = str(CookAssist.mensaje('pedido_code',False)).zfill(6)
                                for d_prod in ped.get_detalle():
                                    if d_prod.get_receta() == None and d_prod.get_producto().get_codigo() == code:
                                        code2 = str(input(CookAssist.mensaje('detalle_editar_producto',False)))
                                        d_prod.set_producto(Producto.ListProductos[code2])
                                        CookAssist.mensaje('ped_prod_edit',True) #producto Editado Corectamente
                                        d_rec.set_cantidad(input('pedido_editar_cant',False))
                                    else:
                                        CookAssist.mensaje('receta_not_found',True)

                        ped.set_descripcion(input('pedido_editar_desc',False))

                        CookAssist.mensaje('ped_edit',True)

                    else:
                        CookAssist.mensaje('pedidos_not_found',True)
            elif op1 == '2':
                pass
            else:
                CookAssist.mensaje('pedido_opcion_no_valida',True)

            op1 = input(CookAssist.mensaje('editar_pedido',False))
        
    @staticmethod
    def eliminar_pedido(): # Chef
        op = input(CookAssist.mensaje('eliminar_pedido',False))
        while op != '4':
            if(len(Pedido._list_pedidos)>0):
                if(op == '1'):
                    code = input(CookAssist.mensaje('pedido_code',False)).zfill(6)
                    for ped in Pedido._list_pedidos:
                        if(ped.get_codigo() == code):
                            Pedido._list_pedidos.remove(ped)
                            Pedido._num_pedidos_eliminados += 1
                            CookAssist.mensaje('pedido_eliminado',True)
                elif(op == '2'):
                    
                        Pedido._list_pedidos.pop()
                        Pedido._num_pedidos_eliminados += 1
                        CookAssist.mensaje('pedido_eliminado',True)
                    
                elif(op == '3'):
                    CookAssist.vaciar_pedidos()
                elif(op == '4'):
                    pass
                else:
                    CookAssist.mensaje('pedido_opcion_no_valida',True)
                
            else:
                CookAssist.mensaje('pedidos_not_found',True)
            op = input(CookAssist.mensaje('eliminar_pedido',False))

    @staticmethod
    def vaciar_pedidos():
        Pedido._num_pedidos_eliminados += len(Pedido._list_pedidos)
        Pedido._list_pedidos.clear()
        Usuario._list_pedidos.clear()      
        Detalle_pedido._list_detalle_pedido.clear()                       
        CookAssist.mensaje('pedido_eliminado',True) 
        
    @staticmethod
    def menu_producto():
        menu = {}
        option = None
        if CookAssist.chef:
            menu = {
                '1': CookAssist.ver_producto,
                '2': CookAssist.agregar_producto,
                '3': CookAssist.editar_producto,
                '4': CookAssist.change_quantity,
                '5': CookAssist.ver_productos_disponibles,
                '6': CookAssist.ver_lista_de_compras
            }
            option = input(CookAssist.mensaje('menu_producto_chef', False))
        elif CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.ver_producto,
                '2': CookAssist.agregar_producto,
                '3': CookAssist.editar_producto,
                '4': CookAssist.change_quantity,
                '5': CookAssist.ver_productos_disponibles,
                '6': CookAssist.ver_lista_de_compras
            }
            option = input(CookAssist.mensaje('menu_producto_admin', False))
        else:
            menu = {
                '1': CookAssist.ver_producto
            }
            option = input(CookAssist.mensaje('menu_producto_user', False))
        return menu.get(option)
    
    @staticmethod
    def ver_producto():
        CookAssist.mensaje('ver_producto')
        opcion = input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            codigo = input(CookAssist.mensaje('codigoP', False))
            producto = Producto.get_producto_by_codigo(codigo)
            if producto:
                print(producto)
                return producto
            else:
                CookAssist.mensaje('codeNotFound')
                return None
            
        elif opcion == '2':
            nombre1 = input(CookAssist.mensaje('nombreP', False))
            producto1 = Producto.get_producto_by_nombre(nombre1)
            if len(producto1) != 0:
                CookAssist.mensaje('buscar_prod_c')
                for i in range(len(producto1)):
                    num1= str(i+1)
                    print(num1 + '   ' + producto1[i].get_codigo().zfill(6) + '   ' + producto1[i].get_nombre())
                oppcion= int(input(CookAssist.mensaje('opcion', False)))
                producto1 = producto1[(oppcion-1)]
                print(producto1)
                return producto1
            else:
                CookAssist.mensaje('producto_not_found')
                
    @staticmethod
    def agregar_producto():
        name = input(CookAssist.mensaje('agregar_producto_1', False))
        cant = int(input(CookAssist.mensaje('agregar_producto_2', False)))
        med = input(CookAssist.mensaje('agregar_producto_3', False))
        opcionestad= input(CookAssist.mensaje('disponibilidad_p', False))
        if opcionestad == '1':
            opcionestad = True
        elif opcionestad == '2':
            opcionestad = False
        else:
            pass

        Producto(name, cant, med, opcionestad)

        enter1= input(CookAssist.mensaje('producto_agregado', False))

#    @staticmethod
#    def producto_status():
#        pass

    @staticmethod
    def editar_producto():
        auxpro= CookAssist.ver_producto()
        if auxpro is not None:
            CookAssist.mensaje('editar_producto')
            opcionedit = input(CookAssist.mensaje('opcion', False))
            if opcionedit == '1':
                nombrenu = input(CookAssist.mensaje('editar_nombre_p', False))
                auxpro.set_nombre(nombrenu)

            elif opcionedit == '2':
                cantnu= int(input(CookAssist.mensaje('editar_cantidad_p', False)))
                auxpro.set_cantidad(cantnu)
            elif opcionedit == '3':
                CookAssist.mensaje('cambiar_estado_p')
                opcionactiv= input(CookAssist.mensaje('opcion', False))
                if opcionactiv == '1':
                    auxpro.set_estado(True)
                elif opcionactiv == '2':
                    auxpro.set_estado(False)
                    auxpro.set_cantidad(0)
                else:
                    pass
            elif opcionedit == '4':
                medicionnu = input(CookAssist.mensaje('cambiar_medicion_p', False))
                auxpro.set_medicion(medicionnu)     
            else: 
                pass
            auxpro.actualizar_en_txt()
        else:
            pass
    
    @staticmethod
    def change_quantity():
        auxpro= CookAssist.ver_producto()
        CookAssist.mensaje('cambiar_cantidad_p')
        opcioncam= input(CookAssist.mensaje('opcion', False))
        if opcioncam == '1':
            canti= int(input(CookAssist.mensaje('agregar_cantidad_p', False)))
            auxpro.cambiar_cantidad(canti)
        elif opcioncam == '2':
            canti= int(input(CookAssist.mensaje('restar_cantidad_p', False)))
            canti1 = canti*(-1)
            auxpro.cambiar_cantidad(canti1)
        else:
            pass
        
    
    @staticmethod
    def ver_productos_disponibles():
        listaaux = Producto.productos_disponibles()
        if len(listaaux) != 0:
            CookAssist.mensaje('prod_disponibles')
            for n in range(len(listaaux)):
                print(listaaux[n].get_codigo().zfill(6) + '  ' + listaaux[n].get_nombre())
        else:
            pass
    
    @staticmethod
    def ver_lista_de_compras():
        listcompra= Producto.lista_de_compras()
        if len(listcompra) != 0:
            CookAssist.mensaje('prod_a_comprar')
            for i in range(len(listcompra)):
                print(listcompra[i].get_codigo().zfill(6) + '  '+ listcompra[i].get_nombre() +'   '+str(listcompra[i].get_cantidad())+listcompra[i].get_medicion())
        else:
            return CookAssist.mensaje('prod_suficientes')
        

    @staticmethod
    def run():

        Mensajes.men = Mensajes.spanish
        Chef(True, 'juanca5481999@gmail.com', 'Juan Jaramillo', '12345','7/11/1999')
        CookAssist.user = Chef(True, 'alemandoa@gmail.com', 'Alejandro Jiménez', '12345', '28/10/1999')
        Usuario(False, 'ejemplo@gmail.com', 'NN', '12345', '01/01/1963')
        Usuario(True,'juan@dios.net','juan','666','01/01/0001')
        
        while True:

            while CookAssist.user is None:
                CookAssist.enter()

            while CookAssist.user is not None:
                CookAssist.main()
            

if __name__ == '__main__':
    
    CookAssist.run()

