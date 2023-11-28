
class User:
    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._is_authenticated = False

    def authenticate(self, input_username, input_password):
        self._is_authenticated = self._name == input_username and self._password == input_password
        return self._is_authenticated

    def is_authenticated(self):
        return self._is_authenticated

    def set_authenticated(self, is_authenticated):
        self._is_authenticated = is_authenticated

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

