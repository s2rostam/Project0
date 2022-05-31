from decimal import Decimal
from repository.acc_info_dao import update_user_account_info
from repository.login_dao import get_user_id_by_username
from repository.transaction_dao import create_transaction_log
from service.validate_signup_service import validate_length_username, validate_pattern_username

from service.wd_service import check_user_account_info, validate_money_amount_deposit_chequeing, validate_money_amount_withdraw_chequeing


def send_money_chequeing(id, other_id, money, sent_user):
    if check_user_account_info(id) is not None and check_user_account_info(other_id) is not None:
        if (validate_money_amount_withdraw_chequeing(id, money)):
            t_id = do_transaction(id, 'chequeing', -Decimal(money), f"Sent money to {sent_user}", "credit", "chq")
            if t_id is not None:
                return True
        else:
            return False
    return False

def recieve_money_chequeing(id, money, rec_user):
    if (validate_money_amount_deposit_chequeing(id, money)):
        t_id = do_transaction(id, 'chequeing', Decimal(money), f"Recieved money from {rec_user}", 'debit', "chq")
        return t_id

def do_transaction(id, acc_name, money, t_name, d_c_type, acc):
    account = check_user_account_info(id)

    update_user_account_info(id, acc_name, money, account.c_amount)
    return create_transaction_log(id, t_name, money, d_c_type , acc)

def validate_username(username):
    return validate_pattern_username(username) and validate_length_username(username)

def get_id_of_recieving_user(username):
    return get_user_id_by_username(username)