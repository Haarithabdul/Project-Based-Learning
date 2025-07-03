import random
import sys

while True:
    try:
        num = int(input("Enter a random number: "))
        guess = int(input("Guess the number: "))

        num = random.randint(1, num)

        while guess > num:
            print("Too large!")
            guess = int(input("Guess the number: "))

        while guess < num:
            print("Too small!")
            guess = int(input("Guess the number: "))

        if guess == num:
            print("Just right!")
            sys.exit()

    except Exception:
        pass
