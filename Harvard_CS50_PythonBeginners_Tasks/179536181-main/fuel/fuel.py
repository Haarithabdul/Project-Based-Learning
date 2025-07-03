while True:
    try:
        fuel = input("How much fuel is left(Fraction)\n")
        splitFuel = fuel.split("/")
        X = int(splitFuel[0])
        Y = int(splitFuel[1])
        percFuel = round((100 // Y) * X)

        if percFuel <= 1:
            print("E")
            break
        elif 99 <= percFuel <= 100:
            print("F")
            break
        elif 1 < percFuel < 99:
            print(percFuel, "%", sep = "")
            break

    except ValueError:
        pass
    except ZeroDivisionError:
        pass
