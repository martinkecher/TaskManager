from .users.user import User 
from .taskmanager.taskmanager import TaskManager

if __name__ == "__main__":
    #Creating the task manager instance
    tm = TaskManager() 
    #MENU
    ans = input("Hi! This is your task manager! Please log in('i')/sign up('u')").lower # TODO: Do some nice UI
    user = input("User name:")
    password = input("Password:")
    if ans == 'u': # Check if username exists, if no, ask to repeat password and save in users_list
        while user in tm.users_list:
            print(f"Username: {user} already exists, try adifferent username.")
            user = input("User name:")
            password = input("Password:")
        pass_val = input("Enter password again:")
        if password == pass_val:
            new_user = User(user, password)
            tm.users_list[user] = new_user
            
        

    print("Choose from the following:")