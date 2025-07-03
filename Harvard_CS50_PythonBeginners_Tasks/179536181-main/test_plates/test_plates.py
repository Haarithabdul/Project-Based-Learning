from plates import is_valid

#condition1 = max 6 chars min 2 chars
#condition2 = at least first two chars must be letters
#condition3 = numbers cannot be used in the middle of the plate, only in the end and the first number cannot be 0
#condition4 = no periods, spaces or exclamation marks

def test_con1():
    assert is_valid("C") == False
    assert is_valid("CS50CS50") == False


def test_con2():
    assert is_valid("CS") == True
    assert is_valid("21") == False
    assert is_valid("C5") == False
    assert is_valid("5C") == False

def test_con3():
    assert is_valid("CS50P") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_con4():
    assert is_valid("CS50.") == False
    assert is_valid("CS50!") == False
    assert is_valid("CS 50") == False
