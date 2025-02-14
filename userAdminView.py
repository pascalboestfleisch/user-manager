class UserAdminView:

    @staticmethod
    def display_menu():
        print("1. Login")
        print("2. Register")
        print("3. Update password")
        print("4. Show all users when logged in")
        print("5. Exit")

    @staticmethod
    def get_user_input() -> int:
        try:
            return int(input("Input your prefered action: "))
        except ValueError:
            return -1

    @staticmethod
    def get_username_input() -> str:
        return input("Insert username: ").strip()

    @staticmethod
    def get_password_input() -> str:
        return input("Insert password: ").strip()

    @staticmethod
    def get_password_changed() -> str:
        return input("Input new password: ").strip()

    @staticmethod
    def get_all_users(users):
        print("Registered users")
        for user in users:
            print(f"- {user}")
