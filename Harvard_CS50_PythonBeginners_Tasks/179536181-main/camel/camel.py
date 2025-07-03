camel = input("Enter camelCase: ").strip()
for i in camel:
    if i.isupper() == True:
        i = i.lower()
        print("_", end="")
    print(i, end="")
print()
