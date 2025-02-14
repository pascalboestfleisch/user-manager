from userAdminModel import UserAdminModel
from userAdminView import UserAdminView


def main():
    while True:
        UserAdminView.display_menu()
        choice = UserAdminView.get_user_input()

        if choice == 1:  # Login
            username = UserAdminView.get_username_input()
            password = UserAdminView.get_password_input()
            user = UserAdminModel(username, password)
            if user.login():
                print("Login successfull!")
            else:
                print("Invalid password or username!")

        elif choice == 2:  # Register
            username = UserAdminView.get_username_input()
            password = UserAdminView.get_password_input()
            user = UserAdminModel(username, password)
            if user.check_user():
                print("User already exists!")
            else:
                user.insert_user()
                print("User registered successfully!")

        elif choice == 3:  # Update Password
            username = UserAdminView.get_username_input()
            new_password = UserAdminView.get_password_changed()
            user = UserAdminModel(username, "")
            if user.check_user():
                user.update_user(new_password)
                print("Password change was successful.")
            else:
                print("User doesn't exist!")

        elif choice == 4:  # show all users
            users = UserAdminModel.select_all_users()
            UserAdminView.get_all_users(users)

        elif choice == 5:  # Stop program
            print("Program stopped!")
            break

        else:
            print("Only input numbers 1-5!")


if __name__ == "__main__":
    main()
