from .role import Role

class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username if username_is_valid else print("User name is not valid") # TODO: add username_is_valid func and change the print
        self.password = password if password.isalnum() else print("Password is not valid")
        self.role = Role.REGULAR