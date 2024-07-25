# This is the main program of the TaskManager program

from ..utils.singleton import singleton
from ..users.users_list import Users_list
from ..users.user import User 


@singleton
class TaskManager:
    def __init__(self):
        self.users_list = Users_list()

    def add_user(self, user: User) -> bool:
        if user.username in self.users_list:
            return False
        else:
            Users_list[user.username] = (user.password, user.role)
            return True
        



