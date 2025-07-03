#BLACKJACK


#Imports
import pydealer
import sys


#Create deck object
deck = pydealer.Deck()


with open("coins.txt", "r") as file:
    fileCoins = file.read()
    coins = int(fileCoins)

specValues = ("Queen", "King", "Jack", "Ace")

specTens = {"Queen":10, "King":10, "Jack":10, "Ace":11}


class Dealer:
    def __init__(self, *args):
        self.dealerCards = list(args)

    def Display(self):
        print(f"\nDealer's cards: ")
        for card in self.dealerCards:
            print(card)
        print()

    def dealerHit(self):
        newCard = deck.deal(1)
        self.dealerCards.append(newCard)
        return self.dealerCards

    def calcScore(self):
        #Takes the values from each card given
        dealerValues = []
        totalScore = 0
        aceCount = 0
        for count in range(len(self.dealerCards)):
            card = self.dealerCards[count]
            card = str(card)
            card = card.split("\n")
            for x in card:
                x = x.split(" ")
                for i in x:
                    if i.isdigit() == True or i in specValues:
                        dealerValues.append(i)
        for val in dealerValues:
            if val in specValues:
                val = specTens[val]
            if val == "Ace":
                aceCount += 1

            totalScore += int(val)

        if totalScore > 21 and aceCount >= 1:
            totalScore -= 10

        return totalScore


class Player:
    def __init__(self, coins, *args):
        self.playerCards = list(args)
        self.coins = coins

    def __str__(self):
        print()
        return str(self.coins)

    def Display(self):
        print(f"\nYour cards: ")
        for card in self.playerCards:
            print(card)
        print()

    def createBet(self, bet):
        self.coins -= bet
        return bet

    def addCoins(self, add):
        self.coins += add
        return self.coins

    def playerHit(self):
        newCard = deck.deal(1)
        self.playerCards.append(newCard)
        return self.playerCards

    def playerDoubleD(self, playerBet):
        playerBet = playerBet * 2
        self.coins -= playerBet
        print()
        return playerBet

    def calcScore(self):
        #Takes the values from each card given
        values = []
        totalScore = 0
        aceCount = 0
        for count in range(len(self.playerCards)):
            card = self.playerCards[count]
            card = str(card)
            card = card.split("\n")
            for x in card:
                x = x.split(" ")
                for i in x:
                    if i.isdigit() == True or i in specValues:
                        values.append(i)
                        break
        for val in values:
            if val in specValues:
                val = specTens[val]
            if val == "Ace":
                aceCount += 1

            totalScore += int(val)

        if totalScore > 21 and aceCount >= 1:
            totalScore -= 10

        return totalScore


def checkWinner(dealerScore, playerScore, pot):
    if playerScore > dealerScore:
        playerWon(pot)
        sys.exit(0)
    elif dealerScore > playerScore:
        print("Dealer won:(")
        sys.exit(1)
    elif dealerScore == playerScore:
        print("Tie!")
        sys.exit(2)


def playerWon(pot):
    print("You won!")
    player.addCoins(pot * 2)
    print(f"New coins: {player}")


def dealerPlay(pot):
    #Deals 2 cards to the dealer by default
    dealerCards = deck.deal(2)

    dealerCard1, dealerCard2 = dealerCards

    #Creating a dealer object
    dealer = Dealer(dealerCard1, dealerCard2)

    dealer.Display()
    dealerScore = dealer.calcScore()

    while dealerScore <= 16:
        dealer.dealerHit()
        dealer.Display()
        dealerScore = dealer.calcScore()

    if dealerScore == 21:
        print("Dealer won :(")
        sys.exit(1)
    elif dealerScore > 21:
        playerWon(pot)
        print("Dealer went bust")
        sys.exit(0)
    else:
        checkWinner(dealerScore, player.calcScore(), pot)


#Shuffles Deck
deck.shuffle()

#Deals 2 cards to player by Default
playerCards = deck.deal(2)

#Creates an instance of the Player class and passes the cards through as arguments
player = Player(coins, playerCards)


def main():
    #Create a pot for the bet
    pot = 0

    #Show coins
    print(f"Your coins: {player}")

    #Shows cards dealt
    player.Display()

    #User enters bet
    playerBet = int(input("Enter bet: "))
    if playerBet > coins:
        print("Not enough coins")
        sys.exit(3)

    #Player's bets are added to the pot
    pot += playerBet

    #Takes away from user coins and adds to pot
    player.createBet(playerBet)

    print("ROUND STARTED\n")


    while True:

        print(f"Current Score: {player.calcScore()}")

        if player.calcScore() > 21:
            print("You have gone BUST")
            sys.exit(1)
        elif player.calcScore() == 21:
            playerWon(pot)
            sys.exit(0)

        print("Type 'v' to view your cards, type 'h' to hit, type 's' to stand, type 'd' to double down")

        userInput = input()

        match userInput:
            case "v":
                player.Display()
            case "h":
                player.playerHit()
                player.Display()
            case "d":
                player.playerHit()
                player.Display()
                print(f"New bet: {player.playerDoubleD(playerBet)}\n")
            case "s":
                dealerScore = dealerPlay(pot)
                checkWinner(dealerScore, player.calcScore(), pot)
            case _:
                print("Invalid input")


if __name__ == "__main__":
    try:
        main()

    except Exception:
        print("Error")
        sys.exit(3)

    finally:
        with open("coins.txt", "w") as file:
            file.write(str(player))
