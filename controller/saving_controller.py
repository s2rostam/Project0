from flask import render_template, session

from service.transaction_view_service import check_user_account_info, retrieve_list_of_transactions

def get_saving_page(q_param):
    if 'user_id' in session:    
        acc_info = check_user_account_info(session['user_id'])
        if acc_info is not None:
            l_transactions = retrieve_list_of_transactions(session['user_id'], q_param.lower())
            return render_template('actions/saving.html', sav_num = acc_info.s_amount, list_of_transactions = l_transactions)
        else:
            return "Something went wrong"
    else:
        return "Not logged in"