def main():
    ans = input("Greeting: ").title()
    print(value(ans))

def value(ans):
    if ans.find("Hello") == 0:
        return 0
    elif ans.find("H") == 0:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
