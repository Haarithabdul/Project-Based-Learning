shoppingList = {}

counter = 0

try:
    while True:
        item = input().strip().upper()

        if item not in shoppingList:
            shoppingList[item] = 1
        else:
            shoppingList[item] += 1


except EOFError:
    for x in sorted(shoppingList):
        print(shoppingList[x], x)
