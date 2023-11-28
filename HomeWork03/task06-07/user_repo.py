from user import User


class UserRepository:
    def __init__(self):
        self.data: list[User] = []

    def add_user(self, user: User):
        if user is not None and not self.find_by_name(user.get_name()):
            self.data.append(user)

    def find_by_name(self, username):
        for user in self.data:
            if user.get_name() == username:
                return True
        return False
