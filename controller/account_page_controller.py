from flask import render_template, session, redirect, url_for

from service.login_service import check_for_login_account
from service.remove_service import remove_user_records
from service.signup_service import create_user_account
from service.user_info_service import retrieve_user_info
from service.validate_signup_service import validate_login_info, validate_user_info

def get_account_page(input_form):
    soptions = ["Chequeing", "Saving", "Deposit/Withdraw", "Transfer"]
    surl = ['chequeing', 'saving', 'wd', 'transfer-money']

    if input_form.get('submit') == 'Log out':
        session.pop('user_id', None)
        return redirect(url_for("landing_page"))

    elif input_form.get('submit') == 'Remove account':
        remove_user_records(session['user_id'])
        session.pop('user_id', None)
        return redirect(url_for("landing_page"))

    elif input_form.get('page') == 'sign up':
        if validate_login_info(input_form.get("uname"), input_form.get("upass")) and validate_user_info(input_form.get("fname"), input_form.get("lname")):
            create_user_account(input_form)
            return redirect(url_for("login"))
        else:
            return "Invalid input for signup. Make sure name, login and password are valid. (no special characters/numbers allowed for names, capitalization required)"

    user_login = check_for_login_account(input_form)
    if user_login is not None:
        session['user_id'] = user_login.user_id
        user_name_greet = retrieve_user_info(session['user_id'])
        return render_template("start/accountpage.html", user_first_name = user_name_greet.first_name, user_last_name = user_name_greet.last_name, options = soptions, url_options = surl)
    else:
        return "Login failed. Account not found"

