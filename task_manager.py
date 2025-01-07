#region imports
from datetime import date, datetime
#endregion

#region Task Management
#region View Tasks
# Function to build a label with spaces for formatting
def build_label(label_text):
    spaces_count = 20 - len(label_text)
    spaces = ''
    for i in range(1, spaces_count):
        spaces = spaces + ' '

    return f"{label_text}:{spaces}"

# Function to print a task in the console
def print_task_in_console(user, task_title, task_description, 
                          task_assigned_date, task_due_date, is_completed):
    print("______________________________________________________________________________________\n")
    print(f"{build_label('Task')} {task_title}")
    print(f"{build_label('Assigned to')} {user}")
    print(f"{build_label('Date assigned')} {task_assigned_date}")
    print(f"{build_label('Due date')} {task_due_date}")
    print(f"{build_label('Task complete?')} {is_completed}")
    print(f"{build_label('Task description')} {task_description}")

# Function to print multiple tasks
def print_tasks(tasks):
    for task_details in tasks:
        try:
            user = task_details[0].strip()
            task_title = task_details[1].strip()
            task_description =  task_details[2].strip() 
            task_assigned_date =  task_details[3].strip()
            task_due_date =  task_details[4].strip()
            is_completed =  task_details[5].strip()
        except IndexError:
            raise IndexError("Error: A task field within a record in tasks.txt is missing.")
        except:
            raise Exception("Error: An error occurred while parsing task information from a line in the tasks.txt file.")

        print_task_in_console(user, task_title, task_description,
                            task_assigned_date, task_due_date, is_completed)
    print("______________________________________________________________________________________\n")

# Function to extract and format all tasks from a file content
def get_all_tasks(tasks_file_content):
    tasks = []
    lines = tasks_file_content.split("\n")

    for line in lines:
        tasks.append(line.split(","))

    return tasks

# Function to get tasks for a specific user
def get_tasks_for_user(user, tasks):
    user_tasks = []
    for task in tasks:
        assigned_user = task[0]
        if assigned_user == user:
            user_tasks.append(task)
    return user_tasks

# Function to read the content of the tasks file
def get_tasks_file_content():
     return open('tasks.txt', 'r').read()

# Function to view tasks for a specific user
def view_tasks_for_user(user):
    tasks = []
    tasks_file_content = get_tasks_file_content()
    tasks += get_tasks_for_user(user, get_all_tasks(tasks_file_content))

    if(len(tasks) == 0):
        print(f"No tasks found for user '{user}.'")
    else:
        print_tasks(tasks)  

# Function to view all tasks for all users
def view_tasks_for_all_users():
    tasks = []
    tasks_file_content = get_tasks_file_content()
    tasks += get_all_tasks(tasks_file_content)

    if(len(tasks) == 0):
        print(f"No tasks found.")
    else:
        print_tasks(tasks)  
#endregion

#region Add New Task
# Function to get task details from user input
def get_task_details():
    task_assignee = input("Please enter the username of the person whom the task is assigned to: ")
    task_title = input("Please enter the title of the task: ")
    task_description = input("Please enter the description of the task: ")
    task_due_date = get_due_date()
    task_assigned_date = date.today().strftime("%d %b %Y")
    is_completed = "No"

    return f"{task_assignee}, {task_title}, {task_description}, {task_assigned_date}, {task_due_date}, {is_completed}" 

# Function to get a due date for a task
def get_due_date():
    try:
        input_value = input("Please enter the due date of the task in the format of the following example: dd mm yyyy: ")
        task_due_date = datetime.strptime(input_value, "%d %M %Y")
        return task_due_date.strftime("%d %b %Y")
    except ValueError:
        raise ValueError("Error: Invalid datetime provided while entering task due date.")
       
# Function to add a new task to the tasks file       
def add_new_task():
    line = get_task_details()
    with open('tasks.txt', 'a+') as file:
            file.write('\n' + line) 
#endregion
#endregion

#region User Management
#region Add New User
# Function to register a new user
def register(user):
    if(user != 'admin'):
        print(f"user '{user}' is not allowed to register new users.")
        return

    username = str(input("Please enter a username: "))
    password = str(input("Please enter your password: "))

    if username == '' or password == '':
        print("Username or password cannot be empty.")

    password_confirmation = str(input("Please re-enter you password: "))

    if password != password_confirmation:
        print("Passwords did not match! Please start over and try again.")
    else:
        with open('user.txt', 'a+') as file:
            file.write(f"\n{username}, {password}")
#endregion

#region Login functions
# Function to get user credentials from a file
def get_users():
    try:
        users = []
        lines = open('user.txt', 'r').read().split("\n")
        for line in lines:
            user_credentials = line.split(",")
            users.append([user_credentials[0].strip(), user_credentials[1].strip()])
        return users
    except IndexError:
        raise IndexError("Error: Username or password of a record in user.txt is missing.")
    except:
        raise Exception("Error: An error occurred while parsing user credentials from the user.txt file.")        

# Function to find a user's credentials by username
def find_user(users, username):
    for user in users:
        if user[0] == username:
            return user
    else:
        print("Specified user doesn't exist, please start over and provide a valid username.")
        exit()

# Function to handle user login
def login():
    users = get_users()
    username = str(input("Please enter a username: "))
    user_credentials = find_user(users, username)
    
    while True:
        given_password = str(input("Please enter your password: "))

        user = user_credentials[0]
        password = user_credentials[1]

        if(password == given_password):
            print(f"User '{user}' is now logged in.")
            return user
        else:
            print("Incorrect password, please try again:")
#endregion
#endregion

#region Menu
# Function to display program statistics
def show_statistics():
    tasks_file_content = get_tasks_file_content()
    total_tasks_count = len(get_all_tasks(tasks_file_content))
    print(f"Total number tasks: {total_tasks_count}")

    users_count = len(get_users())
    print(f"Total number users: {users_count}")

# Function to check if a user is an admin
def is_admin(user):
    return user == 'admin'

# Function to build the menu options based on the user's role
def build_options(user):
    options = '''Select one of the following options:
    r  - register a user
    a  - add task
    va - view all tasks
    vm - view my tasks
    e  - exit'''
    
    if(is_admin(user)):
        options += '''
    s  - show statistics'''
        
    return options + "\n:"

# Function to get user input for menu options
def get_choice(user):
        print("")
        menu = build_options(user)
        choice = input(menu)
        print("")
        return choice

# Function to present the main menu and handle user input
def present_menu(user):
    while True:
        # Present the menu to the user and 
        # make sure that the user input is converted to lower case.
        try:
            menu = get_choice(user)

            if menu == 'r':
                register(user)
                pass

            elif menu == 'a':
                add_new_task()
                pass

            elif menu == 'va':
                view_tasks_for_all_users()
                pass

            elif menu == 'vm':
                view_tasks_for_user(user)
                pass

            elif menu == 'e':
                print('Goodbye!!!')
                exit()

            elif menu == 's' and is_admin(user):
                show_statistics()
                pass
            else:
                print("You have made entered an invalid input. Please try again")
        except Exception as e:
            print(e)
#endregion

# Entry point of the program
def main():
    user = login()
    present_menu(user)

main()