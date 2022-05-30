from flask import render_template

def get_signup_page():
    return render_template('start/signup.html')