import re

#methods below for initial creation validation
def validate_pattern_username(username):
    p_login = r'^[^\0][a-zA-Z]\w+$'

    if (re.search(p_login, username) is not None):
        return True
    else:
        return False

def validate_pattern_password(password):
    p_login = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#$%^&*]{4,}$'

    if (re.search(p_login, password) is not None):
        return True
    else:
        return False

def validate_pattern_first_name(first_name):
    p_name = r"^\b([A-ZÀ-ÿ][-,a-z. ']+[ ]*)+[^\s]$"

    if (re.search(p_name, first_name) is not None):
        return True
    else:
        return False

def validate_pattern_last_name(last_name):
    p_name =r"^\b([A-ZÀ-ÿ][-,a-z. ']+[ ]*)+[^\s]$"

    if (re.search(p_name, last_name) is not None):
        return True
    else:
        return False

def validate_length_username(username):
    return len(username) > 3 and len(username) <= 50

def validate_length_password(password):
    return len(password) > 3 and len(password) <= 50

def validate_length_first_name(first_name):
    return len(first_name) > 3 and len(first_name) <= 30

def validate_length_last_name(last_name):
    return len(last_name) > 3 and len(last_name) <= 50

def validate_pattern_login(username, password):
    return validate_pattern_username(username) and validate_pattern_password(password)

def validate_length_login(username, password):
    return validate_length_username(username) and validate_length_password(password)

def validate_login_info(username, password):
    return validate_pattern_login(username, password) and validate_length_login(username, password)

def validate_pattern_user_info(first_name, last_name):
    return validate_pattern_first_name(first_name) and validate_pattern_last_name(last_name)

def validate_length_user_info(first_name, last_name):
    return validate_length_first_name(first_name) and validate_length_last_name(last_name)

def validate_user_info(first_name, last_name):
    return validate_pattern_user_info(first_name, last_name) and validate_length_user_info(first_name, last_name)