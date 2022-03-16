import sqlite3

connection = sqlite3.connect('budget.db')
fursor = connection.cursor()


connection.close()