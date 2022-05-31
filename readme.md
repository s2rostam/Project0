# **Bank of Mango Web Application**

This is the web application for the Bank of Mango. Create an account in order to use our services.

Features include:
- Create an account
    -  Includes a Chequeing and Savings account
- Withdraw and deposit
- View previous transactions
- Transfer funds to another account with the Bank of Mango
- Removing your account 

# **Technologies**

This app is hosted by the Flask Web Framework (2.1.2) and uses the following technology:
- Python 3.9.12 - For server backend
- psycopg2 - For accessing database from flask server
- HTML - For templates
- Jinja - For rendering templates
- AWS RDS (PostgreSQL10) - For storing and accessing data 
- pytest - For unit testing
- Postman - For server testing
- DBeaver - For viewing and creating tables
- Git - For version control

# **Install**
In order to use the Bank of Mango Web Application on your device please follow the steps below:

### Prerequsites
- Python 3.9.12 or higher
    - pip
- Git
- Command line interface of your choice
    - (Recommended) Git Bash
    - Powershell
    - CMD
    - Terminal
---
1. Install the virtualenv package using pip
    ```
    > pip install virtualenv
    ```
2. Clone this repository to your local machine to where you'd like
    ```
    > git clone https://github.com/s2rostam/Project0.git
    ```
3. Inside the the repository you just cloned, create a virtual environment and then activate it
    ```
    > virtualenv venv
    > source venv/Scripts/activate
    ```
4. Once activated install all packages using the following command
    ```
    > pip install -r requirements.txt
    ```
5. Run the program 
    ```
    > python app.py
    ```
6. If you want to run the test cases use the command
    ```
    > pytest
    ```
7. If you want to deactivate the virtual enviroment after done with the app use the command below
    ```
    > deactivate
    ```

# **User Stories**

[Link to user stories here.](https://trello.com/b/JofIOTMt/sarah-projects)
