from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    inpDate = checkDateFormat(input("Date of birth: ").strip())
    ageMinutes = calcAgeMinutes(inpDate)
    output = f"{p.number_to_words(ageMinutes, andword="")} minutes".capitalize()
    print(output)



def checkDateFormat(inpDate):
    pattern = r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$"

    if check := re.search(pattern, inpDate):
        return inpDate
    else:
        sys.exit("Incorrect format")


def calcAgeMinutes(birthday):
    try:
        birthYear, birthMonth, birthDate = birthday.split("-")

        newBirthday = date(int(birthYear), int(birthMonth), int(birthDate))

        currentDate = date.today()

        timeDiff = currentDate - newBirthday

        timeDiffMinutes = timeDiff.days * 24 * 60

        return timeDiffMinutes

    except ValueError:
        sys.exit("Invalid range")


if __name__ == "__main__":
    main()
