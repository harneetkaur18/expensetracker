# Expense Tracker Project
expenses = []  # List of all expenses in the form of dictionary

print("Welcome to Expense Tracker")

while True:
    print("\n=== Menu ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = input("Please enter your choice: ")

    # 1. Add Expense
    if choice == "1":
        date = input("Enter the date: ")
        category = input("Enter the category: ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    # 2. View All Expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            for i in range(len(expenses)):
                print(
                    f"{i+1}. Date: {expenses[i]['date']}, "
                    f"Category: {expenses[i]['category']}, "
                    f"Description: {expenses[i]['description']}, "
                    f"Amount: {expenses[i]['amount']}"
                )

    # 3. View Total Spending
    elif choice == "3":
        total = 0
        for eachExpense in expenses:
            total += eachExpense["amount"]
        print("Total Expenses =", total)

    # 4. Exit
    elif choice == "4":
        print("Thank you for using our Expense Tracker")
        break

    else:
        print("Invalid choice, try again")
