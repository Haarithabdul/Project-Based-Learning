import re
import sys

monthList = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

def main():
    mdyDate = input("Date: ").strip()
    mdyDate = checkMDYformat(mdyDate)
    newDate = convertForm(mdyDate)
    print(newDate)


def checkMDYformat(date):
    try:
        if date[0].isalpha():
            date = date.replace(",", "")
            dateList = date.split(" ")
            month = monthList[dateList[0].title()]
            newDate = f"{month}/{dateList[1]}/{dateList[2]}"
            date = newDate

        if result := re.search(r"(\d\d?)/(\d\d?)/(\d\d\d\d)", date):
            if int(result.group(1)) > 12:
                sys.exit()
            elif int(result.group(2)) > 31:
                sys.exit
            else:
                return date

    except Exception:
        main()


def convertForm(oldDate):
    try:
        month, date, year = oldDate.split("/")

        if int(month) < 10:
            month = month.zfill(2)
        if int(date) < 10:
            date = date.zfill(2)

        newDate = f"{year}-{month}-{date}"
        return newDate

    except Exception:
        main()


if __name__ == "__main__":
    main()
