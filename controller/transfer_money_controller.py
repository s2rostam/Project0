

from flask import request, session, render_template
from repository.acc_info_dao import get_user_account_info
from repository.login_dao import get_user_login_by_id

from service.transfer_money_service import get_id_of_recieving_user, recieve_money_chequeing, send_money_chequeing, validate_username


def get_transfer_money_page(input_form):
    if 'user_id' in session:
        if request.method == "POST":
            #check if valid username?
            print(input_form)
            if validate_username(input_form.get('sendunamemoney')):
            #check if login exists and get user id
                rec_id = get_id_of_recieving_user(input_form.get('sendunamemoney'))
                if send_money_chequeing(session['user_id'], rec_id, input_form.get('sendamountmoney'), get_user_login_by_id(rec_id)):
                    recieve_money_chequeing(rec_id, input_form.get('sendamountmoney'), get_user_login_by_id(session['user_id']) )
                    return "Success"
                else:
                    return "couldn't complete"
            else:
                return "invalid username"            
        elif request.method == "GET":
            return render_template('actions/transfer_money.html')
    else:
        return "You are not logged in"