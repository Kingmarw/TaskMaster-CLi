import sqlite3

class View():
    def __init__(self) -> None:
        from rich import print,box,table
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        table = table.Table(box=box.SQUARE, title="To-Do List")
        table.add_column("ID", justify="center", style="bold green")
        table.add_column("Task", justify="left", style="bold blue")
        cr.execute("SELECT * from task")
        for row in cr:
            table.add_row(str(row[0]), row[1])
        print(table)
        db.close()