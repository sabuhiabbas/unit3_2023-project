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

### Success Criteria
1. The solution implements encryption of sensitive data inputted by the user.
2. The application features a secure login system, enabling the user to protect their data. 
3. The user is able to input various information pertaining to the rental equipment. 
4. The solution affords the user the ability to effortlessly delete equipment records upon return. 
5. The user is able to view a categorized list of borrowed equipment, organized by customer ID, type of rental equipment, and rental date. 
6. The user has the capability to edit previously entered data within the application.

### Rationale for Proposed Solution
Python is a versatile language and can be used for a wide range of applications, including web development, scientific computing, data analysis, artificial intelligence, and more. This versatility makes it a good choice for building a wide range of applications, including custom software.[^1]
Python has a large and active community of users and developers. This means that there is a wealth of resources available to help you learn the language and build your application, as well as a large pool of talented developers who can contribute to your project.[^2]
Python has a simple, intuitive syntax that makes it easy for new users to learn and for experienced developers to quickly pick up. This makes it a good choice for building applications quickly and with fewer bugs, as well as for prototyping new ideas.[^3]

One of the main advantages of using KivyMD is that it allows developers to build applications that can run on multiple platforms, including Android, iOS, and Windows. This makes it an ideal choice for those who want to reach a wide audience with their apps. KivyMD is designed to be user-friendly and intuitive, making it easy for developers of all skill levels to get started with creating their own applications. This can help to save time and effort, allowing developers to focus on creating their app's functionality and features. KivyMD offers a wide range of customization options that allow developers to tailor their apps to meet the specific needs of their users. From changing the look and feel of the interface to adding custom animations, the library offers a variety of options to make an app truly unique.[^4]

SQL is designed to handle large amounts of data efficiently, making it an ideal choice for applications that need to store and manage a large amount of information. This makes it an ideal choice for applications that need to scale as they grow, as SQL databases can be easily expanded to meet the needs of the application. SQL databases allow for the storage of structured data, which can be easily queried and manipulated. This makes it easier to find the information you need, and to perform complex data analysis tasks. SQL databases are highly reliable, and offer features such as transaction management and data integrity to ensure that the data stored in the database remains accurate and up-to-date. This makes SQL an ideal choice for applications that need to store critical data that must be maintained even in the event of a power outage or other failure.[^5]

# Criteria B: Design

## System Diagram
![System diagram for skisnowboard rental shop tracker](https://user-images.githubusercontent.com/111758436/218088249-14279bc6-a1fe-40fd-98bb-fd0d3174b344.png)
<p align='justify'>
<i>Figure 1</i> - System diagram for the application. As shown in the figure 1, the application uses PyCharm and KivyMD Library to develop the program. Shown with arrows, it stores the data in unit3_project_database.db, using the SQLite database engine. 
</p>

## Wireframe
![unit3_project_wireframe (1)](https://user-images.githubusercontent.com/111758436/218105085-c54acaf6-3e25-42ba-a799-c51b652a95ae.png)
<p align='justify'>
<i>Figure 2</i> - Wirefrime for the user interface. As shown in the figure 2, the application welcomes the user with a login page. If logged in, it will take the user to the homepage page. If pressed to "Sign up," the user find themselves in the sign up page. In the homepage page, the user can press "new item" and go to the new item page. If the user presses "borrowed items list" button, the app will change the page to the page where the user can see the list of borrowed equipments. The last button on the homepage page "log out" logs out the user and take them to login page back. In the new item page, the user can press save button after completing the form. It will take the user to the thank you page. If cancel is pressed, it will be taken to the homepage page. In thank you page, the user can either go to the list of borrowed items page or to the homepage. In the borrowed items list, the user is provided with the list of borrowed items from the shop. The user can go to the homepage from this page. Finally, in sign up page, the user can press register button to finsih the registration or login button to go back to the login page.
</p>

## Flow diagram
## ER Diagram
## UML Diagram

## Test Plan
| Description | Type | Inputs | Outputs | 
| ----------- | ---- | ------ | ------- |

## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|


# Criteria C: Development

## List of techniques used

## Development


# Criteria D: Functionality
## A video demonstrating the proposed solution with narration

[^1]: "Python." Wikipedia, Wikimedia Foundation, 10 Feb. 2023, https://en.wikipedia.org/wiki/Python.
[^2]: "Why Choose Python." Python.org, Python Software Foundation, 10 Feb. 2023, https://www.python.org/about/gettingstarted/.
[^3]: "Python for Data Science Handbook." O'Reilly, O'Reilly Media, Inc., 10 Feb. 2023, https://www.oreilly.com/library/view/python-for-data/9781491912126/
[^4]: "KivyMD: Material Design Components for Kivy." Github, 10 Feb. 2023, https://github.com/kivymd/KivyMD.
[^5]: "SQL." W3Schools, 10 Feb. 2023, https://www.w3schools.com/sql/
