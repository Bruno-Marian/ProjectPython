class Conect:

    def __init__(self, db_name, host, port, user, password):
        self.__db_name = db_name
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password

    @property
    def db_name(self):
        return self.__db_name

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    @db_name.setter
    def db_name(self, value):
        self.db_name = value

    @host.setter
    def host(self, value):
        self.host = value

    @port.setter
    def port(self, value):
        self.port = value

    @user.setter
    def user(self, value):
        self.user = value

    @password.setter
    def password(self, value):
        self.password = value

