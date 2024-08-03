from .users.user import User 
from .taskmanager.taskmanager import TaskManager

if __name__ == "__main__":
    #Creating the task manager instance
    tm = TaskManager() 
    is_loggedin: bool = False
    #MENU
    while True:
        ans: str = input("Hi! This is your task manager! Please log in('i')/sign up('u')").lower # TODO: Do some nice UI
        user: str = input("User name:").lower
        password: str = input("Password:")
        if ans == 'u': # Check if username exists, if no, ask to repeat password and save in users_list
            while user in tm.users_list:
                print(f"Username: {user} already exists, try adifferent username.")
                user: str = input("User name:")
                password: str = input("Password:")
            pass_val:str = input("Enter password again:")
            if password == pass_val:
                new_user:str = User(user, password)
                tm.users_list[user] = new_user
        if ans == 'i': # Login
            while(tm.users_list[user].password != password):
                print("Wrong username or Password, Try again.")
                user: str = input("User name:").lower
                password:str = input("Password:")

            is_loggedin = True
            while True:      
                print("Choose from the following:")
                print("1. Add a new task")
                print("2. Edit a task")
                print("3. View tasks list")
                print("4. Log out from your account")
                user_choice:str = print(f"{user}, your choice: ")
                
                if user_choice == '4': # Log out
                    is_loggedin = False
                    break
                
                if user_choice == '1': # Add a new task