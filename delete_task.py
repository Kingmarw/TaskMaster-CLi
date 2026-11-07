# here's we will build delete tasks Class

import sqlite3

class Delete:
    def __init__(self) -> None:
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        Task = input("Enter Your Task > ") # DELETE FROM recharge_codes WHERE `recharge_codes`.`code` = "BADR-554C19"
        self.task = Task
        if self.task == "all":
            cr.execute(f"DELETE from task")
            cr.execute(f"DELETE from sqlite_sequence WHERE name='task'")
            print("delete all data from database has been done successfully")
        else:
            cr.execute(f"DELETE FROM task WHERE `task`.`name` = ?", (self.task,))
            print(f"Your task is {self.task}")
            print(f"Your Task has been saved in Database ")
        db.commit()
        print("ID | Task")
        cr.execute("SELECT * from task")
        for row in cr:
            print(f"{row[0]}  | {row[1]}")
        db.close()