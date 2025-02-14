import userAdminDb
from string import ascii_lowercase, digits
from random import choice
from tabulate import tabulate


def generate_random_string():
    return "".join(choice(ascii_lowercase + digits) for i in range(8))


random_username = generate_random_string()
random_password = generate_random_string()
new_random_password = generate_random_string()


user_list = []

# Smple insertion tests
userAdminDb.UserAdminDB.insert_user(random_username, random_password)
userAdminDb.UserAdminDB.update_user(random_username, new_random_password)
login_success = userAdminDb.UserAdminDB.login(random_username, new_random_password)
user_list = userAdminDb.UserAdminDB.select_all_users()


print(f"Login erfolgreich: {login_success}")
print(
    tabulate(
        [[i + 1, user] for i, user in enumerate(user_list)], headers=["#", "Benutzer"]
    )
)
