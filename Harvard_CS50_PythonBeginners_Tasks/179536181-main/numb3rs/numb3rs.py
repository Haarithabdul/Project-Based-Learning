import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$"
    if numbers := re.search(pattern, ip):
        for i in range(1,5):
            if int(numbers.group(i)) > 255 or int(numbers.group(i)) < 0:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
