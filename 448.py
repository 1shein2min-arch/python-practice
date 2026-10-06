import sqlite3

connection = sqlite3.connect("repair.db")

print("Database connected!")

connection.close()