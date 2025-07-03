def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    dollars1 = float(dollars.removeprefix("$"))
    return dollars1


def percent_to_float(percent):
    percent1 = float(percent.removesuffix("%")) / 100
    return percent1

main()
