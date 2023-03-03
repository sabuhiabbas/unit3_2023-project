# Unit 3: Ski/snowboard rental shop tracker

![image](https://user-images.githubusercontent.com/111758436/218400436-5362c306-be78-4a34-9e6d-dd300da998e9.png)
<p align='justify'>
<i>Ski / Snowboard Rental</i> - “Ski / Snowboard Rental - SNOW MONKEY RESORTS.” SNOW MONKEY RESORTS!, 29 March 2021, https://www.snowmonkeyresorts.com/activities/ski-snowboard-rental/. Accessed 13 February 2023.
</p>

# Criteria A: Planning

## Problem definition
<p align="justify">
Oswell Taiga Sakaguchi runs a ski and snowboard rental shop called "Fly Skis" in Karuizawa. They offer skis, snowboards, shoes, and clothes for rent to customers visiting the area for skiing or snowboarding. Fly Skis is known for having the best equipment, which has been great for Mr. Sakaguchi's business.
However, this has also created problems for his employees. They have recently expressed their frustration about the lack of a system to keep track of the equipment that has been rented out. This makes it difficult for them to help customers when they return the equipment, as they need to search for the receipt and confirm that all items have been returned. Some workers have even threatened to quit if the situation is not resolved.
</p>

## Proposed Solution
### Design Statement
<p align="justify">
To solve the issue of keeping track of equipment rented out at Fly Skis, a custom application can be developed using the Python programming language and the Kivy MD library for the user interface design. The choice of Python was made for several reasons, including its ease of use, large community, and wide range of libraries. It is also available on all software systems. The Kivy MD library was chosen because it provides a material design look and feel for the user interface, making it intuitive and easy to use for employees.
The data for the rental transactions will be stored using SQL. SQL is a very strong and versatile database management system. It is perfect for this kind of application because it can handle a lot of data, keep it safe with its security features, and support multiple people using it at the same time. It's really amazing what SQL can do! By using SQL to store the rental information, Fly Skis will have a robust and scalable solution for managing their equipment rentals.
With this proposed solution, Fly Skis will have a centralized, easy-to-use system for tracking equipment rentals, improving the efficiency of the rental process, and reducing frustration among employees.
</p>

### Rationale for Proposed Solution
Python is a versatile language and can be used for a wide range of applications, including web development, scientific computing, data analysis, artificial intelligence, and more. This versatility makes it a good choice for building a wide range of applications, including custom software.[^1]
Python has a large and active community of users and developers. This means that there is a wealth of resources available to help you learn the language and build your application, as well as a large pool of talented developers who can contribute to your project.[^2]
Python has a simple, intuitive syntax that makes it easy for new users to learn and for experienced developers to quickly pick up. This makes it a good choice for building applications quickly and with fewer bugs, as well as for prototyping new ideas.[^3]

One of the main advantages of using KivyMD is that it allows developers to build applications that can run on multiple platforms, including Android, iOS, and Windows. This makes it an ideal choice for those who want to reach a wide audience with their apps. KivyMD is designed to be user-friendly and intuitive, making it easy for developers of all skill levels to get started with creating their own applications. This can help to save time and effort, allowing developers to focus on creating their app's functionality and features. KivyMD offers a wide range of customization options that allow developers to tailor their apps to meet the specific needs of their users. From changing the look and feel of the interface to adding custom animations, the library offers a variety of options to make an app truly unique.[^4]

SQL is designed to handle large amounts of data efficiently, making it an ideal choice for applications that need to store and manage a large amount of information. This makes it an ideal choice for applications that need to scale as they grow, as SQL databases can be easily expanded to meet the needs of the application. SQL databases allow for the storage of structured data, which can be easily queried and manipulated. This makes it easier to find the information you need, and to perform complex data analysis tasks. SQL databases are highly reliable, and offer features such as transaction management and data integrity to ensure that the data stored in the database remains accurate and up-to-date. This makes SQL an ideal choice for applications that need to store critical data that must be maintained even in the event of a power outage or other failure.[^5]

### Success Criteria
1. The solution validates the input for items to rent, so the datatable is well-organized.
2. The application features a secure login system, enabling the user to protect their data. 
3. The user is able to input various information pertaining to the rental equipment. 
4. The solution affords the user the ability to effortlessly delete equipment records upon return. 
5. The solution hashes the signup information entered by the user when trying to sign up.
6. The user is able to log out, so the information is secure.

# Criteria B: Design

## System Diagram
![System diagram for skisnowboard rental shop tracker](https://user-images.githubusercontent.com/111758436/218088249-14279bc6-a1fe-40fd-98bb-fd0d3174b344.png)
<i>Figure 1</i> - The system diagram for the application is illustrated in Figure 1. The development of the program is achieved through the use of PyCharm and the KivyMD library. Data is stored in unit3_project_database.db, which is facilitated by the SQLite database engine. The arrows in the diagram indicate the flow of data between the various components of the application.[^16]

## Wireframe
![unit3_project_wireframe (1)](https://user-images.githubusercontent.com/111758436/218105085-c54acaf6-3e25-42ba-a799-c51b652a95ae.png)
<i>Figure 2</i> - The wireframe for the user interface is depicted in Figure 2. Upon launching the application, the user is welcomed with a login page. After successful login, the user is redirected to the homepage, where they can navigate to various pages through the buttons provided. Pressing the "Sign up" button on the login page takes the user to the sign-up page.

The homepage provides the user with four buttons, namely "new item," "borrowed items list," "log out," and "return item." Clicking on the "new item" button leads the user to the new item page where they can fill out a form to add a new item. Once the form is completed, the user can either press "save" to proceed to the thank you page or "cancel" to go back to the homepage.

The "borrowed items list" button on the homepage takes the user to a page where they can view a list of borrowed equipment. From this page, the user can go back to the homepage by clicking on the "home" button.

In the sign-up page, the user can either press "register" to complete the registration process or "login" to go back to the login page.

In the thank you page, the user is given the option to either go back to the homepage or view the list of borrowed items. Overall, the user interface is designed to be user-friendly and intuitive, making it easy for users to navigate and perform tasks.[^17]

## Flow diagram
### Flow diagram for create_table (database_handler_login_signup class)
<img src="https://user-images.githubusercontent.com/111758436/222377806-7220550d-357d-4b1c-ab3f-4902abed7a99.jpeg" alt="Flowchart_create_table" style="width:100%;height:auto;">
<p align="justify">
  <i>Figure 3</i> - The flow diagram for the create_table method of the database_handler_login_signup class is shown in Figure 3. This method is used to create a table with the name "users" that contains four columns, namely email, username, password, and user_type. This table is created only when the program is run for the first time, and if the table already exists, the method does not create a new table. The create_table method is an essential part of the database_handler_login_signup class as it sets up the necessary table for the program to function correctly.
</p>

### Flow diagram for try_login (LoginScreen class)
<img src="https://user-images.githubusercontent.com/111758436/222398513-37b6aeaf-e966-4068-9208-8692f8585dd3.jpg" alt="Flowchart_try_login" style="width:100%;height:auto;">
<p align="justify">
  <i>Figure 4</i> - The try_login method of the LoginScreen class is used to authenticate the user's login credentials. It takes in the user's email and password as input, and then retrieves the hashed password from the "users" table in the database using the get_password_from_email() method from the database_handler_login_signup class. The try_login method is a crucial part of the LoginScreen class as it ensures that only authorized users are granted access to the application's features.
</p>

### Flow diagram for on_pre_enter (BorrowedItemsScreen class)
<img src="https://user-images.githubusercontent.com/111758436/222402110-b5b4fe78-d3fd-45ea-93c2-c0abf8d55c99.jpg" alt="Flowchart_on_pre_enter" style="width:100%;height:auto;">
<p align="justify">
  <i>Figure 5</i> - The on_pre_enter method of the BorrowedItemsScreen class is a crucial function that is triggered when the user clicks the "BorrowedItemsScreen" button to view a list of borrowed items. As demonstrated in Figure 5, this method updates the displayed table each time it is run to ensure that the user is presented with the most current information from the database. on_pre_enter method of the BorrowedItemsScreen class is instrumental in providing the user with a smooth and up-to-date experience when interacting with the application.
</p>

## ER Diagram
![ER_diagram](https://user-images.githubusercontent.com/111758436/221069445-e499566c-0956-4678-8704-b0b00b32315d.jpg)
<i>Figure 6</i> - The ER diagram for the database used by the application is shown in Figure 6. The database consists of two tables, "users" and "items". The "users" table, which is located on the left side of the diagram, stores the user information, including their username, email, and password.

On the right side of the diagram, the "items" table is shown. This table is used to store data related to borrowed items, such as customer ID, date, kind, size, and item ID. Each item in the table is assigned a unique item ID to prevent a single item from being lent out to multiple customers simultaneously.[^18]

## UML Diagram
![UML_diagram](https://user-images.githubusercontent.com/111758436/222324521-c8d27aa5-3c10-43c0-9a90-05e6bdbc6e37.jpg)
<i>Figure 7</i> - The UML diagram in Figure 7 illustrates the class hierarchy used in the application. All classes are designed to inherit from the main class MDApp and MDClasses. This inheritance hierarchy is shown in the diagram, which clearly illustrates the relationships between the various classes and their properties.

In the diagram, each class is represented by a rectangle containing the class name, attributes, and methods. Arrows between the classes denote inheritance relationships, with child classes located beneath their parent classes.[^19]

## Test Plan
| Description | Type | Inputs | Outputs | 
| ----------- | ---- | ------ | ------- |
Test if signup page works	|	Functional: Integration testing	|	Press "Sign up", use "j" for all text fields. Press "Submit".	|	Should bring to login screen
Test if login page works	|	Functional: Integration testing	|	Enter "j" for email and password. Press "Login".	|	Should bring the user to Homescreen
Testing if adding new item works	|	Functional: Integration testing	|	Enter 1, 03-02-2023, Ski, 170, 10987, respectively to the fields customer_id, date, item, size, item_id. Press submit.	|	Should pop up a dialog saying that the item ID: 10987 added to the borrowed items list.
Check if code has good comments, variable and method names	|	Non-functional: Code review	|	N/A	|	The code should contain comments, good variable and method names.
Check if table shows the correct data	|	Non-functional: Load testing	|	Login, go to Borrowed Items screen.	|	The table should have the exact data as in database.

## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
1	|	Meet the client	|	Brainstorming about problem definition, design statement, and success criteria	|	30 mins.	|	2/7/2023	|	A
2	|	Write a problem definition	|	To have a clear idea on how to solve the problem and choose the best tools for the project	|	20 mins.	|	2/9/2023	|	A
3	|	Write a design statement	|	To have a better visual understanding of what is going to be in the application for the user.	|	20 mins.	|	2/9/2023	|	A
4	|	Rationale for Proposed Solution	|	To make it easier for the developer to get client's approval to start the project.	|	20 mins.	|	2/10/2023	|	A
5	|	Write Success Criteria	|	To make it easier for the developer to get client's approval to start the project.	|	20 mins.	|	2/10/2023	|	A
6	|	Draw a system diagram	|	To have a clear idea of the hardware and software requirements for the proposed solution	|	1 hour	|	2/10/2023	|	B
7	|	Meet the client	|	Having success criteria get confirmed	|	30 mins.	|	2/10/2023	|	A
8	|	Draw a wireframe and write a brief explanation	|	To better understand how different screen pages look like in the app.	|	1 hour	|	2/10/2023	|	B
9	|	Make a login page	|	Login page	|	1 hour	|	2/13/2023	|	C
10	|	Make a signup page	|	Signup page with encryption feature to secure the password	|	1 hour	|	2/13/2023	|	C
11	|	Draw an ER diagram and write a brief explanation	|	To illustrate the tables and attributes of the solution.	|	30 mins.	|	2/24/2023	|	B
12	|	Make a homescreen page	|	Homescreen with features "New item", "Borrowed items list", and "Log out"	|	2 hours	|	2/24/2023	|	C
13	|	Make a new item page	|	New item page to add a new borrowed item information to database 	|	1 hour	|	2/27/2023	|	C
14	|	Make validations for text fields	|	Methods for each text field to validate input	|	2 hours	|	2/27/2023	|	C
15	|	Make a thank you popup dialog	|	Page for thanking the user when added a new item to the list	|	1 hour	|	2/28/2023	|	C
16	|	Make a borrowed items list page	|	Page that shows a table which has data of borrowed items list from the database	|	2 hours	|	3/1/2023	|	C
17	|	Make a table for all items in database	|	Table for the borrowed items list page that shows all items in one table	|	45 mins.	|	3/1/2023	|	C
18	|	Write the list of techiques used	|	List that contains what has been used during the development of the solution	|	15 mins.	|	3/2/2023	|	C
19	|	Draw a UML diagram for all classes and write an explanation	|	A diagram showing how the product was developed with methods and atrributes of the solution	|	1 hour.	|	3/2/2023	|	B
20	|	Draw a flow diagram and write an explanation	|	A flowchart for create_table method used for the development of the solution	|	15 mins.	|	3/2/2023	|	B
21	|	Draw a flow diagram and write an explanation	|	A flowchart for create_table method used for the development of the solution	|	25 mins.	|	3/2/2023	|	B
22	|	Draw a flow diagram and write an explanation	|	A flowchart for create_table method used for the development of the solution	|	25 mins.	|	3/2/2023	|	B
23	|	Test if login page works	|	Successful login	|	5 mins.	|	3/2/2023	|	B
24	|	Test if signup page works	|	Successful signup	|	5 mins.	|	3/2/2023	|	B
25	|	Testing if adding new item works	|	Successful adding new item	|	5 mins.	|	3/2/2023	|	B
26	|	Check if code has good comments, variable and method names	|	Having good comments for code and appropriate variable, method names	|	10 mins.	|	3/2/2023	|	B
27	|	Check if table shows the correct data	|	Table, showing the exact data as the database	|	5 mins.	|	3/2/2023	|	B
28	|	Create test plan	|	Tets plan table with test type, input, and output	|	10 mins.	|	3/2/2023	|	B
29	|	Add development of success criteria 1 to the documentation	|	Paragraph showing how the solution to the problem was developed.	|	10 mins.	|	3/2/2023	|	C
30	|	Add development of success criteria 2 to the documentation	|	Paragraph showing how the solution to the problem was developed.	|	10 mins.	|	3/2/2023	|	C
31	|	Add development of success criteria 3 to the documentation	|	Paragraph showing how the solution to the problem was developed.	|	10 mins.	|	3/2/2023	|	C
32	|	Add development of success criteria 4 to the documentation	|	Paragraph showing how the solution to the problem was developed.	|	10 mins.	|	3/2/2023	|	C
33	|	Add development of success criteria 5 to the documentation	|	Paragraph showing how the solution to the problem was developed.	|	10 mins.	|	3/2/2023	|	C
34	|	Add development of success criteria 6 to the documentation	|	Paragraph showing how the solution to the problem was developed.	|	10 mins.	|	3/2/2023	|	C
35	|	Record and upload a video of max. 4 min. length, presenting the application.	|	A video, showing how the application functions. Last 30 seconds should be focused on well-organization of code.	|	10 mins.	|	3/2/2023	|	D


# Criteria C: Development

## List of techniques used

1. If-else statements: These are conditional statements that allow the program to make decisions based on certain conditions. If a condition is true, a certain block of code is executed, otherwise, another block of code is executed.[^6]
2. Loops: These are used to repeat a certain block of code multiple times. There are different types of loops, such as for loops, while loops, and do-while loops.[^7]
3. Functions: These are reusable blocks of code that can be called multiple times from different parts of a program. Functions usually take inputs, perform some operations on those inputs, and then return a result.[^8]
4. Variables: These are containers for storing data values in a program. Variables can hold different types of data, such as numbers, strings, or boolean values.[^9]
5. Arrays: These are used to store multiple values in a single variable. Arrays can be of different types, such as one-dimensional arrays or multi-dimensional arrays.[^10]
6. Objects: These are complex data types that store data and methods related to a particular object or entity. Objects are typically used in object-oriented programming.[^11]
7. Classes: These are templates for creating objects in object-oriented programming. A class defines the properties and behaviors of an object, and objects can be created from a class.[^12]
8. Inheritance: This is a feature of object-oriented programming that allows a class to inherit properties and behaviors from another class.[^13]
9. Polymorphism: This is another feature of object-oriented programming that allows objects of different classes to be treated as if they were of the same class, by using common interfaces or abstract classes.[^14]
10. Recursion: This is a technique where a function calls itself to solve a problem by breaking it down into smaller subproblems. Recursion is used in many algorithms, such as sorting and searching.[^15]
11. KivyMD: building UI using KivyMD library, including navigation, layouts, widgets, and animations.[^4]
12. SQLite: working with SQLite database, including creating tables, inserting, updating, and retrieving data, and using SQL queries to manipulate data.[^5]

## Development
### Success criteria 1: The solution validates the input for items to rent, so the datatable is well-organized
In order to ensure a well-organized structure for the item details in the table, validation for each input is necessary. This approach provides a systematic way of organizing the data and ensures that only valid inputs are stored in the table.
#### Validating
```.py
def validate_date(self, text):
    """
    Validate the entered date
    """
    # Check if the entered text is a valid date in the specified format
    try:
        datetime.strptime(text, self.input_format)
        print("Valid date entered!")
    except ValueError:
        self.ids.date.error = True.
```
The code above illustrates the method used to validate input fields. This validation structure is implemented for each text field in the application to ensure data accuracy and consistency.[^8]

#### Inserting values to database
```.py
def insert(self, email, username, password):
    query = f"INSERT into users (email, password, username) VALUES ('{email}', '{password}', '{username}')"
    self.run_query(query)
```
The code shown above demonstrates how to insert new user data into the database. This same structure is also applied when I need to insert a new item into the database.

#### Show password method
```.py
# Define a method that toggles the visibility of the password field
def toggle_show_password(self):
    # Invert the value of the show_password attribute
    self.show_password = not self.show_password
    # Set the password attribute of the password field to the opposite of the show_password attribute
    self.ids.passwd_in.password = not self.show_password
```
The code defines a method that allows for the visibility of the password field to be toggled. This helped me to make it easier for the user to avoid human errors when entering their password on the login screen. When called, the method inverts the value of the show_password attribute and sets the password attribute of the password field to the opposite of the show_password attribute.

### Success criteria 2: The application features a secure login system, enabling the user to protect their data
The login system provides a secure way for users to access the application, protecting the data they enter and store in the application's database. Users can log in whenever they need to use the application, ensuring the safety and confidentiality of their information.
#### KivyMD Text field
```.kv
MDTextField:
    id: email_in
    hint_text: "Enter your email"
    icon_left: "email"
    helper_text_mode: "on_error"
    helper_text: "Please enter email"
```
This piece of code shows the use of KivyMD to create a text field for obtaining user input. The text field includes a hint text to indicate the expected input, an icon on the left side to signify the type of input, and a helper text that appears in case of an error. This structure is used throughout the development of my solution for user inputs.[^20]
#### KivyMD Button
```.kv
MDRaisedButton:
    font_name: "avenir_regular.ttf"
    id: login
    text: "Login"
    on_press: root.try_login()
    size_hint: .3, .5
    md_bg_color: "#689ebd"
```
The code above demonstrates how a button is created and utilized to obtain a command from the user via KivyMD. This structure is implemented throughout the code to obtain commands from the user in different places of my code.[^21]

### Success criteria 4: The solution affords the user the ability to effortlessly delete equipment records upon return
#### Deleting a row from the table
```.py
def delete(self):
    # Function to delete checked rows in the table
    checked_rows = self.data_table.get_row_checks() # Get the checked rows
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
```
The above code shows how to delete checked rows from a table in the database. The code accesses the checked rows using the get_row_checks() function, deletes them using a loop and a delete query. The code also uses the MDDialog function to create an alert dialog to inform the user that the item has been deleted. This structure is used in other areas of the code to display pop-up dialogs.[^22]

### Success criteria 5: The solution hashes the signup information entered by the user when trying to sign up
#### Hashing a string
```.py
from passlib.context import CryptContext

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
```
The above code demonstrates how to hash a string using the passlib library. The hash_password() function takes a user password as an input and returns the hashed password. The check_password() function is used to verify whether a user-entered password matches the hashed password stored in the database during the login process. These functions ensure that passwords are securely stored in the database and cannot be accessed by unauthorized users.[^23]

### Success criteria 6: The user is able to log out, so the information is secure
#### Change screens, leave screens
```.py
# Function to log out the user
def try_logout(self):
    print("User trying logging out")
    self.parent.current = "LoginScreen"
```
The code above demonstrates how to log out a user and switch to the LoginScreen page by changing the parent's current attribute to "LoginScreen". This code structure is used in various parts of the application to enable switching between different pages.[^24]
```.kv
MDRaisedButton:
  id: return_home
  size_hint: .4, 1
  text: "Return home"
  on_press: app.root.current = "HomeScreen"
  pos_hint: {"center_x": .5, "center_y": .5}
  md_bg_color: "#689ebd"
```
The code snippet above is an example of how to create a KivyMD button and link it to a function that changes the current screen to the "HomeScreen". The function app.root.current is used to set the current screen of the app to the desired screen. This code structure is used in different parts of the app to create buttons that navigate to different screens.[^21][^24]

### Accessing result run in console
```.py
def search(self, query):
    result = self.cursor.execute(query).fetchall()
    return result
```
The code above demonstrates a method that allows you to retrieve the results of a query that was executed in the console. This method is helpful as it enables me to run queries and retrieve their output in various parts of my application.

### Pop-up diolog
```.py
dialog = MDDialog(title="Thank you, item deleted!",
                         text=f"Your item ID: {item_id} has been successfully deleted.")
dialog.open()
```
This code creates a dialog box using KivyMD to notify the user that an item has been successfully deleted from the database. It takes the item ID as input and displays it in the dialog box. This code is reusable in different parts of the application where a similar confirmation dialog box is needed.

# Criteria D: Functionality
## A video demonstrating the proposed solution with narration
Please find the video in [this link](https://youtu.be/HfCwjyDmsc0) to watch how the application function.

[^1]: "Python." Wikipedia, Wikimedia Foundation, 10 Feb. 2023, https://en.wikipedia.org/wiki/Python.
[^2]: "Why Choose Python." Python.org, Python Software Foundation, 10 Feb. 2023, https://www.python.org/about/gettingstarted/.
[^3]: "Python for Data Science Handbook." O'Reilly, O'Reilly Media, Inc., 10 Feb. 2023, https://www.oreilly.com/library/view/python-for-data/9781491912126/
[^4]: "KivyMD: Material Design Components for Kivy." Github, 10 Feb. 2023, https://github.com/kivymd/KivyMD.
[^5]: "SQL." W3Schools, 10 Feb. 2023, https://www.w3schools.com/sql/
[^6]: "4.1. if Statements." Python 3.10.1 Documentation, Python Software Foundation, 2022, Accessed 2 Mar. 2023. https://docs.python.org/3/tutorial/controlflow.html#if-statements.
[^7]: Python Library. “Chapter 5: Loops.” Python 101, pythonlibrary.org, Accessed 2 Mar. 2023. https://python101.pythonlibrary.org/chapter5_loops.html.
[^8]: "Functions." Easy Python Docs, Easy Python, 2023, Accessed 2 Mar. 2023. https://www.easypythondocs.com/functions.html.
[^9]: "Variables." Easy Python Docs, Easy Python Docs, n.d., https://www.easypythondocs.com/variables.html. Accessed 2 Mar. 2023.
[^10]: Code Fellows. “Python Data Structures: Arrays and Lists.” Code Fellows, n.d., https://codefellows.github.io/sea-python-401d4/lectures/array.html. Accessed 2 Mar. 2023.
[^11]: Python Software Foundation. "Objects, Values, and Types." Python 3.9.7 documentation, 2021, https://docs.python.org/3/reference/datamodel.html#objects-values-and-types. Accessed 2 Mar. 2023.
[^12]: Python Software Foundation. “9. Classes.” Python 3.10.0 documentation, Python Software Foundation, 2021, https://docs.python.org/3/tutorial/classes.html. Accessed 2 Mar. 2023.
[^13]: Inheritance: "Classes - Python 3.10.0 documentation." Python Software Foundation, 2021, https://docs.python.org/3/tutorial/classes.html#inheritance. Accessed 2 Mar. 2023.
[^14]: Polymorphism in Python: Programiz. “Polymorphism in Python.” Programiz, n.d., https://www.programiz.com/python-programming/polymorphism. Accessed 2 March 2023.
[^15]: Real Python. “Python Recursion: Learn to Solve Problems with Recursion (Examples).” Real Python, Real Python, 11 May 2021, https://realpython.com/python-recursion/. Accessed 2 Mar. 2023
[^16]: Canva. "Amazingly Simple Graphic Design Software – Canva." Canva, Canva, https://www.canva.com/. Accessed Feb. 10 2023
[^17]: Wireframe.cc. N.p., n.d. Web. https://wireframe.cc/. Accessed Feb. 10 2023
[^18]: "Online Diagramming and Visual Solution." Creately, Creately, https://creately.com/. Accessed Feb. 24 2023
[^19]: "Diagrams.net." diagrams.net, 2023, https://www.diagrams.net/. Accessed 2 Mar. 2023
[^20]: "Text Field — KivyMD 0.104.1.dev0 documentation." KivyMD, 2021, https://kivymd.readthedocs.io/en/0.104.1/components/text-field/index.html. Accessed Mar. 2 2023
[^21]: "Button — KivyMD 0.104.1.dev0 documentation." KivyMD, 2021, https://kivymd.readthedocs.io/en/0.104.1/components/button/index.html. Accessed Mar. 2 2023
[^22]: "Dialog — KivyMD 0.104.1.dev0 documentation." KivyMD, 2021, https://kivymd.readthedocs.io/en/0.104.1/components/dialog/index.html. Accessed Mar. 2 2023
[^23]: "The CryptContext Class — Passlib v1.7.4 Documentation." Passlib, 2021, https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#the-cryptcontext-class. Accessed Mar. 2 2023
[^24]: "Kivy.uix.screenmanager — Kivy 2.0.0 documentation." Kivy, 2021, https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html. Accessed Mar. 2 2023

# Appendix
## Success criteria confirmation by the client
![Success_criteria_confirmation](https://user-images.githubusercontent.com/111758436/222607119-ad790fe6-f842-4692-8bbb-9d64e6ff16dc.png)
## Python code
```.py
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
                    # Create and open the alert dialog to say that the email or password is wrong
                    dialog = MDDialog(title="Login error",
                                      text=f"Entered email or password is wrong")
                    dialog.open()
            else:
                dialog = MDDialog(title="Login error",
                                  text=f"Entered email or password is wrong")
                dialog.open()

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
            # Create and open the alert dialog to say that the account has created successfully
            dialog = MDDialog(title="New account",
                              text=f"The account has created successfully, please log in")
            dialog.open()
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
    input_format = "%d-%m-%Y" # input format for date text field

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

    def try_add(self):
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
        checked_rows = self.data_table.get_row_checks() # Get the checked rows
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
                         ("Kind", 25),
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
```
## KivyMD code
```.kv
# login.kv

ScreenManager:
    LoginScreen:
        name: "LoginScreen"

    SignupScreen:
        name: "SignupScreen"

    HomeScreen:
        name: "HomeScreen"

    NewitemScreen:
        name: "NewitemScreen"

    BorrowedItemsScreen:
        name: "BorrowedItemsScreen"

<LoginScreen>:
    size: 500, 500
    FitImage:
        source: "background.png"

    MDCard:
        size_hint: .5, .9
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: dp(50)
        md_bg_color: "#EEE9DA"

        MDLabel:
            font_name: "avenir_regular.ttf"
            text: "Login"
            font_size: 30
            size_hint: .3, .4
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .5}

        MDBoxLayout:
            orientation: "vertical"
            size_hint: 1, None
            height: dp(120)

            MDTextField:
                id: email_in
                hint_text: "Enter your email"
                icon_left: "email"
                helper_text_mode: "on_error"
                helper_text: "Please enter email"

            MDTextField:
                id: passwd_in
                hint_text: "Enter your password"
                icon_left: "key"
                password: not show_pass.active
                helper_text_mode: "on_error"
                helper_text: "Please enter password"

            MDBoxLayout:
                orientation: "horizontal"
                size_hint: 1, None
                height: dp(40)
                MDCheckbox:
                    id: show_pass
                    size_hint_x: 0.1
                    on_active: passwd_in.password = not self.active
                    active: False
                MDLabel:
                    text: "Show password"
                    font_name: "avenir_regular.ttf"
                    font_size: 18
                    size_hint_x: 0.7

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .1

            MDRaisedButton:
                font_name: "avenir_regular.ttf"
                id: login
                text: "Login"
                on_press: root.try_login()
                size_hint: .3, .5
                md_bg_color: "#689ebd"

            MDLabel:
                font_name: "avenir_regular.ttf"
                size_hint: .3, 1

            MDRaisedButton:
                font_name: "avenir_regular.ttf"
                id: signup
                text: "Signup"
                on_press: root.try_signup()
                size_hint: .3, .5
                md_bg_color: "#689ebd"

<SignupScreen>:
    size: 500, 500
    FitImage:
        source: "background.png"

    MDCard:
        size_hint: .5, .9
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: dp(50)
        md_bg_color: "#EEE9DA"

        MDLabel:
            font_name: "avenir_regular.ttf"
            text: "Signup"
            font_size: 30
            size_hint: 1, .2
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .5}

        MDTextField:
            id: uname
            #required: True
            hint_text: "Enter username"
            icon_left: "account"

        MDTextField:
            id: email
            #required: True
            hint_text: "Enter your email"
            icon_left: "email"

        MDTextField:
            id: e_passwd
            #required: True
            hint_text: "Enter password"
            icon_left: "key"
            password: True
            helper_text_mode: "on_focus"
            helper_text: "Password must be at least 8 characters"

        MDTextField:
            id: c_passwd
            #required: True
            hint_text: "Confirm password"
            icon_left: "key"
            password: True
            helper_text_mode: "on_error"
            helper_text: "Passwords don't match"


        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .1

            MDRaisedButton:
                font_name: "avenir_regular.ttf"
                id: signup_cancel
                text: "Cancel"
                on_press: root.try_cancel()
                size_hint: .3, .7
                md_bg_color: "#93BFCF"

            MDLabel:
                font_name: "avenir_regular.ttf"
                size_hint: .3, 1

            MDRaisedButton:
                font_name: "avenir_regular.ttf"
                id: signup
                text: "Submit"
                on_press: root.try_register()
                size_hint: .3, .7
                md_bg_color: "#689ebd"

<HomeScreen>:
    size: 500, 500

    FitImage:
        source: "background.png"

    MDCard:
        size_hint: .5, .9
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: dp(50)
        md_bg_color: "#EEE9DA"

        MDLabel:
            id: wlcm_msg
            text: "Welcome to tracker"
            font_name: "avenir_regular.ttf"
            font_size: 30
            size_hint: 1, .1
            halign: "center"

        MDBoxLayout:
            size_hint: 1, .9
            orientation: 'vertical'
            padding: dp(50)


            MDBoxLayout:
                size_hint: (1, .15)
                spacing: dp(40)
                orientation: "vertical"

                MDFillRoundFlatIconButton:
                    text: 'New item'
                    icon: 'plus-circle-outline'
                    pos_hint: {'center_x': .5}
                    md_bg_color: "#689ebd"
                    font_name: "avenir_regular.ttf"
                    on_press: root.try_newitem()

                MDFillRoundFlatIconButton:
                    text: 'Borrowed items list'
                    icon: 'format-list-bulleted'
                    pos_hint: {'center_x': .5}
                    md_bg_color: "#689ebd"
                    font_name: "avenir_regular.ttf"
                    on_release: app.root.current = "BorrowedItemsScreen"

                MDFillRoundFlatIconButton:
                    text: 'Log out'
                    icon: 'logout-variant'
                    pos_hint: {'center_x': .5}
                    on_press: app.root.current = 'LoginScreen'
                    md_bg_color: "#689ebd"
                    font_name: "avenir_regular.ttf"

<NewitemScreen>:
    size: 500, 500
    FitImage:
        source: "background.png"

    MDCard:
        size_hint: .5, .9
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        md_bg_color: "#EEE9DA"

        MDBoxLayout:
            size_hint: 1, .1
            MDLabel:
                text: "New item"
                font_name: "avenir_regular.ttf"
                font_size: 30
                size_hint: 1, 1
                halign: "center"
                pos_hint: {"center_x": .5, "center_y": .3}

        MDLabel:
            size_hint: 1, .2

        MDBoxLayout:
            orientation: "vertical"
            size_hint: 1, .85
            padding: dp(30)

            MDTextField:
                id: customer_id
                hint_text: "Customer ID"
                icon_left: "account"
                on_text_validate: root.validate_customer_id(self.text)
                helper_text_mode: "on_error"
                helper_text: "Customer ID must be a number"

            MDTextField:
                id: date
                hint_text: "Date"
                icon_left: "calendar"
                multiline: False
                on_text_validate: root.validate_date(self.text)
                helper_text_mode: "on_error"
                helper_text: "Date must be in this format: dd-mm-YYYY"

            MDTextField:
                id: item
                hint_text: "Item"
                icon_left: "shopping"
                helper_text_mode: "on_error"
                helper_text: "Item must be one of these:\nSki, Snowboard, Ski shoes, Snowboard boots,\nSki clothes, Snowboard clothes"

            MDTextField:
                id: size
                hint_text: "Size"
                icon_left: "resize"
                on_text_validate: root.validate_size(self.text)
                helper_text_mode: "on_error"
                helper_text: "Size must be a number"

            MDTextField:
                id: item_id
                hint_text: "Item ID"
                icon_left: "barcode"
                on_text_validate: root.validate_item_id(self.text)
                helper_text_mode: "on_error"
                helper_text: "Item ID must be a number"

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: .7, .1
            pos_hint: {"center_x": .5, "center_y": .5}

            MDRaisedButton:
                font_name: "avenir_regular.ttf"
                id: newitem_cancel
                text: "Cancel"
                on_press: root.try_cancel()
                size_hint: .35, .7
                md_bg_color: "#689ebd"

            MDLabel:
                size_hint: .3, 1
                halign: "center"

            MDRaisedButton:
                font_name: "avenir_regular.ttf"
                id: newitem_submit
                text: "Submit"
                on_press: root.try_add()
                size_hint: .35, .7
                md_bg_color: "#689ebd"

        MDLabel:
            size_hint: 1, .05

<BorrowedItemsScreen>:
    size: 500, 500
    FitImage:
        source: "background.png"

    MDLabel:
        size_hint: 1, .9

    MDBoxLayout:
        size_hint: 1, .1
        orientation: "vertical"
        MDLabel:
            size_hint: 1, .05

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: .5, .1
            pos_hint: {"center_x": .5, "center_y": .5}


            MDRaisedButton:
                id: return_home
                size_hint: .4, 1
                text: "Return home"
                on_press: app.root.current = "HomeScreen"
                pos_hint: {"center_x": .5, "center_y": .5}
                md_bg_color: "#689ebd"

            MDLabel:
                size_hint: .2, .1

            MDRaisedButton:
                id: delete
                size_hint: .4, 1
                text: "Delete"
                on_press: root.delete()
                pos_hint: {"center_x": .5, "center_y": .5}
                md_bg_color: "#689ebd"

        MDLabel:
            size_hint: 1, .1
```
