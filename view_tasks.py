import sqlite3
class View():
    def __init__(self) -> None:
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        print("ID | Task")
        cr.execute("SELECT * from task")
        for row in cr:
            print(f"{row[0]}  | {row[1]}")
        db.close()