from mensajes import Mensajes

class Usuario:

    ListUsuarios = {}

    def __init__(
            self, admin, email, 
            name, password, born_date):
        '''ATTRIBUTES
            self._admin
            self._email
            self._name
            self._password
            self._born_date
            self._status
        '''
        self._ListCalificaciones = {}
        self._ListPedidos = {}
        self.set_admin(admin)
        self.set_email(email)
        self.set_name(name)
        self.set_password(password)
        self.set_born_date(born_date)
        self.set_status(True)
        Usuario.ListUsuarios[email] = self

    def set_admin(self, admin):
        self._admin = admin

    def get_admin(self):
        return self._admin

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_email(self, email):
        self._email = email

    def get_email(self):
        return self._email

    def set_born_date(self, born_date):
        self._born_date = born_date

    def get_born_date(self):
        return self._born_date

    def set_password(self, password):
        self._password = password

    def get_password(self):
        return self._password
    
    def set_status(self, status):
        self._status = status
            
    def get_status(self):
        return self._status

    def set_calificaciones(self, calificacion):
        self._ListCalificaciones[calificacion.get_codigo()] = calificacion

    def set_promote_calificaciones(self, calificaciones):
        for calificacion in calificaciones:
            calificacion.set_usuario(self)

    def get_calificaciones(self):
        return self._ListCalificaciones

    def set_pedidos(self, pedido):
        self._ListPedidos[pedido.get_codigo()] = pedido

    def set_promote_pedidos(self, pedidos):
        for pedido in pedidos:
            pedido.set_usuario(self)

    def get_pedidos(self):
        return self._ListPedidos

    def __str__(self):
        admin = self.get_admin()
        if admin:
            admin = Mensajes.men.get('yes')
        else:
            admin = Mensajes.men.get('no')
        name = self.get_name()
        email = self.get_email()
        born_date = self.get_born_date()
        status = self.get_status()
        if status:
            status = Mensajes.men.get('active')
        else:
            status = Mensajes.men.get('inactive')
        Str = Mensajes.men.get('str_user') % (
                admin, name, email, 
                born_date, status)
        return Str

    @staticmethod
    def get_user_by_email(email):
        return Usuario.ListUsuarios.get(email)

    @staticmethod
    def check_login(email, password):
        user = Usuario.get_user_by_email(email)
        if user is not None:
            if user.get_status():
                if user.get_password() == password:
                    return user
        return None

    @staticmethod
    def get_user_by_name(name):
        ListCoincidencias = []
        for user in Usuario.ListUsuarios.values():
            if user.get_name().lower().find(name.lower()) != -1:
                ListCoincidencias.append(user)
        return ListCoincidencias