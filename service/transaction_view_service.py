
from repository.acc_info_dao import get_user_account_info
from repository.transaction_dao import get_transaction_log


def check_user_account_info(id):
    acc_info = get_user_account_info(id)

    if acc_info is not None:
        return acc_info

def retrieve_list_of_transactions(id, q_param):
    l_transactions = get_transaction_log(id, q_param.lower())

    if (isinstance(l_transactions, list) or isinstance(l_transactions, str)):
        return l_transactions