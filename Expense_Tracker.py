expenses = []
total = 0

for i in range(3):
    expense = input("Expense: ")
    amount = float(input("Amount: "))

    expenses.append((expense, amount))
    total = total + amount

print("Total spent:", total)
print("\nExpenses:")

for expense, amount in expenses:
    print(expense, "-", amount)