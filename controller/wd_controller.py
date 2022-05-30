
from flask import render_template, request, session
from service.wd_service import *
from service.transaction_view_service import get_user_account_info

def get_wd_page(input_form):
    if 'user_id' in session:
        if request.method == "POST":
            if validate_button_pressed(input_form):
                if (input_form.get("accounts") == "chq" and input_form.get("moneytransac") == "withdraw"):
                    if validate_money_amount_withdraw_chequeing(session['user_id'], input_form.get("withdrawmoney")):
                        val = withdraw_money_chequeing(session['user_id'], input_form.get("withdrawmoney"), input_form.get("accounts"))
                        if val is not None:
                            return "Success"
                        else:
                            return "Something went wrong"
                    else:
                        return "Not enough money"
                elif (input_form.get("accounts") == "chq" and input_form.get("moneytransac") == "deposit"):
                    if validate_money_amount_deposit_chequeing(session['user_id'], input_form.get("depositmoney")):
                        val = deposit_money_chequeing(session['user_id'], input_form.get("depositmoney"), input_form.get("accounts"))
                        if val is not None:
                            return "Success"
                        else:
                            return "Something went wrong"
                    else:
                        return "Not enough money"
                elif (input_form.get("accounts") == "sav" and input_form.get("moneytransac") == "withdraw"):
                    if validate_money_amount_withdraw_saving(session['user_id'], input_form.get("withdrawmoney")):
                        val = withdraw_money_saving(session['user_id'], input_form.get("withdrawmoney"), input_form.get("accounts"))
                        if val is not None:
                            return "Success"
                        else:
                            return "Something went wrong"
                    else:
                        return "Too much money"
                elif (input_form.get("accounts") == "sav" and input_form.get("moneytransac") == "deposit"):
                    if validate_money_amount_deposit_saving(session['user_id'], input_form.get("depositmoney")):
                        val = deposit_money_saving(session['user_id'], input_form.get("depositmoney"), input_form.get("accounts"))
                        if val is not None:
                            return "Success"
                        else:
                            return "Something went wrong"
                    else:
                        return "Too much money"
                else:
                    return "Something went wrong"
            else:
                return "Fill correct box"
            
        elif request.method == "GET":
            user_acc = get_user_account_info(session['user_id'])
            if (user_acc is not None):
                return render_template('actions/wd.html', camount = user_acc.c_amount, samount = user_acc.s_amount)
            else:
                return "Something went wrong. Account doesn't exist"
    else:
        return "You are not logged in"