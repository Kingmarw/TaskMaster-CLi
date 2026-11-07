# here is we will build create task Class
import sqlite3

class Create:
    def __init__(self):
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute("CREATE TABLE if not exists task(id INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
        Task = input("Enter Your Task > ")
        self.task = Task
        cr.execute("INSERT INTO task(name) VALUES(?)",(self.task,))
        db.commit()
        print(f"Your task is {self.task}")
        print(f"Your Task has been saved in Database ")
        print("ID | Task")
        cr.execute("SELECT * from task")
        for row in cr:
            print(f"{row[0]}  | {row[1]}")
        db.close()

