# **Bank of Mango Web Application**

This is the web application for the Bank of Mango. Create an account in order to use our services.

Features include:
- Create an account
    -  Includes a Chequeing and Savings account
- Withdraw and deposit
- View previous transactions
- Transfer funds to another account with the Bank of Mango
- Removing your account 

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

# License

MIT License

Copyright (c) [2022] [Sarah Rostami]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
