import sqlite3

class Modify():
    def __init__(self):
        db = sqlite3.connect("app.db") # connect to database file
        cr = db.cursor()
        print("the saved tasks is :")
        print("ID | Task")
        cr.execute("SELECT * from task")
        for row in cr:
            print(f"{row[0]}  | {row[1]}")
        TaskID = input("Enter task ID > ")
        self.taskid = int(TaskID)
        TaskN = input("Enter new task > ")
        self.taskn = TaskN
        cr.execute(f"UPDATE task SET name = ? WHERE id = ?", (self.taskn,self.taskid))
        db.commit()
        print("ID | Task")
        cr.execute("SELECT * from task")
        for row in cr:
            print(f"{row[0]}  | {row[1]}")
        print("Edit has been saved successfully.")
        db.close()
