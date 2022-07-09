import sqlite3

def adduser(user, mail, phone):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS users
        (username text, email text, phone integer)""")

    c.execute("INSERT INTO users VALUES (?,?,?)", (user,mail,phone))
    conn.commit()
    conn.close()
