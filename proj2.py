total = 0

while True:
    expense = input("enter expense amount (or 'quit' to stop): ")

    if expense == "quit":
        break

    total = total + int(expense)

print("total spent:", total)
