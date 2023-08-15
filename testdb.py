import sqlite3


con=sqlite3.connect('database.db')
cur=con.cursor()
statement1= f"SELECT email, password from DATA"

cur.execute(statement1)

output = cur.fetchall()

for email, password in output:
    print(email, password.decode('utf-8'))

con.commit()
con.close()
