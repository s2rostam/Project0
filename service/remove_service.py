
from repository.acc_info_dao import delete_user_account_info
from repository.login_dao import delete_user_login_by_id, get_user_login_by_id
from repository.transaction_dao import delete_transaction_logs
from repository.user_info_dao import delete_user_info_by_id


def remove_user_records(id):
    if check_user_account_info(id) is not None:
        delete_transaction_logs(id)
        delete_user_info_by_id(id)
        delete_user_account_info(id)
        delete_user_login_by_id(id)

def check_user_account_info(id):
    acc_info = get_user_login_by_id(id)

    if acc_info is not None:
        return acc_info