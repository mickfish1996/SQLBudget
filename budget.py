import sqlite3

connection = sqlite3.connect('budget.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, spending FLOAT)")

choice = None

while choice != "6":
    print("1) Display Users")
    print("2) Add User")
    print("3) Update Spending")
    print("4) Reset Spending")
    print("5) Delete User")
    print("6) Quit")

    choice = input("> ")

    match choice:
        case "1":
            cursor.execute("SELECT * FROM users ORDER BY spending")

            
            print("{:>10}  {:>10}" .format("Name", "Spending"))

        
            for record in cursor.fetchall():
                print("{:>10}  {:>10}".format(record[0], record[1]))

        case "2":
            try: 
                name = input("Name: ")
                spending = 0.0
                values = (name, spending)

                cursor.execute("INSERT INTO users VALUES (?,?)", values)
                connection.commit()

            except ValueError:
                print("Invalid name: ")

connection.close()