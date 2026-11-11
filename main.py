# To Do List CLi
# Ok, so we should make an input to take data from user

# Hmmm, we have a problem now as a To Do list system we will face a problem. the problem is there's many
# choices like Modify task , Delete task, Add Task
# So, we will add this feature in our system

# Hmm, after Run this version of app. I found a problem that happend. this problem is data type that 
# return from choice input was string but now when i put Varibale "choice" in brackets of "int" class 
# to convert it into an integer. it's working

# Ok , now we should put the input with conditions in Loop to continue application without stopping
from time import sleep
from rich.console import Console
from rich import print,box,table
import create_task, delete_task,modify_task,view_tasks,export_tasks
import pyfiglet
import os
console = Console()
os.system("cls") # clean screen
# console.clear()

pyfiglet.print_figlet("Task Master CLi",font="slant",colors="red") # TaskMaster Cli logo
console.log("Hello, world")


pyfiglet.print_figlet("Developed by Kingmarw", font="mini")
while True:
    print("""
        Choose Your Choice:
        [1] Create Task
        [2] Modify Task
        [3] Delete Task
        [4] View Tasks 
        [5] Export Tasks
        [6] Exit
    """) 
    choice = input("Enter your Choice > ")

    try:
        if int(choice) == 1:
            print("Your choice is \"Create Task\"")
            create_task.Create()
        elif int(choice) == 2:
            print("Your choice is \"Modify Task\"")
            modify_task.Modify()
        elif int(choice) == 3:
            print("Your choice is \"Delete Task\" -> you can write command \"all\" to delete all items")
            delete_task.Delete()
        elif int(choice) == 4:
            os.system("cls") # clean screen
            pyfiglet.print_figlet("Task Master CLi",font="slant",colors="red") # TaskMaster Cli logo
            pyfiglet.print_figlet("Developed by Kingmarw", font="mini")
            print("Your choice is \"View Tasks\"")
            print("Your To-Do List today is")
            view_tasks.View()
        elif int(choice) == 5:
            print("Your choice is \"Export Tasks\"")
            export_tasks.Export()
        elif int(choice) == 6:
            print("Your choice is \"Exit\" See you soon")
            break
        else:
            print("Sorry, it's invalid command try again later")
    except Exception as e:
        print("Invalid input")
        print(f"Err yasta {e}")

    print("=" * 50)