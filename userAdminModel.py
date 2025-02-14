from userAdminDb import UserAdminDB


class UserAdminModel:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def set_username(self, username: str):
        self.username = username

    def set_password(self, password: str):
        self.password = password

    def login(self) -> bool:
        return UserAdminDB.login(self.username, self.password)

    def check_user(self) -> bool:
        return UserAdminDB.check_username(self.username) > 0

    def insert_user(self):
        UserAdminDB.insert_user(self.username, self.password)

    def update_user(self, new_password: str):
        UserAdminDB.update_user(self.username, new_password)

    @staticmethod
    def select_all_users():
        return UserAdminDB.select_all_users()
