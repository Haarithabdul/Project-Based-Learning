import re
import sys


def main():
    result = convert(input("Hours: "))
    print(result)

def convert(time):
    pattern =r"([0-9]+)\:?([0-9]{2})? (AM|PM) to? ([0-9]+)\:?([0-9]{2})? (AM|PM)"
    if time := re.search(pattern, time):
        hour1, min1, period1 = time.group(1), time.group(2), time.group(3)
        hour2, min2, period2 = time.group(4), time.group(5), time.group(6)
        min1 = min1 if min1 is not None else "00"
        min2 = min2 if min2 is not None else "00"
        if int(hour1) > 12:
            raise ValueError
        elif int(hour2) > 12:
            raise ValueError
        elif int(min1) > 59:
            raise ValueError
        elif int(min2) > 59:
            raise ValueError
        else:
            converted1 = convert24Hour(int(hour1), min1, period1)
            converted2 = convert24Hour(int(hour2), min2, period2)
            return f"{converted1} to {converted2}"
    else:
        raise ValueError

def convert24Hour(hour, min, period):
    if period == "PM" and hour < 12:
        hour += 12

    if hour == 12 and period == "AM":
        hour = 0

    if len(str(hour)) == 1:
        hour = "0" + str(hour)

    return f"{hour}:{min}"

if __name__ == "__main__":
    main()
