# from rich import inspect
# from rich.color import Color
# color = Color.parse("red")
# inspect(color, methods=True)
# print(d)
# compl = 5+6j
# print(compl * compl.conjugate())
# for i in :
    # console.status("Monkeying around...", speed=1)
# print(x)


# from rich.console import Console
# from rich.table import Table

# table = Table(title="Star Wars Movies")

# table.add_column("Released", justify="right", style="cyan", no_wrap=True)
# table.add_column("Title", style="magenta")
# table.add_column("Box Office", justify="right", style="green")

# table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
# table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
# table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
# table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

# console = Console()
# console.print(table)

# from rich.tree import Tree
# from rich import print

# tree = Tree("Rich Tree")
# tree.add("foo")
# tree.add("bar")
# print(tree)

# import sys
# from rich.console import Console
# from datetime import datetime

# with open("report.txt", "wt") as report_file:
#     console = Console(file=report_file)
#     console.rule(f"Report Generated {datetime.now().ctime()}")


# """template script for writing to a csv file"""
# import csv

# # open new file for writing - will erase file if it already exists -
# csvfile = open('example.csv', 'w', newline='', encoding='utf-8')

# # make a new variable - c - for Python's CSV writer object -
# c = csv.writer(csvfile)

# # write a column headings row - do this only once -
# c.writerow( ['name','address','job'] )

# # call some function that returns a list --
# # for purposes of the template, here is a list of lists -
# the_list = [
#     ['Alice', 'Gainesville, Florida', 'chef'],
#     ['Bob', 'Chicago, Illinois', 'writer'],
#     ['Ted', 'Miami, Florida', 'driver'],
#     ['Carol', 'Portland, Oregon', 'executive']
# ]

# # use a for-loop to write each row into the CSV file
# for item in the_list:
#     # write one row to csv — item MUST BE a LIST
#     c.writerow(item)

# # save and close the file
# csvfile.close()