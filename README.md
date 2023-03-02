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
<i>Figure 1</i> - System diagram for the application. As shown in the figure 1, the application uses PyCharm and KivyMD Library to develop the program. Shown with arrows, it stores the data in unit3_project_database.db, using the SQLite database engine.[^16]

## Wireframe
![unit3_project_wireframe (1)](https://user-images.githubusercontent.com/111758436/218105085-c54acaf6-3e25-42ba-a799-c51b652a95ae.png)
<i>Figure 2</i> - Wirefrime for the user interface. As shown in the figure 2, the application welcomes the user with a login page. If logged in, it will take the user to the homepage page. If pressed to "Sign up," the user find themselves in the sign up page. In the homepage page, the user can press "new item" and go to the new item page. If the user presses "borrowed items list" button, the app will change the page to the page where the user can see the list of borrowed equipments. The last button on the homepage page "log out" logs out the user and take them to login page back. In the new item page, the user can press save button after completing the form. It will take the user to the thank you page. If cancel is pressed, it will be taken to the homepage page. In thank you page, the user can either go to the list of borrowed items page or to the homepage. In the borrowed items list, the user is provided with the list of borrowed items from the shop. The user can go to the homepage from this page. Finally, in sign up page, the user can press register button to finsih the registration or login button to go back to the login page.[^17]

## Flow diagram
### Flow diagram for create_table (database_handler_login_signup class)
<img src="https://user-images.githubusercontent.com/111758436/222377806-7220550d-357d-4b1c-ab3f-4902abed7a99.jpeg" alt="Flowchart_create_table" style="width:100%;height:auto;">
<p align="justify">
  <i>Figure 3</i> - Flow diagram for create_table method of database_handler_login_signup class. The method is used to create a table with the name "users" that contains columns email, username, email, and password. This is used when the program is run for the first time. If the table already exists, it doesn't create a new table.
</p>

### Flow diagram for try_login (LoginScreen class)
<img src="https://user-images.githubusercontent.com/111758436/222398513-37b6aeaf-e966-4068-9208-8692f8585dd3.jpg" alt="Flowchart_try_login" style="width:100%;height:auto;">
<p align="justify">
  <i>Figure 4</i> - Flow diagram for try_login method of LoginScreen class. The method is used to login. It is able to compare the password with the password that is shown as hashed in the database. If entered email and password is correct, the method takes the user to Homescreen.
</p>

### Flow diagram for on_pre_enter (BorrowedItemsScreen class)
<img src="https://user-images.githubusercontent.com/111758436/222402110-b5b4fe78-d3fd-45ea-93c2-c0abf8d55c99.jpg" alt="Flowchart_on_pre_enter" style="width:100%;height:auto;">
<p align="justify">
  <i>Figure 5</i> - Flow diagram for on_pre_enter method of BorrowedItemsScreen. The method is used when the user wants to see the list of borrowed items. The method  that is called on_pre_enter works when the button "BorrowedItemsScreen" is pressed. As it can be seen from the figure 5, the method updates the table every time it is run.
</p>

## ER Diagram
![ER_diagram](https://user-images.githubusercontent.com/111758436/221069445-e499566c-0956-4678-8704-b0b00b32315d.jpg)
<i>Figure 6</i> - ER diagram for the database. As shown in the figure x, the database has 2 tables named "users" and "items." Shown on the left, the users table is to save users' username, email, and password. The table shown on the right saves the data of borrowed items: customer ID, date, kind, size, and item ID. Having a unique item ID for each item helps the user not to lend one item second time to another customer.[^18]

## UML Diagram
![UML_diagram](https://user-images.githubusercontent.com/111758436/222324521-c8d27aa5-3c10-43c0-9a90-05e6bdbc6e37.jpg)
<i>Figure 7</i> - UML diagram for the classes used in the app. As you can see from the figure 7, all classes inherit from the main class MDApp and MDClasses.[^19]

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
7	|	Draw a wireframe and write a brief explanation	|	To better understand how different screen pages look like in the app.	|	1 hour	|	2/10/2023	|	B
8	|	Make a login page	|	Login page	|	1 hour	|	2/13/2023	|	C
9	|	Make a signup page	|	Signup page with encryption feature to secure the password	|	1 hour	|	2/13/2023	|	C
10	|	Draw an ER diagram and write a brief explanation	|	To illustrate the tables and attributes of the solution.	|	30 mins.	|	2/24/2023	|	B
11	|	Make a homescreen page	|	Homescreen with features "New item", "Borrowed items list", and "Log out"	|	2 hours	|	2/24/2023	|	C
12	|	Make a new item page	|	New item page to add a new borrowed item information to database 	|	1 hour	|	2/27/2023	|	C
13	|	Make validations for text fields	|	Methods for each text field to validate input	|	2 hours	|	2/27/2023	|	C
14	|	Make a thank you popup dialog	|	Page for thanking the user when added a new item to the list	|	1 hour	|	2/28/2023	|	C
15	|	Make a borrowed items list page	|	Page that shows a table which has data of borrowed items list from the database	|	2 hours	|	3/1/2023	|	C
16	|	Make a table for all items in database	|	Table for the borrowed items list page that shows all items in one table	|	45 mins.	|	3/1/2023	|	C
17	|	Write the list of techiques used	|	List that contains what has been used during the development of the solution	|	15 mins.	|	3/2/2023	|	C
18	|	Draw a UML diagram for all classes and write an explanation	|	A diagram showing how the product was developed with methods and atrributes of the solution	|	1 hour.	|	3/2/2023	|	B
19	|	Draw a flow diagram and write an explanation	|	A flowchart for create_table method used for the development of the solution	|	15 mins.	|	3/2/2023	|	B
20	|	Draw a flow diagram and write an explanation	|	A flowchart for create_table method used for the development of the solution	|	25 mins.	|	3/2/2023	|	B
21	|	Draw a flow diagram and write an explanation	|	A flowchart for create_table method used for the development of the solution	|	25 mins.	|	3/2/2023	|	B
22	|	Test if login page works	|	Successful login	|	5 mins.	|	3/2/2023	|	B
23	|	Test if signup page works	|	Successful signup	|	5 mins.	|	3/2/2023	|	B
24	|	Testing if adding new item works	|	Successful adding new item	|	5 mins.	|	3/2/2023	|	B
25	|	Check if code has good comments, variable and method names	|	Having good comments for code and appropriate variable, method names	|	10 mins.	|	3/2/2023	|	B
26	|	Check if table shows the correct data	|	Table, showing the exact data as the database	|	5 mins.	|	3/2/2023	|	B
27	|	Create test plan	|	Tets plan table with test type, input, and output	|	10 mins.	|	3/2/2023	|	B
28	|	Add development of success criteria 1 to the documentation	|	Paragraph showing how the solution to the problem was developed.	|	10 mins.	|	3/2/2023	|	C
29	|	Add development of success criteria 2 to the documentation	|	Paragraph showing how the solution to the problem was developed.	|	10 mins.	|	3/2/2023	|	C
30	|	Add development of success criteria 3 to the documentation	|	Paragraph showing how the solution to the problem was developed.	|	10 mins.	|	3/2/2023	|	C
31	|	Add development of success criteria 4 to the documentation	|	Paragraph showing how the solution to the problem was developed.	|	10 mins.	|	3/2/2023	|	C
32	|	Add development of success criteria 5 to the documentation	|	Paragraph showing how the solution to the problem was developed.	|	10 mins.	|	3/2/2023	|	C
33	|	Add development of success criteria 6 to the documentation	|	Paragraph showing how the solution to the problem was developed.	|	10 mins.	|	3/2/2023	|	C
34	|	Record and upload a video of max. 4 min. length, presenting the application.	|	A video, showing how the application functions. Last 30 seconds should be focused on well-organization of code.	|	10 mins.	|	3/2/2023	|	D


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
13. Testing: writing and running tests to ensure code functionality and performance.

## Development
### Success criteria 1: The solution validates the input for items to rent, so the datatable is well-organized
To have a structure for item details in the table, having validation for each input makes the table well-organized.
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
This code shows how I validate an input. I use the same structure for other text fields as well.[^8]

#### Inserting values to database
```.py
def insert(self, email, username, password):
    query = f"INSERT into users (email, password, username) VALUES ('{email}', '{password}', '{username}')"
    self.run_query(query)
```
The code above shows how to insert new user information to the database. I use this structure when I need to add new item to database as well.

### Success criteria 2: The application features a secure login system, enabling the user to protect their data
Login system enables the user to login to the application when the user wants to use. This lets the user secure the data entered to the database in the application.
#### KivyMD Text field
```.kv
MDTextField:
    id: email_in
    hint_text: "Enter your email"
    icon_left: "email"
    helper_text_mode: "on_error"
    helper_text: "Please enter email"
```
This piece of code shows how I create a text field and get an input from the user by using KivyMD. I use the same structure to get inputs in different places of codes.[^20]
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
This piece of code shows how I create a button to get a commmand from the user by using KivyMD. I use the same structure to get commands in different places of codes.[^21]

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
The code above how to access checked rows, a database, create and get result of a query. Additionaly, I use MDDiaolog to let the user know that the row has been deleted from the database. I use the same structure of code in different areas of my code if I need a pop-up diaolog.[^22]

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
The code above shows two functions hash and check passwords used to hash the password when created a new account. The function check_password helps the app to check if the entered password in login screen matches with the hashed password in the database.[^23]

### Success criteria 6: The user is able to log out, so the information is secure
#### Change screens, leave screens
```.py
# Function to log out the user
def try_logout(self):
    print("User trying logging out")
    self.parent.current = "LoginScreen"
```
The code shows how to change screen using Python. I use the same code in different pages to switch between pages.[^24]
```.kv
MDRaisedButton:
  id: return_home
  size_hint: .4, 1
  text: "Return home"
  on_press: app.root.current = "HomeScreen"
  pos_hint: {"center_x": .5, "center_y": .5}
  md_bg_color: "#689ebd"
```
The KivyMD code above shows a button to change the screen to Homescreen. Line 5 has a function "app.root.current" which allows us to switch between pages. I use the same code if needed to change the page using KivyMD.[^21][^24]

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
