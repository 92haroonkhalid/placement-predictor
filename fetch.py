# to fetch data from database
import sqlite3

con = sqlite3.connect("Project/SQL/users.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

con.close()