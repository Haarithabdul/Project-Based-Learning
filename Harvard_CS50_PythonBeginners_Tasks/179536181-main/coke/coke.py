price = 50
amountPaid = 0
coins = [25, 10, 5]

while amountPaid < 50:
    paid = int(input("Insert Coin: "))
    if paid in coins:
        amountPaid += paid
    else:
        print("Invalid coin")

    if amountPaid <= 50:
        print(f"Amount Due: {price - amountPaid}")
    elif amountPaid > 50:
        print(f"Change Owed: {amountPaid - price}")
