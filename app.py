from cmath import log
from flask import Flask, request, jsonify
import secrets
import logging
from logging.handlers import RotatingFileHandler
from time import strftime

from controller.account_page_controller import get_account_page
from controller.chequeing_controller import get_chequeing_page
from controller.saving_controller import get_saving_page;
from controller.landing_page_controller import get_landing_page
from controller.login_controller import get_login_page
from controller.signup_controller import get_signup_page
from controller.transfer_money_controller import get_transfer_money_page
from controller.wd_controller import get_wd_page

app = Flask(__name__)

app.secret_key = secrets.token_hex()
        
@app.route('/', methods=["GET"])
def landing_page():
    return get_landing_page()

@app.route('/signup', methods=["GET"])
def signup():
    return get_signup_page()

@app.route('/login', methods=["GET"])
def login():
    return get_login_page()

@app.route('/account', methods=["POST"])
def account():
    input_form = request.form
    return get_account_page(input_form)
        
@app.route('/account/chequeing', methods=["GET"])
def chequeing():
    acc = request.args.get('submit')
    return get_chequeing_page(acc)


@app.route('/account/saving', methods=["GET"])
def saving():
    acc = request.args.get('submit')
    return get_saving_page(acc)

@app.route('/account/transfer-money', methods=["GET", "POST"])
def transfer_money():
    input_form =  request.form
    return get_transfer_money_page(input_form)

@app.route('/account/wd', methods=["GET", "POST"])
def wd():
    input_form = request.form
    return get_wd_page(input_form)

if __name__ == '__main__':
    logger = logging.getLogger('werkzeug')
    handler = logging.FileHandler('requests.log')
    logger.addHandler(handler)
    app.run(debug=True)