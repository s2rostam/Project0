from repository.acc_info_dao import create_user_account_info
from repository.login_dao import create_user_login
from repository.user_info_dao import create_user_info

def init_user_account_info(id):
    confirm_creation_id = create_user_account_info(id)

    if confirm_creation_id is not None:
        return True
    else:
        return False

def init_user_info(id, first_name, last_name):
    user_info_creation_id = create_user_info(id, first_name, last_name)

    if user_info_creation_id is not None:
        return True
    else:
        return False

def validate_all_sections_filled(input_form):
    return ((not input_form.get("uname") == '') and (not input_form.get("upass") == '') and (not input_form.get("fname") == '') and (not input_form.get("lname") == ''))

def create_user_account(input_form):
    if validate_all_sections_filled(input_form):
        created_user_login_id = create_user_login(input_form.get('uname'), input_form.get('upass'))

        if created_user_login_id is not None:
            if init_user_account_info(created_user_login_id) and init_user_info(created_user_login_id, input_form.get('fname'), input_form.get('lname')):
                return created_user_login_id


