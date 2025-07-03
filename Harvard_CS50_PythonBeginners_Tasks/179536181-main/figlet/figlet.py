import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fontList = figlet.getFonts()


def main():
    commandLine = sys.argv

    if len(commandLine) == 1:
        say = input("Input: ")
        randomFont(say)

    elif len(commandLine) == 3:
        font = sys.argv[2]

        if font not in fontList:
            raise Exception

        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            say = input("Input: ")
            figletFont(font, say)
        else:
            raise Exception

    else:
        raise Exception


def figletFont(Ifont, say):
    figlet.setFont(font=Ifont)
    print(figlet.renderText(say))


def randomFont(say):
    ranFont = random.choice(fontList)
    figlet.setFont(font=ranFont)
    print(figlet.renderText(say))


if __name__ == "__main__":
    main()
