from flask import render_template

def get_login_page():
    return render_template('start/login.html')