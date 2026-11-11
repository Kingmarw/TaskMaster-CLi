import sqlite3

class Modify():
    def __init__(self):
        from rich import print,box,table
        db = sqlite3.connect("app.db") # connect to database file
        cr = db.cursor()
        print("the saved tasks is :")
        t1 = table.Table(box=box.SQUARE, title="To-Do List")
        t1.add_column("ID", justify="center", style="bold green")
        t1.add_column("Task", justify="left", style="bold blue")
        cr.execute("SELECT * from task")
        for row in cr:
            t1.add_row(str(row[0]), row[1])
        print(t1)
        TaskID = input("Enter task ID > ")
        self.taskid = int(TaskID)
        TaskN = input("Enter new task > ")
        self.taskn = TaskN
        cr.execute(f"UPDATE task SET name = ? WHERE id = ?", (self.taskn,self.taskid))
        db.commit()
        cr.execute("SELECT * from task")
        t_u = table.Table(box=box.SQUARE, title="To-Do List")
        t_u.add_column("ID", justify="center", style="bold green")
        t_u.add_column("Task", justify="left", style="bold blue")
        for row in cr:
            t_u.add_row(str(row[0]), row[1])
        print(t_u)
        print("Edit has been saved successfully.")
        db.close()
