
from repository.login_dao import get_user_login


def check_for_login_account(input_form):
    user_login = get_user_login(input_form.get('uname'), input_form.get('upass'))
    if user_login is not None:
        return user_login