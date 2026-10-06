import sqlite3

connection = sqlite3.connect("repair.db")

connection.execute("""
ALTER TABLE repairs
ADD COLUMN status TEXT DEFAULT 'Pending'
""")

connection.commit()
connection.close()