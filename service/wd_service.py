
from decimal import Decimal
from repository.acc_info_dao import get_user_account_info, update_user_account_info
from repository.transaction_dao import create_transaction_log


def withdraw_money_chequeing(id, money, acc):
    t_id = do_transaction(id, 'chequeing', -Decimal(money), "Withdraw", "credit", acc)
    return t_id

def withdraw_money_saving(id, money, acc):
    t_id = do_transaction(id, 'saving', -Decimal(money), "Withdraw", "credit", acc)
    return t_id

def deposit_money_chequeing(id, money, acc):
    t_id = do_transaction(id, 'chequeing', Decimal(money), 'Deposit', 'debit', acc)
    return t_id

def deposit_money_saving(id, money, acc):
    t_id = do_transaction(id, 'saving', Decimal(money), 'Deposit', 'debit', acc)
    return t_id

def do_transaction(id, acc_name, money, t_name, d_c_type, acc):
    account = check_user_account_info(id)
    if "s" in acc_name:
        id = update_user_account_info(id, acc_name, money, account.s_amount)
        return create_transaction_log(id, t_name, money, d_c_type , acc)
    else:
        id = update_user_account_info(id, acc_name, money, account.c_amount)
        return create_transaction_log(id, t_name, money, d_c_type , acc)

def validate_money_amount_deposit_chequeing(id, money):
    account = check_user_account_info(id)
    if account is not None:
       return deposit_check(money, account.c_amount)

def validate_money_amount_deposit_saving(id, money):
    account = check_user_account_info(id)
    if account is not None:
        return deposit_check(money, account.s_amount)

def deposit_check(money: str, curr_amount: Decimal):
    conver_money = Decimal(money)
    if (conver_money < Decimal(0.00)):
        return False
    total = Decimal(money) + curr_amount
    if total < 9999999:
        return True
    else:
        return False

def validate_money_amount_withdraw_chequeing(id, money):
    account = check_user_account_info(id)
    if account is not None:
        return withdraw_check(money, account.c_amount)

def validate_money_amount_withdraw_saving(id, money):
    account = check_user_account_info(id)
    if account is not None:
        return withdraw_check(money, account.s_amount)

def withdraw_check(money: str, curr_amount: Decimal):
    conver_money = Decimal(money)
    if (conver_money < Decimal(0.00)):
        return False
    total = -Decimal(money) + curr_amount
    if total >= 0:
        return True
    else:
        return False

def validate_button_pressed(form):
    check_input = form.get("moneytransac") + 'money'
    input_value = form.get(check_input)
    if input_value == '':
        return False
    else: 
        return True

def check_user_account_info(id):
    acc_info = get_user_account_info(id)

    if acc_info is not None:
        return acc_info

