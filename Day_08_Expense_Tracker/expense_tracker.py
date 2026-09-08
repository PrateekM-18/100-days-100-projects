from datetime import date


expenses = []


def add_expense():  #Add expenses 

    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    
    category = input("Enter the category: ")
    description = input("Enter the description: ")


    expense = {
        "Amount" : amount,
        "Category" : category,
        "Description" : description,
        "Date" : date.today()
    }
    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():    #View Expenses

    if not expenses:
        print("\nNo Expenses found.")
        return
    
    print("\n===== ExpenseList =====")

    for i, expense in enumerate(expenses):

        print(f"{i+1}. "
              f"Amount: {expense['Amount']}, "
              f"Category: {expense['Category']}, "
              f"Description: {expense['Description']}, "
              f"Date: {expense['Date']}")


def calculate_total_expenses(): #Calculate Total Expenses

    if not expenses:
        print("\nNo expenses found.")
        return

    total = 0

    for expense in expenses:
        total += expense['Amount']
        print(f"\nTotal Expenses: {total:.2f}")

        
def delete_expense():   #Delete Expenses

    if not expenses:
        print("\nNo expense to delete.")
        return

    view_expenses()

    try:
        index = int(input("Enter the index of the expense to delete: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    if 0 <= index < len(expenses):
        deleted_expense = expenses.pop(index)
    
        print(
            f"Deleted expense: "
            f"amount: {deleted_expense['Amount']}, "
            f"Amount: {deleted_expense['Category']}, "
            f"Description: {deleted_expense['Description']}, "
            f"Date: {deleted_expense['Date']}"
        )

    else :
        print("Invalid Index, Please try again.")


while True:
    print("\n===== ExpenseTracker =====")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Delete Expense")
    print("4. Show Total")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
         delete_expense()

    elif choice == 4:
        calculate_total_expenses()

    elif choice == 5:
        print("Exiting the program. Thank You for choosing Expense Tracker!")
        break

    else:
        print("Invalid Choice, Please select from 1 - 5.")
