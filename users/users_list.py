from ..utils.singleton import singleton


@singleton
class Users_list():
    def __init__(self):
        # The users_list will look like this: Key = username, Value = User instance
        users_list = {}