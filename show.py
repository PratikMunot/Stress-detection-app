import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()
def show():
    a = cur.execute("SELECT * from admin")
    print(list(a))

show()



