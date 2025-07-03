def main():
    time = input("What is the time?\n").strip()
    CheckTime = convert(time)
    if 7.00 <= CheckTime <= 8.00:
        print("breakfast time")
    elif 12.00 <= CheckTime <= 13.00:
        print("lunch time")
    elif 18.00 <= CheckTime <= 19.00:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60

if __name__ == "__main__":
    main()
