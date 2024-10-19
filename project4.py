
#create a simple expenses tracking program that allows user to record their expenses in a file
#Add expenses
#View expenses
#Write expenses to file
#using class and filehandling


def expense_tracker():
    expenses = []
    while True:
        print("1.Add Expense")
        print("2.View Expenses")
        print("3.Exit")
        choice = input("choose an option:")

        if choice == "1":
            expense = input("Enter date,category,amount:")
            expenses.append(expense)
            print("Expense added successfully.")
        elif choice == "2":
            print("Date\tCategory\tAmount")
            for expense in expenses:
                print(expenses)
        elif choice == "3":
            break
        else:
            print("invalid option.please choose again")
expense_tracker()