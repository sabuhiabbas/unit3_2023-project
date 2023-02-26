# login.py
import sqlite3
import random

from email_validator import validate_email, EmailNotValidError
from passlib.context import CryptContext

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
                          default="pbkdf2_sha256",
                          pbkdf2_sha256__default_rounds=30000
                          )

testEmail = "examplestackabuse.com"


def hash_password(user_password):
    return pwd_config.hash(user_password)

def check_password(hashed_password, user_password):
    return pwd_config.verify(user_password, hashed_password)

class database_handler_login_signup(MDApp):
    def __init__(self, namedb: str):
        self.connection = sqlite3.connect(namedb)
        self.cursor = self.connection.cursor()

    def create_table(self):
        query = f"""CREATE TABLE if not exists users(
            id INTEGER PRIMARY KEY not NULL,
            email text not NULL unique,
            password text not NULL,
            username text not NULL unique
            )"""
        self.run_query(query)

    def run_query(self, query: str):
        # This function runs a console query
        self.cursor.execute(query)
        self.connection.commit()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def close(self):
        # This function is to close a database
        self.connection.close()

    def insert(self, email, username, password):
        """
        This function is to insert new user information to the
        database
        :param email: string
        :param password: string
        :param username: string
        :return:
        """
        query = f"INSERT into users (email, password, username) VALUES ('{email}', '{password}', '{username}')"
        self.run_query(query)


class LoginScreen(MDScreen):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

    def try_login(self):
        email_entered = self.ids.email_in.text
        pass_entered = self.ids.passwd_in.text

        if email_entered == "":
            self.ids.email_in.error = True

        if pass_entered == "":
            self.ids.passwd_in.error = True

        else:
            db = database_handler_login_signup(namedb="unit3_project_database.db")
            query = f"SELECT password FROM users WHERE email = '{email_entered}'"
            result = db.search(query)
            if len(result) == 1:
                if check_password(result[0][0], pass_entered):
                    print(f"Login successfull")
                    self.parent.current = "HomeScreen"
                else:
                    print("Try again")
            else:
                print("Try again")


    def toggle_show_password(self):
        self.show_password = not self.show_password
        self.ids.passwd_in.password = not self.show_password

    def build(self):
        return


class SignupScreen(MDScreen):
    def try_cancel(self):
        self.parent.current = "LoginScreen"

    def try_register(self):
        passwd1 = self.ids.e_passwd.text
        passwd2 = self.ids.c_passwd.text
        if passwd1 != passwd2:
            self.ids.e_passwd.error = True
            self.ids.c_passwd.error = True
        else:
            db.insert(email=self.ids.email.text, username=self.ids.uname.text,
                      password=hash_password(self.ids.c_passwd.text))
        print("New user")

    def toggle_show_password(self):
        self.show_password = not self.show_password
        self.ids.e_passwd.password = not self.show_password
        self.ids.c_passwd.password = not self.show_password

class HomeScreen(MDScreen):
    def try_logout(self):
        print("User trying logging out")
        self.parent.current = "LoginScreen"

    def build(self):
        return

class unit3_project(MDApp):
    def build(self):
        return

db = database_handler_login_signup(namedb="unit3_project_database.db")
db.create_table()

test = unit3_project()
test.run()

db.close()
