# unit3_project.py
import sqlite3

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from passlib.context import CryptContext

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from datetime import datetime

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

class database_handler_items(MDApp):
    def __init__(self, namedb: str):
        self.connection = sqlite3.connect(namedb)
        self.cursor = self.connection.cursor()

    def create_table(self):
        query = f"""CREATE TABLE if not exists items(
            id INTEGER PRIMARY KEY not NULL,
            customer_id int,
            date text,
            item text,
            size text,
            item_id int
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

    def insert(self, customer_id, date, item, size, item_id):
        query = f"INSERT into items (customer_id, date, item, size, item_id) VALUES ('{customer_id}', '{date}', '{item}', '{size}', '{item_id}')"
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
                    self.ids.email_in.text = ""
                    self.ids.passwd_in.text = ""
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
            self.parent.current = "LoginScreen"
            self.ids.e_passwd.text = ""
            self.ids.c_passwd.text = ""
            self.ids.uname.text = ""
            self.ids.email.text = ""


    def toggle_show_password(self):
        self.show_password = not self.show_password
        self.ids.e_passwd.password = not self.show_password
        self.ids.c_passwd.password = not self.show_password

class HomeScreen(MDScreen):
    def try_logout(self):
        print("User trying logging out")
        self.parent.current = "LoginScreen"

    def try_newitem(self):
        print("Trying adding new item")
        self.parent.current = 'NewitemScreen'

    def build(self):
        return

class NewitemScreen(MDScreen):
    input_format = "%d-%m-%Y"

    def validate_date(self, text):
        """
        Validate the entered date
        """
        # Check if the entered text is a valid date in the specified format
        try:
            datetime.strptime(text, self.input_format)
            print("Valid date entered!")
        except ValueError:
            self.ids.date.error = True

    def validate_customer_id(self, text):
        """
        Validate the customer ID entered in the customer_id MDTextField.
        """
        try:
            customer_id = int(text)
        except ValueError:
            self.ids.customer_id.error = True

    def validate_size(self, text):
        """
        Validate the size entered in "size" MDTextField.
        """
        try:
            size = float(text)
        except ValueError:
            self.ids.size.error = True

    def validate_item_id(self, text):
        """
        Validate the item ID entered in the item_id MDTextField.
        """
        try:
            item_id = int(text)
        except ValueError:
            self.ids.item_id.error = True

    def validate_item(self, text):
        """
        Validate the item entered in item MDTextField.
        """
        items = ["Ski", "Snowboard", "Ski shoes", "Snowboard boots", "Ski clothes", "Snowboard clothes"]
        try:
            index = items.index(text)
        except ValueError:
            self.ids.item.error = True

    def try_submit(self):
        db_items = database_handler_items(namedb="unit3_project_database.db")
        db_items.insert(self.ids.customer_id.text, self.ids.date.text, self.ids.item.text, self.ids.size.text, self.ids.item_id.text)
        print("Item added")

        # Create and open the alert dialog
        dialog = MDDialog(title="Thank you, item added!", text=f"Your item ID: {self.ids.item_id.text} has been successfully added.")
        dialog_buttons = [MDFlatButton(text="OK", on_release=dialog.dismiss, md_bg_color=[1, 1, 1, 1])]
        dialog.buttons = dialog_buttons
        dialog.open()

        self.ids.customer_id.text = ""
        self.ids.date.text = ""
        self.ids.item.text = ""
        self.ids.size.text = ""
        self.ids.item_id.text = ""
        self.parent.current= 'HomeScreen'

    def build(self):
        return

class unit3_project(MDApp):
    def build(self):
        return

db = database_handler_login_signup(namedb="unit3_project_database.db")
db.create_table()

db_items = database_handler_items(namedb="unit3_project_database.db")
db_items.create_table()

test = unit3_project()
test.run()

db.close()
db_items.close()
