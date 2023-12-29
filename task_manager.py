# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date
    
# Reads task_overview and user_overview
def user_read():
        # Create tasks.txt if it doesn't exist
    if not os.path.exists("task_overview.txt"):
        with open("task_overview.txt", "w") as task_over:
            pass

    with open("task_overview.txt", 'r') as task_over: 
        task_view = task_over.read().split("\n")
        task_view = [t for t in task_view if t != ""] 
        
    report = []   
        
    for ut_str in task_view:

        total_u = {}

        # Split by semicolon and manually add each component
        task_components = ut_str.split(";")
        total_u['amount'] = task_components[0]
        total_u['task_completed'] = task_components[1]
        total_u['task_not_comp'] = task_components[2]
        total_u['overdue'] = task_components[3]
        total_u['total_users'] = task_components[4]
            
        report.append(total_u)
    
    if not os.path.exists("user_overview.txt"):
        with open("user_overview.txt", "w") as user_over:
            pass
     
    with open("user_overview.txt", "r") as user_over:   
        task_user = user_over.read().split("\n")
        task_user = [t for t in task_user if t != ""]
        
    user_report = []  
        
    for u_str in task_user:

        total_u = {}

        # Split by semicolon and manually add each component
        task_components = u_str.split(";")
        total_u['user_tasks'] = task_components[0]
        total_u['total_percent'] = task_components[1]
        total_u['percent_comp'] = task_components[2]
        total_u['percent_not_comp'] = task_components[3]
        total_u['percent_overdue'] = task_components[4]
            
        user_report.append(total_u)

# Displays values of task_list.               
def disp_task(t):
    disp_str = f"Id number: \t\t{t['task_id']} \n\n"
    disp_str += f"Task: \t\t {t['title']}\n"
    disp_str += f"Assigned to: \t {t['username']}\n"
    disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Task Description: \n {t['description']}\n"
    disp_str += f"Task completion: \t {t['completed']}\n"
    print(disp_str)
    
    

# writes altered task_list to .txt                      
def task_write(): 
    
    # writes task_list to tasks.txt
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No",
                t['task_id']
                
                ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))


def task_update(select_task):
    
    task_username = input("Name of person assigned to task: ")
    
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
    else:
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")

        
            # Then get the current date.
        curr_date = date.today()
        
        # Add the data to the file task.txt and
        # Include 'No' to indicate if the task is complete.'''
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False,
        }
        
        # Updates the chosen task.
        for i in task_list[select_task]:
            task_list[select_task].update(new_task)

#Registers New user         
def reg_user():
    

    new_username = input("New Username: ")
    
    while new_username in username_password:
        print("username already exist!")
        new_username = input("Please try a different username: ")
    else:
            # - Request input of a new password
        new_password = input("New Password: ")

                # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

                # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
                    # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
                
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))

            # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match")
     
def add_task():
    '''Allow a user to add a new task to task.txt file
    Prompt a user for the following: 
     - A username of the person whom the task is assigned to,
     - A title of a task,
     - A description of the task and 
     - the due date of the task.'''
     
    print("----------------Add--A--New--Task-----------------------------------\n")
    
    task_username = input("Name of person assigned to task: ")
    
    # Checks input against username keys.
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        
    else:
        
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")
        
        print("\nTask Successfully added.")
       
            # Then get the current date.
        curr_date = date.today()
        
        # Creates task_id
        user_id = 1
        for i in task_list:
            user_id += 1
        
        # Add the data to the file task.txt and
        # Include 'No' to indicate if the task is complete.''' 
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False,
            "task_id" : str(user_id)
        }

        task_list.append(new_task)
        task_write()

def view_all():
    
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling) 
    '''
    
    print("----------------VIEW--ALL--TASKS-----------------------------------\n")
    for t in task_list:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            disp_str += f"Task completion: \t {t['completed']}\n"
            print(disp_str)
            print("-------------------------------------------------------------------\n")

def view_mine():
    
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)
    '''

    
    print("----------------VIEW--MY--TASK---------------------------------\n")
    
    # Searches task_list for current username.
    for t in task_list: 
        
        if t['username'] == curr_user:
            disp_task(t)
            print("-------------------------------------------------------------------\n")

     
    select_task = input("Please select a task or type -1 to return to the main menu: ")
    print()
    

    
    # Enter -1 to exit.
    while select_task != "-1":
        
        # Checking input is a number.
        if str(select_task).isdigit():
            select_task = int(select_task)-1
            
        # Gets username and task Id number. 
        user = task_list[select_task]['username']
        user_task = task_list[select_task]['task_id']
        
        # Turns select_task to a string.
        str_task = (select_task)+1
        task_id = str(str_task)
        
        # Checks input valid to task_id and task username is same as current user.
        if task_id == user_task and user == curr_user:
            for t in task_list:
                if t['task_id'] == task_id:
                    disp_task(t) 
                 
        else:
            print("please enter correct task id.")
            break
        
        completed = input("Have you completed this task (y or n): ")
        
        
        # Change complete to yes.
        if completed == "y":
                    
            task_list[select_task].update({'completed': True})
            task_write()

            print("\nTask successfully updated.")
            disp_task(t)
        
        #Allow user to edit task.    
        elif completed == "n":
            
            update = input("\nWould you like to update this task (y/n): ")
            if update =="y":
                task_update(select_task)
                task_write()
                        
                print("\nTask successfully updated.")                   
            print("-----------------------------------------------------\n")
        else:
            print("Invalid Entry.")
        
        break

 #-------------------------------------------------------------------------------------------------             
            
def gen_reports():

    # Creates or opens task & user overview.txt
    user_read()
  
    num_of_task = 0
    task_comp = 0
    task_uncomp = 0
    overdue = 0
    total_users = 0
    user_tasks = 0
    curr_comp = 0
    curr_non_comp = 0
    curr_overdue = 0
    
    # Adds up the number of tasks
    for t in task_list:
        num_of_task += 1
        if t["completed"] == True:
            task_comp += 1
        elif t["completed"] == False and t["due_date"] < datetime.today():
            overdue += 1
            task_uncomp += 1
        elif t["completed"] == False:
            task_uncomp += 1
    
        # Adds up tasks assigned to user.
        if t['username'] == curr_user:
            user_tasks += 1 
            if t['completed'] == True:
                curr_comp += 1
            elif t['completed'] == False and t['due_date'] < datetime.today():
                curr_overdue += 1
                curr_non_comp += 1
            elif t['completed'] == False:
                curr_non_comp += 1
            
    # Adds the amount of users.      
    for t in username_password:
        total_users += 1
        
    report = [] 
    
    # Sorts out addition variables into dictioanry.     
    new_report = {
        "amount" : str(num_of_task),
        "task_completed" : str(task_comp),
        "task_not_comp" : str(task_uncomp),
        "overdue" : str(overdue),
        "total_users" : str(total_users)
    }
    
    report.append(new_report)
    
    # Adds list to .txt file
    with open("task_overview.txt", "w") as task_over:
        report_list_to_write = []
        for t in report:
            str_attrs = [
                t['amount'],
                t['task_completed'],
                t['task_not_comp'],
                t['overdue'],
                t['total_users']        
                ]
            report_list_to_write.append(";".join(str_attrs))
        task_over.write("\n".join(report_list_to_write))  
    
    print("----------------Generate--Reports-------------------------\n")
    for t in report:
        disp_str = f"Current tasks:\t\t{t['amount']}\n"
        disp_str += f"Completed Tasks:\t{t['task_completed']}\n"
        disp_str += f"Uncompleted Tasks:\t{t['task_not_comp']} \n"
        disp_str += f"Overdue Tasks:\t\t{t['overdue']}\n"
        disp_str += f"Total number of users:\t{t['total_users']}\n"
        print(disp_str)
        print("-----------------------------------------------------\n")
    
    # Works out percentage.
    percent_user_task = round(user_tasks / num_of_task * 100, 2)
    percent_comp = round(curr_comp / user_tasks * 100, 2)
    percent_non_comp = round(curr_non_comp / user_tasks * 100, 2)
    percent_overdue = round(curr_overdue / user_tasks * 100, 2)
    
    # Store percent dictionary
    user_report = []
           
    new_user_report = {
        "user_tasks" : str(user_tasks),
        "total_percent" : str(percent_user_task),
        "percent_comp" : str(percent_comp),
        "percent_not_comp" : str(percent_non_comp),
        "percent_overdue" : str(percent_overdue)
    }
    
    user_report.append(new_user_report)
    
    # Write List to .txt
    with open("user_overview.txt", "w") as user_over:
        user_list_to_write = []
        for t in user_report:
            str_attrs = [
                t['user_tasks'],
                t['total_percent'],
                t['percent_comp'],
                t['percent_not_comp'],
                t['percent_overdue']        
                ]
            user_list_to_write.append(";".join(str_attrs))
        user_over.write("\n".join(user_list_to_write))  
       
    print(f"--------------------{curr_user}--Reports-------------------------\n\n")
    
    for t in user_report:
        disp_str = f"{curr_user} has:\t\t{t['user_tasks']} tasks. \n"
        disp_str += f"You have {t['total_percent']}% of the tasks.\n"
        disp_str += f"You have completed {t['percent_comp']}% of your tasks.\n"
        disp_str += f"You still have {t['percent_not_comp']}% to complete.\n"
        disp_str += f"You have {t['percent_overdue']}% of your tasks overdue.\n"
        print(disp_str)
    print("-----------------------------------------------------\n\n")
            
            
  #-------------------------------------------------------------------------------      
    
def statistics():
    
    # Gets info  from user and task .txt.
    for u in user_details:
        print(f"Username: \t {u['username']} \t\t  Password: {u['password']}\n")
        print("-------------------------------------------------------------------\n")
        for t in task_list:
            if t['username'] == u['username']:
                disp_task(t)
        print("-------------------------------------------------------------------\n")
       
    

DATETIME_STRING_FORMAT = "%Y-%m-%d"


# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

# List of task dictionaries.
task_list = []


for t_str in task_data:
    
    curr_t = {}

    # Split by semicolon and manually add each component to curr_t
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False
    curr_t['task_id'] = task_components[6]
    
    
  
    task_list.append(curr_t)



#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")
    user_data = [t for t in user_data if t != ""]
    
# Contains dictionary of username and passwords.   
user_details = []


for u_str in user_data:
    
    curr_user = {}

    # Split by semicolon and manually add each component
    task_components = u_str.split(";")
    curr_user['username'] = task_components[0]
    curr_user['password'] = task_components[1]
     
    user_details.append(curr_user)

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
                 
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()


    elif menu == 'a':
        add_task()


    elif menu == 'va':
        view_all()


    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        gen_reports()

    elif menu == 'ds' and curr_user == 'admin': 
        statistics()

    elif menu == 'e':
        print('Goodbye!!!')
        exit() 

    else:
        print("You have made a wrong choice, Please Try again")