import inflect

p = inflect.engine()

nameList = []

try:
    while True:
        name = input()
        nameList.append(name)
except EOFError:
        print(f"Adieu, adieu, to {p.join(nameList)}")
