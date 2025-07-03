#condition1 = max 6 chars min 2 chars
#condition2 = at least first two chars must be letters
#condition3 = numbers cannot be used in the middle of the plate, only in the end and the first number cannot be 0
#condition4 = no periods, spaces or exclamation marks



def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    try:
        digits = 0

        if len(plate) > 6:
            return False
        elif len(plate) < 2:
            return False

        for char in plate:
            if char.isalnum() == False:
                return False

        if plate[0].isalpha() == False or plate[1].isalpha() == False:
            return False

        for char in plate:
            if char.isdigit():
                digits += 1
            if digits == 1 and char == "0":
                return False

        if digits > 0:
            if plate[len(plate) - 1].isalpha():
                return False

        return True

    except Exception:
        return False


if __name__ == "__main__":
    main()
