import random
import sys

def main():
    score = 0
    level = int(get_level())
    for i in range (10):
        wrong = 0
        question = generate_integer(level)

        while True:
            userAns = int(input(f"{question[0]} + {question[1]} = "))

            if userAns == question[2]:
                score += 1
                break
            else:
                print("EEE")
                wrong += 1

            if wrong == 3:
                print(f"{question[0]} + {question[1]} = {question[2]}")
                break

    print(f"Your score was {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level == "1" or level == "2" or level == "3":
            return level
        else:
            pass

def generate_integer(level):
    numList = []
    if level == 1:
        X = random.randrange(10)
        Y = random.randrange(10)
        ans = X + Y
        numList.append(X)
        numList.append(Y)
        numList.append(ans)
        return numList
    if level == 2:
        X = random.randrange(100)
        Y = random.randrange(100)
        ans = X + Y
        numList.append(X)
        numList.append(Y)
        numList.append(ans)
        return numList
    if level == 3:
        X = random.randrange(1000)
        Y = random.randrange(1000)
        ans = X + Y
        numList.append(X)
        numList.append(Y)
        numList.append(ans)
        return numList


if __name__ == "__main__":
    main()
