import sqlite3
from datetime import datetime

connection = sqlite3.connect('budget.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS transactions(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, amount FLOAT, date_info DATETIME)")



choice = None

while choice != "5":
    print()
    print("1) Display Users")
    print("2) Add spending")
    print("3) Update Spending")
    print("4) Delete Spending")
    print("5) Quit")

    choice = input("> ")
    print()

    match choice:
        case "1":
            today = datetime.today()
            current_month = datetime(today.year, today.month, 1)

            value = (current_month,)
            cursor.execute("SELECT * FROM transactions WHERE date_info >= date('now','start of month')")

            
            print("{:>10}  ${:>10}  {:>10}".format("ID", "AMOUNT", "DATE"))
            print("-----------------------------------")
            sum = 0
            for record in cursor.fetchall():
                print("{:>10}  ${:>10}  {:>10}".format(record[0], record[1], record[2]))
                sum += record[1]

            print("-----------------------------------")
            print(f"Sum: ${sum}")

        case "2":
            try: 
                amount = float(input("Enter Amount: "))
                date = datetime.today().strftime('%Y-%m-%d')
                values = (amount, date)

                cursor.execute("INSERT INTO transactions(amount, date_info) VALUES (?,?)", values)
                connection.commit()

            except ValueError:
                print("Invalid Amount: ")

        case "3":
            try:
                modify = int(input("Enter the transaction ID that you would like to modify: "))
                
                new_amount = float(input("Enter the new amount of the transaction: "))
                values = (new_amount, modify)
                cursor.execute("UPDATE transactions SET amount = ? WHERE ID = ?", values)
                connection.commit()

            except ValueError:
                print("Invalid ID")

        case "4":
            try:
                id = int(input("Enter the transaction ID that you would like to DELETE: "))

                values = (id,)

                cursor.execute("DELETE FROM transactions WHERE ID = ?", values)
                connection.commit()

            except ValueError:
                print("Invalid ID")



connection.close()