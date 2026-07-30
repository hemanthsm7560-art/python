from expense import Expense


def load_expenses():
    expenses = []
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 3:
                    title = data[0]
                    amount = float(data[1])
                    category = data[2]
                    expenses.append(Expense(title, amount, category))
    except FileNotFoundError:
        pass
    return expenses


def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(str(expense) + "\n")
