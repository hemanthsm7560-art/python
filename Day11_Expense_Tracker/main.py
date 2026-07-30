
from expense import Expense
from file_handler import load_expenses, save_expenses
expenses = load_expenses()


def add_expense():
    title = input("Enter expense title:")
    amount = float(input("Enter Expense amount:"))
    category = input("Enter Expense Category:")

    expense = Expense(title, amount, category)
    expenses.append(expense)

    save_expenses(expenses)
    print("\n Expense Added Succcessfully! \n")


def view_expenses():
    if len(expenses) == 0:
        print("\nNo expenses found!\n")
        return

    print("\n------ All Expenses ------")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense.title} | ₹{expense.amount} | {expense.category}")


while True:
    print("\n =====EXPENSE TRACKER===== \n")
    print("1. Add Expense")
    print("2. View Expense")
    print("3.search by category")
    print("4. Total Expense")
    print("5. Delete Expense")
    print("6.Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        add_expense()

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    elif choice == "2":
        view_expenses()

    else:
        print("Invalid Choice!")
