import sqlite3
from datetime import datetime

connection = sqlite3.connect('budget.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, id INTEGER)",
               "CREATE TABLE IF NOT EXISTS transactions(user_id INTEGER, amoutn FLOAT, date DATE TIME)")

choice = None

while choice != "6":
    print()
    print("1) Display Users")
    print("2) Add User")
    print("3) Update Spending")
    print("4) Reset Spending")
    print("5) Delete User")
    print("6) Quit")

    choice = input("> ")
    print()

    match choice:
        case "1":
            cursor.execute("SELECT * FROM users ORDER BY spending")

            
            print("{:>10}  {:>10}  {:>10}".format("Name", "Spending", "DateTime"))

        
            for record in cursor.fetchall():
                print("{:>10}  {:>10}  {:>10}".format(record[0], record[1], record[2]))

        case "2":
            try: 
                name = input("Name: ")
                spending = 0.0
                date = datetime.now()
                values = (name, spending,date)

                cursor.execute("INSERT INTO users VALUES (?,?,?)", values)
                connection.commit()

            except ValueError:
                print("Invalid name: ")

connection.close()