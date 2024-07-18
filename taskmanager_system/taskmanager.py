# This is the main program of the TaskManager program

from ..utils.singleton import singleton
from ..users.users_list import Users_list


@singleton
class TaskManager:
    def __init__(self):
        self.users_list = Users_list()

    def add_user(self, user)