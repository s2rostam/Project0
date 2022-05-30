
from repository.user_info_dao import get_user_info


def retrieve_user_info(id):
    vals = get_user_info(id)

    return vals