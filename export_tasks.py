import csv
import sqlite3

class Export():
    def __init__(self):
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute("SELECT * from task")
        rows = cr.fetchall()
        with open('exported_tasks/tasks.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Task'])
            writer.writerows(rows)
        print("Tasks have been exported to tasks.csv")
        db.close()