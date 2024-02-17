

class SqlConfig:
    def __init__(self, host, port, user, password, db_name):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db_name = db_name

    @property
    def user_param(self):
        return self.host, self.port, self.user, self.password, self.db_name



