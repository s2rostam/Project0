from flask import render_template

def get_landing_page():
    return render_template('start/landingpage.html')