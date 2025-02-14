import random
import psycopg2
import bcrypt


class UserAdminDB:

    logged_in_user = None

    @staticmethod
    def connect():
        return psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432",
        )

    @staticmethod
    def check_username(username: str) -> int:
        conn = UserAdminDB.connect()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM passwd WHERE user_name = %s", (username,))
        count = cur.fetchone()[0]
        cur.close()
        conn.close()
        return count

    @staticmethod
    def hash_password(password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()

    @staticmethod
    def verify_password(entered_password: str, stored_hash: str) -> bool:
        return bcrypt.checkpw(entered_password.encode(), stored_hash.encode())

    @staticmethod
    def login(username: str, password: str) -> bool:
        conn = UserAdminDB.connect()
        cur = conn.cursor()
        cur.execute("SELECT password FROM passwd WHERE user_name = %s", (username,))
        result = cur.fetchone()

        if result:
            stored_hash = result[0]
            if UserAdminDB.verify_password(password, stored_hash):
                UserAdminDB.logged_in_user = username
                cur.close()
                conn.close()
                return True

        cur.close()
        conn.close()
        return False

    @staticmethod
    def insert_user(username: str, password: str):
        conn = UserAdminDB.connect()
        cur = conn.cursor()
        # Random int for simplicity reasons, UUID prefered
        user_id = random.randint(3, 99999999999)
        hashed_password = UserAdminDB.hash_password(password)

        cur.execute(
            "INSERT INTO passwd (id, user_name, password, date, date_upd) VALUES (%s, %s, %s, NOW(), NOW())",
            (user_id, username, hashed_password),
        )

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def update_user(username: str, password: str):
        conn = UserAdminDB.connect()
        cur = conn.cursor()
        hashed_password = UserAdminDB.hash_password(password)

        cur.execute(
            "UPDATE passwd SET password = %s, date_upd = NOW() WHERE user_name = %s",
            (hashed_password, username),
        )

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def select_all_users():
        if UserAdminDB.logged_in_user:
            conn = UserAdminDB.connect()
            cur = conn.cursor()
            cur.execute("SELECT user_name FROM passwd")
            users = [row[0] for row in cur.fetchall()]
            cur.close()
            conn.close()
            return users
        else:
            print("You have to be logged in to perform this action!")
            return []
