def main():
    fuel = input("How much fuel is left(Fraction)\n")
    percentage = convert(fuel)
    print(gauge(percentage))


def convert(fuel):
    splitFuel = fuel.split("/")
    X = int(splitFuel[0])
    Y = int(splitFuel[1])
    percFuel = round((100 // Y) * X)
    return percFuel


def gauge(percFuel):
    if percFuel <= 1:
        return "E"
    elif 99 <= percFuel <= 100:
        return "F"
    elif 1 < percFuel < 99:
        return f"{percFuel}%"


if __name__ == "__main__":
    main()
