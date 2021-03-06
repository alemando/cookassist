

class Mensajes:
    
    men = {}

    spanish = {
    'language' :'''
    Idioma:
    1. Español
    2. Ingles
    Seleccione: ''',
    'sign_off' : 'Cerrando sesion',
    'enter' : '''
    Bienvenido a CookAssist
    ¿es usted un?
    1. Usuario registrado
    2. Usuario sin registrar
    3. Salir
    Seleccione una opcion: ''',
    'email' : 'Ingrese su email: ',
    'password' : 'Ingrese su contraseña: ',
    'name' : 'Ingrese su nombre: ',
    'admin' : '''
    Usuario administrador?
    1. Si
    2. No
    Ingrese la opcion: ''',
    'born_date' : 'Ingrese su fecha de nacimiento(dd/mm/yyyy): ',
    'user_not_found' : 'Usuario no encontrado',
    'menu_main_admin' : '''
    Menú
    1. Menu Productos
    2. Menu Recetas
    3. Menu Pedidos
    4. Menu Calificaciones
    5. Menu Chefs
    6. Menu Usuarios
    7. Menu Idiomas
    8. Menu Datos
    9. Cerrar Sesión
    Seleccione una opción: ''',
    'menu_main_chef' : '''
    Menú
    1. Menu Productos
    2. Menu Recetas
    3. Menu Pedidos
    4. Menu Chefs
    5. Menu Usuario
    6. Menu Idiomas
    7. Cerrar Sesión
    Seleccione una opción: ''',
    'menu_main_user' : '''
    Menú
    1. Menu Productos
    2. Menu Recetas
    3. Menu Pedidos
    4. Menu Calificaciones
    5. Menu Chefs
    6. Menu Usuario
    7. Menu Idiomas
    8. Cerrar Sesión
    Seleccione una opción: ''',
    'menu_data' : '''
    Menú Datos
    1. Agregar datos ficticios
    2. <-Atras
    Seleccione una opción: ''',
    'menu_language' : '''
    Menú Idiomas
    1. Cambiar idioma
    2. <-Atras
    Seleccione una opción: ''',
    'menu_usuario_admin': '''
    Menú Usuario
    1. Buscar usuario
    2. Nuevo usuario
    3. Editar mi usuario
    4. Cambiar permisos
    5. Activar/Desactivar usuario
    6. <-Atras
    Seleccione una opción: ''',
    'menu_usuario_admin_is_chef': '''
    Menú Usuario
    1. Buscar usuario
    2. Nuevo usuario
    3. Editar mi usuario
    4. Cambiar permisos
    5. Activar/Desactivar usuario
    6. Cambiar modo de inicio
    7. <-Atras
    Seleccione una opción: ''',
    'menu_usuario_chef': '''
    Menú Usuario
    1. Editar mi usuario
    2. Cambiar modo de inicio
    3. <-Atras
    Seleccione una opción: ''',
    'menu_usuario_user': '''
    Menú Usuario
    1. Editar mi usuario
    2. Desactivar mi usuario
    3. <-Atras
    Seleccione una opción: ''',
    'menu_usuario_user_is_chef': '''
    Menú Usuario
    1. Editar mi usuario
    2. Desactivar mi usuario
    3. Cambiar modo de inicio
    4. <-Atras
    Seleccione una opción: ''',
    'search_user' : '''
    Buscar usuario por:
    1. email
    2. Nombre
    3. <-Atras
    Seleccione una opción: ''',
    'not_match' : 'Nó se encontraron coincidencias',
    'yes' : 'Si',
    'no' : 'NO',
    'str_user' : '''
    Administrador: %s
    Nombre: %s
    email: %s
    Fecha nacimiento: %s
    Estado: %s
    ''',
    'active' : 'Activo',
    'inactive' : 'Inactivo',
    'search_user_header' : '# Email                Nombre',
    'option' : 'Seleccione una opción: ',
    'close' : 'Programa Cerrado',
    'menu_chef_admin' : '''
    Menú Chef
    1. Buscar chef
    2. Nuevo chef
    3. Activar/Desactivar chef
    4. Promover a chef
    5. Ver mejor chef
    6. <-Atras
    Seleccione una opción: ''',
    'menu_chef_user' : '''
    Menú Chef
    1. Ver mejor chef
    2. <-Atras
    Seleccione una opción: ''',
    'menu_producto_chef' : '''
    Menú Productos
    1. Buscar producto
    2. Nuevo producto
    3. Editar producto
    4. Añadir existencias
    5. Ver productos disponibles
    6. Ver lista de compras
    7. <-Atras
    Seleccione una opción: ''',
    'menu_producto_admin' : '''
    Menú Productos
    1. Buscar producto
    2. Nuevo producto
    3. Editar producto
    4. Añadir existencias
    5. Ver productos disponibles
    6. Ver lista de compras
    7. <-Atras
    Seleccione una opción: ''',
    'menu_producto_user' : '''
    Menú Productos
    1. Buscar producto
    2. <-Atras
    Seleccione una opción: ''',
    'menu_receta_chef' : '''
    Menú Receta
    1. Buscar receta
    2. Nueva receta
    3. Editar receta
    4. Activar/Desactivar receta
    5. Ver recetas activas/inactivas
    6. <-Atras
    Seleccione una opción: ''',
    'menu_receta_admin' : '''
    Menú Receta
    1. Buscar receta
    2. Nueva receta
    3. Editar receta
    4. Activar/Desactivar recetas
    5. Ver recetas activas/inactivas
    6. <-Atras
    Seleccione una opción: ''',
    'menu_receta_user' : '''
    Menú Receta
    1. Receta activa/inactivas
    2. <-Atras
    Seleccione una opción: ''',
    'opcionesDetalleReceta1':'''
    Opciones Detalle Receta
    1. Agregar Detalle
    2. Terminar Detalle
    ''',
    'producto':'''
    Agregar producto
    ''',
    'cantidad':'''
    Agregar cantidad
    ''',
    'codigo':'''
    Codigo receta
    ''',
    'receta':'''
    Receta a la cual se desea meter el detalle
    ''',
    'Receta_Agregada':'''
    Agregado correctamente
    Presiona enter para continuar...
    ''',
    'estado':'''
    Si desea que la receta este activa ingrese 1
    Si desea que no este activa ingrese 0
    ''',
    'opciones_activar_desactivar':'''
    1. Desactivar
    2. Acivar
    3. <-Atras 
    ''',
    'opcionesVerReceta1':'''
    1. Buscar receta por codigo
    2. Buscar reteta por nombre
    3 <- Atras
    ''',
    'opcionesVerTodasRecetas':'''
    1. Ver recetas activas
    2. Ver recetas inactivas
    3. <- Atras
    ''',
    'opciones_activar_receta':'''
    1. Activar por codigo
    2. Activar por nombre
    3. <- Atras    
    ''',
    'opciones_desactivar_receta':'''
    1. Desactivar por codigo
    2. Desactivar por nombre
    3. <- Atras
    ''',    
    'editar_receta': '''
    Editar Receta
    1. Editar Nombre
    2. Editar Tiempo de Preparacion
    3. Editar Detalle Receta
    4. <- Atras
    ''',
    'editar_DetalleReceta1': '''
    Editar Detalle Receta
    1. Editar cantidad
    2. Eliminar detalle
    3. <- Atras
    ''',
    'agregar_d_receta_producto':'''
    Producto
    1. Ver productos
    2. Agregar Producto
    3. <- Atras
    ''',
    'codigo_detalle':'''
    Codigo del detalle que deseo eliminar
    ''',
    'cod_rece_edit':'''
    codigo de receta que deseo editar
    ''',
    'cod_producto':'''
    Codigo producto
    ''',
    'producto_opcion_no_valida':'''
    No valida
    ''',    
    'menu_pedio_chef' : '''
    Menú Pedido
    1. ver pedidos a mi cargo
    2. Buscar pedidos
    3. Editar pedido
    4. Eliminar Pedido
    5. Tomar pedido
    6. <-Atras
    Seleccione una opción: ''',
    'menu_pedio_admin' : '''
    Menú Pedido
    1. ver mis pedidos
    2. Buscar pedidos
    3. Nuevo Pedido
    4. Editar pedido
    5. Eliminar Pedido
    6. Tomar pedido
    7. <-Atras
    Seleccione una opción: ''',
    'menu_pedio_user' : '''
    Menú Pedido
    1. ver mis pedidos
    2. Nuevo Pedido
    3. <-Atras
    Seleccione una opción: ''',
    'user_duplicated' : 'Usuario existente',
    'chef_duplicated' : 'Chef existente',
    'edit_my_user' : '''
    Modificar:
    1. Nombre
    2. Contraseña
    3. Fecha nacimiento
    4. <-Atras
    Seleccione una opción: ''',
    'old_password' : 'Ingrese la vieja contraseña: ',
    'new_password' : 'Ingrese la nueva contraseña: ',
    'wrong_password' : 'Contraseña incorrecta',
    'status' : '''
    Cambiar estado:
    1. Activar
    2. Desactivar
    Seleccione una opción: ''',
    'status_inactive' : '''
    Esta seguro de querer desactivar su usuario?
    1. Si
    2. No
    Seleccione una opción: ''',
    'login_way' : '''
    Iniciar como:
    1. Usuario
    2. Chef
    Seleccione una opción: ''',
    'search_chef' : '''
    Buscar chef por:
    1. email
    2. Nombre
    3. <-Atras
    Seleccione una opción: ''',
    'chef_not_found' : 'Chef no encontrado',
    'chef_promote' : '''
    ¿Esta seguro de querer promover al usuario?
    1. Si
    2. No
    Seleccione una opción: ''',


    'ver_producto' : '''
    1. Buscar producto por código
    2. Buscar producto por nombre
    3. <-Atras
    ''',
    'codigoP': 'Ingrese el código del producto: ',
    'nombreP': 'Ingrese el nombre del producto: ',
    
    'agregar_producto_1' : 'Ingrese el nombre del producto: ',
    'agregar_producto_2' : 'Ingrese la cantidad de este producto (SÓLO LA CANTIDAD): ',
    'agregar_producto_3' : 'Ingrese la forma de medición de este producto (KG, L, U(Unidades)): ',
    'agregar_producto_5' : '¿este producto estará disponible? Ingrese una opción: ',
    
    'disponibilidad_p' : '''
    El producto estará disponible, ingrese una opción:
    1. Sí
    2. No
    ''',

    'producto_agregado' : 
    '''Producto agregado correctamente, presione enter para continuar... ''',

    'buscar_prod_c' : '#   Codigo   Nombre ',

    'prod_disponibles': 'Código   Nombre',

    'prod_a_comprar' : 'Código  Nombre  Cantidad actual',

    'prod_suficientes' : 'Actualmente la cantidad de productos en el almacen es suficiente',

    'seleccionar_producto': '''
    Para modificar la cantidad de un producto 
    primero debe seleccionarlo, 
    por favor ingrese el código
    del producto. : 

    ''',

    'cambiar_cantidad_p': '''
    Ingrese la opción:
    1. Agregar Cantidad
    2. Restar cantidad
    3. <- Atrás
    ''',
    'agregar_cantidad_p': 'Ingrese la cantidad que desea agregar: ',
    'restar_cantidad_p': 'Ingrese la cantidad que desea restar: ',

    'editar_producto': '''
    ¿Qué desea editar del producto? Seleccione una opción:

    1. Editar nombre
    2. Editar cantidad
    3. Cambiar estado
    4. Cambiar medición
    5. <- Atrás
    ''',

    'editar_nombre_p' : 'Ingrese el nuevo nombre para el producto: ',
    'editar_cantidad_p' : 'Ingrese la nueva cantidad: ',

    'cambiar_estado_p': '''
    1. Activar producto
    2. Desactivar producto
    3. <- Atrás
    ''',
    'cambiar_medicion_p' : 'Ingrese la nueva medición del producto (KG, L o Unidades): ',



    'ver_lista_compra' : '',

    'menu_calificacion': '''
    Menú Calificaciónes
    1. Ver calificación
    2. Agregar calificación
    3. Modificar calificación
    4. Eliminar calificación
    5. <-Atras
    ''',
        
    'menu_receta': '''
    Menu Receta
    1. Ver Receta
    2. Agregar Receta
    3. Editar Receta
    4. Eliminar Receta
    5. Editar Calificacion
    6. Eliminar Calificacion
    7. <- Atras
    ''',
    
    'opcionesDetalleReceta':'''
    Opciones Detalle Receta
    1. Agregar Detalle
    2. <- Atras
    ''',
        
    'editar_receta': '''
    Editar Receta
    1. Editar Nombre
    2. Editar Tiempo de Preparacion
    3. Editar Detalle Receta
    4. <- Atras
    ''',
        
    'editar_DetalleReceta': '''
    Editar Detalle Receta
    1. Editar Cantidad
    2. Eliminar Producto
    3. <- Atras
    ''',
    'opcion' : 'Ingrese una opcion: ',
    'id' : 'Digite el numero de identificación: ',
    'userNotFound' : 'Usuario no encontrado',
    'formatoUsuario' : '''
    Tipo usuario: %s
    Nombre: %s
    Identificación: %d
    Fecha nacimiento: %s
    ''',
    'formatoProducto' : '''
    Código: %s
    Nombre: %s
    Cantidad: %s %s
    Estado: %s
    ''',
    'nombre' : 'Digite el nombre: ',
    'idFound' : 'Identificación existente',
    'opcionesVerReceta' : '''
    1. Buscar por código
    2. <-Atras
    ''',
    'tiempo' : 'Ingrese el tiempo de preparacion: ',
    'opcionesDetalleReceta' :'''
    1. Agregar Ingrediente
    2. Editar Ingrediente
    3. 

    ''',
    'pedido_chef':'''
    Menu Pedido Chef
    1. Ver Pedidos
    2. Elegir Pedido Sin Entregar
    3. <- Atras
    Seleccione una opción: ''',

    'pedido_admin':'''
    Menu Pedido Admin
    1. Ver Pedidos
    2. Editar Pedido
    3. Eliminar Pedido 
    4. <- Atras
    Seleccione una opción: ''',

    'pedido_user':'''
    Menu Pedido Usuario
    1. Ver Pedidos
    2. Agregar Pedido
    3. <- Atras
    Seleccione una opción: ''',

    'set_chef_pedido':'''
    Menu elegir pedido sin entregar
    1. Elegir primer pedido encontrado
    2. Elegir por fecha
    3. <- Atras 
    Seleccione una opción: ''',

    'ver_solo_codigo':'''
    Tus Pedidos
    1. Ver codigos de tus pedidos
    2. Ver detalles de tus pedidos (Codigo del pedido necesario)
    3. <- Atras
    Seleccione una opción: ''',

    'eliminar_pedido':'''
    Eliminar Pedido
    1. Eliminar por codigo
    2. Eliminar ultimo pedido
    3. Eliminar todos los pedidos
    4. <- Atras
    Seleccione una opción: ''',

    'editar_pedido':'''
    Editar Pedido
    1. Buscar por codigo
    2. <- Atras
    Seleccione una opción: ''',

    'editar_p_o_r':'''
    Editar Pedido
    1. Editar Receta
    2. Editar Producto
    Seleccione una opción: ''',

    'editar_por_codigo_rec':'''
    Editar Receta 
    1. Ver recetas del pedido
    2. Editar receta por su codigo
    Seleccione una opción: ''',

    'detalle_editar_receta':'''
    Introducir codigo de la nueva receta: ''',

    'editar_por_codigo_prod':'''
    Editar Producto
    1. Ver productos del pedido
    2. Editar producto por su codigo
    Seleccione una opción: ''',

    'detalle_editar_producto':'''
    Introducir codigo del nuevo producto: ''',

    'pedido_editar_cant':'''
    Editar Cantidad: ''',

    'pedido_editar_desc':'''
    Editar Descripcion: ''',
    'ped_rec_edit':'Receta Editada Correctamente... ',
    'ped_prod_edit':'Producto Editado Correctamente... ',
    'ped_edit':'Pedido Editado Correctamente...',
    'pedido_eliminado':'Pedido(s) eliminado(s) correctamente... ',
    'pedidos_false_not_found':'''No se encontraron pedidos (No entregados)... 
    ''',
    'pedido_opcion_no_valida':'''Opción no valida, seleccione opcion correcta...
    ''',
    'code_not_found':'''
    Codigo no valido...
    ''',
    'pedido_rp_agregado':'''
    Agregado corretamente...
    ''',

    'pedidos_not_found':'No se encontraron pedidos, agregue alguno primero...',
    'agregar_pedido_2':'''
    ?. Ayuda
    Inserte descripción del pedido: ''',
    'pedido_ayuda_des':'''
    Información adicional sobre tus pedidos, por ejemplo, "No agregar sal"
    Si no quieres agregar ninguna, escribe: "Sin descripcion"... ''',
    'agregar_pedido_3':'Inserte usuario del pedido: ',

    'agregar_detalle_pedido':'''
    Agregar Productos o Recetas (Detalle de Pedido)
    1. Agregar Producto
    2. Agregar Receta
    3. -> Terminar
    Seleccione una opción: ''',

    'agregar_d_pedido_2':'''
    Inserte cantidad:  ''',

    'agregar_d_pedido_3':'''
    Inserte receta: 
    1. Ver recetas disponibles
    2. Elegir por codigo
    3. -> Continuar 
    Seleccione una opción: ''',

    'pedido_code':'''
    Inserte codigo: ''',
    'receta_not_found': 'No se encontro receta...',
    'producto_not_found': 'No se encontro producto...',

    'agregar_d_pedido_5':'''
    Inserte producto
    1. Ver productos disponibles
    2. Elegir producto por codigo
    3. -> Continuar
     ''',
    
    'pedido_agregado':'''
    Pedido Agregado Correctamente, Presione enter para continuar...''',
    

    'pedido_fecha_d':'Inserte dia: ',
    'pedido_fecha_m':'Inserte mes: ',
    'pedido_fecha_a':'Inserte año: ',
    'pedido_fecha_h':'Inserte hora: ',
    'pedido_fecha_min':'Inserte minuto: ',
    'pedido_fecha_s':'Inserte segundo: ',
    'editar_pedido_2':'''
    Inserte valores a editar: 

    ''',
    'fecha_not_found':'Fecha no encontrada, presione enter para continuar...'
    }


    english = {
    'menu' : '''
    Menu
    1. Menu Users
    2. Menu Chefs
    3. Menu Ratings
    4. Menu Data
    5. Menu Language
    6. Exit
    ''',
    'menu_usuario' : '''
    Menu Users
    1. View user
    2. Add user
    3. Update user
    4. Delete user
    5. <-Back
    ''',
    'menu_chef' : '''
    Menu Chefs
    1. View chef
    2. Add chef
    3. Update chef
    4. Delete chef
    5. <-Back
    ''',
    'menu_calificacion' : '''
    Menu Ratings
    1. View rating
    2. Add rating
    3. Update rating
    4. Delete rating
    5. <-Back
    ''',
        
    'menu_receta': '''
    Menu Recipe
    1. View Recipe
    2. Add Recipe
    3. Update Recipe
    4. Delete Recipe
    5. Update Rating
    6. Delete Rating
    7. <- Back
    ''',
    
    'opcionesDetalleReceta':'''
    Recipe Detail Options
    1. Add Detail
    2. <- Back
    ''', 
    
    'editar_receta': '''
    Edit Recipe
    1. Edit Name
    2. Edit Preparation Time
    3. Edit recipe detail
    4. <- Back
    ''',
        
    'editar_DetalleReceta': '''
    Edit Recipe Detail
    1. Edit Quantity
    2. Delete Product
    3. <- Back
    ''',    
        
    'menu_datos' : '''
    Menu Data
    1. Add ficticious data
    2. <-Back
    ''',
    'menu_idioma' : '''
    Menu Languages
    1. Change Language
    2. <-Back
    ''',
    'opcion' : 'Enter an option: ',
    'opcionNoValida' : '{0} is not a correct option',
    'salir' : 'Bye Bye',
    'id' : 'Enter the identification number: ',
    'userNotFound' : 'User not found',
    'formatoUsuario' : '''
    User type: %s
    Name: %s
    identification: %d
    Born date: %s
    ''',
    'formatoProducto' : '''
    Code: %s
    Name: %s
    Quantity: %d %s
    Required: %s
    ''',
    'nombre' : 'Enter the name: ',
    'fecha_nac' : 'Enter the born date(dd/mm/yyyy): ',
    'contrasena' : 'Enter the password: ',
    'idFound' : 'Identification found',
    'editar_usuario' : '''
    Options
    1. Change name
    2. Change born date
    3. Change password
    4. <-Back
    ''',
    'oldContrasena' : 'Enter the old password: ',
    'newContrasena' : 'Enter the new password: ',
    'wrongContrasena' : 'Wrong password',
    'yesNo' : '''
    Are you sure?
    1. Yes
    2. No
    ''',
    'opcionesVerReceta' :'''
    1. Search by code
    2. Search by name
    3. <-Back
    ''',
    'tiempo': 'Enter the preparation time: '
    }
    
