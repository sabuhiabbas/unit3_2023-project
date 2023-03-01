# unit3_project.py
import sqlite3

from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from passlib.context import CryptContext

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from datetime import datetime

pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
                          default="pbkdf2_sha256",
                          pbkdf2_sha256__default_rounds=30000
                          )

# Function to hash a password
def hash_password(user_password):
    return pwd_config.hash(user_password)

# Function to check if a password matches a hash
def check_password(hashed_password, user_password):
    return pwd_config.verify(user_password, hashed_password)

# Class for handling login and signup database operations
class database_handler_login_signup(MDApp):
    def __init__(self, namedb: str):
        self.connection = sqlite3.connect(namedb)
        self.cursor = self.connection.cursor()

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    # Create the users table if it doesn't exist
    def create_table(self):
        query = f"""CREATE TABLE if not exists users(
            id INTEGER PRIMARY KEY not NULL,
            email text not NULL unique,
            password text not NULL,
            username text not NULL unique
            )"""
        self.run_query(query)

    # Function to execute a console query
    def run_query(self, query: str):
        self.cursor.execute(query)
        self.connection.commit()

    # Function to search the database
    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    # Function to close the database
    def close(self):
        self.connection.close()

    # Function to insert a new user into the database
    def insert(self, email, username, password):
        query = f"INSERT into users (email, password, username) VALUES ('{email}', '{password}', '{username}')"
        self.run_query(query)

# Class for handling item database operations
class database_handler_items(MDApp):
    def __init__(self, namedb: str):
        self.connection = sqlite3.connect(namedb)
        self.cursor = self.connection.cursor()

    # Create the items table if it doesn't exist
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

    # Function to execute a console query
    def run_query(self, query: str):
        self.cursor.execute(query)
        self.connection.commit()

    # Function to search the database
    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    # Function to close the database
    def close(self):
        self.connection.close()

    # Function to insert a new item into the database
    def insert(self, customer_id, date, item, size, item_id):
        query = f"INSERT into items (customer_id, date, item, size, item_id) VALUES ('{customer_id}', '{date}', '{item}', '{size}', '{item_id}')"
        self.run_query(query)

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

class LoginScreen(MDScreen):
    # Define the __init__ method that initializes the object
    def __init__(self, **kwargs):
        # Call the parent class's __init__ method with any keyword arguments
        super(LoginScreen, self).__init__(**kwargs)

    # Define a method that handles login attempts
    def try_login(self):
        # Get the email and password entered by the user
        email_entered = self.ids.email_in.text
        pass_entered = self.ids.passwd_in.text

        # Check if the email and password fields are empty
        if email_entered == "":
            # Set the error flag for the email field to True
            self.ids.email_in.error = True

        if pass_entered == "":
            # Set the error flag for the password field to True
            self.ids.passwd_in.error = True

        else:
            # Create a database handler object
            db = database_handler_login_signup(namedb="unit3_project_database.db")
            # Create a query to select the password associated with the email entered
            query = f"SELECT password FROM users WHERE email = '{email_entered}'"
            # Execute the query and get the result
            result = db.search(query)
            # Check if there is exactly one result
            if len(result) == 1:
                # Check if the entered password matches the one in the database
                if check_password(result[0][0], pass_entered):
                    # If the passwords match, print a success message, switch to the HomeScreen, and clear the email and password fields
                    print(f"Login successfull")
                    self.parent.current = "HomeScreen"
                    self.ids.email_in.text = ""
                    self.ids.passwd_in.text = ""
                else:
                    # If the passwords don't match, print a message asking the user to try again
                    print("Try again")
            else:
                # If there is no result or more than one result, print a message asking the user to try again
                print("Try again")

    # Define a method that switches to the SignupScreen and clears the email and password fields
    def try_signup(self):
        self.parent.current = "SignupScreen"
        self.ids.email_in.text = ""
        self.ids.passwd_in.text = ""

    # Define a method that toggles the visibility of the password field
    def toggle_show_password(self):
        # Invert the value of the show_password attribute
        self.show_password = not self.show_password
        # Set the password attribute of the password field to the opposite of the show_password attribute
        self.ids.passwd_in.password = not self.show_password

    # Define the build method that returns None
    def build(self):
        return None

class SignupScreen(MDScreen):
    def try_cancel(self):
        # Change the current screen to LoginScreen and clear all the fields.
        self.parent.current = "LoginScreen"
        self.ids.e_passwd.text = ""
        self.ids.c_passwd.text = ""
        self.ids.uname.text = ""
        self.ids.email.text = ""

    def try_register(self):
        # Get the passwords entered by the user.
        passwd1 = self.ids.e_passwd.text
        passwd2 = self.ids.c_passwd.text

        # Check if the two passwords match. If not, set the error flag on both fields.
        if passwd1 != passwd2:
            self.ids.e_passwd.error = True
            self.ids.c_passwd.error = True
        else:
            # Insert the new user into the database and change the current screen to LoginScreen.
            db.insert(email=self.ids.email.text, username=self.ids.uname.text,
                      password=hash_password(self.ids.c_passwd.text))
            print("New user")
            self.parent.current = "LoginScreen"
            self.ids.e_passwd.text = ""
            self.ids.c_passwd.text = ""
            self.ids.uname.text = ""
            self.ids.email.text = ""


    def toggle_show_password(self):
        # Toggle the show_password flag and update the password visibility of both fields.
        self.show_password = not self.show_password
        self.ids.e_passwd.password = not self.show_password
        self.ids.c_passwd.password = not self.show_password

class HomeScreen(MDScreen):

    # Function to log out the user
    def try_logout(self):
        print("User trying logging out")
        self.parent.current = "LoginScreen"

    # Function to add a new item
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

    def try_submit(self):
        # Create a database handler object
        db_items = database_handler_items(namedb="unit3_project_database.db")
        # Insert the new item into the database
        db_items.insert(self.ids.customer_id.text, self.ids.date.text, self.ids.item.text, self.ids.size.text, self.ids.item_id.text)
        print("Item added")

        # Create and open the alert dialog to confirm item has been added
        dialog = MDDialog(title="Thank you, item added!", text=f"Your item ID: {self.ids.item_id.text} has been successfully added.")
        dialog_buttons = [MDFlatButton(text="OK", on_release=dialog.dismiss, md_bg_color=[1, 1, 1, 1])]
        dialog.buttons = dialog_buttons
        dialog.open()

        # Clear the input fields and switch to HomeScreen
        self.ids.customer_id.text = ""
        self.ids.date.text = ""
        self.ids.item.text = ""
        self.ids.size.text = ""
        self.ids.item_id.text = ""
        self.parent.current= 'HomeScreen'

    def try_cancel(self):
        # Clear the input fields and switch to HomeScreen
        self.parent.current = 'HomeScreen'
        self.ids.customer_id.text = ""
        self.ids.date.text = ""
        self.ids.item.text = ""
        self.ids.size.text = ""
        self.ids.item_id.text = ""

    def build(self):
        return

class BorrowedItemsScreen(MDScreen):
    # class_variable
    data_table = None

    def update(self):
        # Read the database and update the table
        db = database_handler_items("unit3_project_database.db")
        query = "SELECT customer_id, date, item, size, item_id from items"
        data = db.search(query)
        print(data)
        db.close()
        self.data_table.update_row_data(None, data)

    def delete(self):
        # Function to delete checked rows in the table
        checked_rows = self.data_table.get_row_checks()
        print(checked_rows)
        # delete
        db = database_handler_items("unit3_project_database.db")
        for r in checked_rows:
            item_id = r[4]  # use item_id instead of id
            print(item_id)
            query = f"delete from items where item_id = {item_id}"  # use item_id instead of id
            print(query)
            db.run_save(query)
            # Create and open the alert dialog to confirm item has been deleted
            dialog = MDDialog(title="Thank you, item deleted!",
                              text=f"Your item ID: {item_id} has been successfully deleted.")
            dialog.open()
        db.close()
        self.update()

    def on_pre_enter(self, *args):
        # Code to run before the screen is created
        self.data_table = MDDataTable(
            size_hint=(.9, .75),
            pos_hint={"center_x": .5, "center_y": .5},
            use_pagination=True,
            check=True,
            background_color = "#689ebd",
            # Title of the columns
            column_data=[("Customer ID", 40),
                         ("Date", 25),
                         ("Kind", 30),
                         ("Item ID", 20),
                         ("Size", 50)]
        )

        # Add functions for events of the mouse
        self.data_table.bind(on_check_press=self.check_pressed)
        self.add_widget(self.data_table)  # Add the table to the GUI
        self.update()

    def check_pressed(self, table, current_row):
        # Function to handle when a check mark is pressed
        print("a check mark was pressed", current_row)

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
