from project import Player, Dealer, checkWinner, playerWon, dealerPlay
from pydealer import Deck, Card
import pytest

deck = Deck()


playerCards1 =  [Card("Ace", "Spades"), Card("7", "Hearts")]
playerCards2 =  [Card("Queen", "Hearts"), Card("King", "Diamonds")]
playerCards3 =  [Card("4", "Hearts"), Card("5", "Clubs")]
playerCards4 =  [Card("10", "Spades"), Card("Ace", "Hearts")]

dealerCards1 =  [Card("Ace", "Spades"), Card("7", "Hearts")]
dealerCards2 =  [Card("Queen", "Hearts"), Card("King", "Diamonds")]
dealerCards3 =  [Card("4", "Hearts"), Card("5", "Clubs")]
dealerCards4 =  [Card("10", "Spades"), Card("Ace", "Hearts")]


def test_playerCoins():
    player = Player(100, playerCards1)

    assert player.addCoins(10) == 110
    player.createBet(10)
    assert player.coins == 100
    assert player.addCoins(50) == 150
    player.createBet(50)
    assert player.coins == 100


def test_playerDoubleD():
    player = Player(100, playerCards1)

    assert player.playerDoubleD(10) == 20
    assert player.playerDoubleD(30) == 60
    assert player.playerDoubleD(100) == 200


def test_playerCalcScore():
    player = Player(100, *playerCards1)
    assert player.calcScore() == 18

    player = Player(100, *playerCards2)
    assert player.calcScore() == 20

    player = Player(100, *playerCards3)
    assert player.calcScore() == 9


def test_playerDisplay():
    player = Player(100, playerCards1)
    assert player.Display() == print(playerCards1)

    player = Player(100, playerCards2)
    assert player.Display() == print(playerCards2)

    player = Player(100, playerCards3)
    assert player.Display() == print(playerCards3)


def test_dealerDisplay():
    dealer = Dealer(*dealerCards1)
    assert dealer.Display() == print(dealerCards1)

    dealer = Dealer(*dealerCards2)
    assert dealer.Display() == print(dealerCards1)

    dealer = Dealer(*dealerCards3)
    assert dealer.Display() == print(dealerCards1)


def test_dealerCalcScore():
    dealer = Dealer(*dealerCards1)
    assert dealer.calcScore() == 18

    dealer = Dealer(*dealerCards2)
    assert dealer.calcScore() == 20

    dealer = Dealer(*dealerCards3)
    assert dealer.calcScore() == 9


def test_checkWinner():
    #Exit code 0 for player win, 1 for dealer win, 2 for tie, 3 for error

    player = Player(100, playerCards1)
    with pytest.raises(SystemExit) as exc_info:
        checkWinner(18, 20, 10)
    assert exc_info.value.code == 0

    with pytest.raises(SystemExit) as exc_info:
        checkWinner(20, 18, 10)
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        checkWinner(7, 7, 10)
    assert exc_info.value.code == 2


def test_playerWon():
    player = Player(100, playerCards1)
    assert playerWon(10) == print("New coins: 120")

    player = Player(100, playerCards2)
    assert playerWon(5) == print("New coins: 110")

    player = Player(100, playerCards1)
    assert playerWon(20) == print("New coins: 140")


def mock_deck_deal(n):
    # Always return the same cards for consistency
    return ["Ace of Spades", "King of Hearts"]

# Mocking the `Dealer` class to always return 21 for dealer's score
class MockDealer:
    def __init__(self, card1, card2):
        pass

    def Display(self):
        pass  # Skip actual display for the test

    def calcScore(self):
        return 21  # Dealer always wins with 21

    def dealerHit(self):
        pass  # No need to hit since score is already 21

# Test function to test dealerPlay with mocked behaviors
def test_dealerPlay():
    import project  # Replace `blackjack` with the module where dealerPlay is defined

    # Save the original references
    original_deck = project.deck
    original_Dealer = project.Dealer

    try:
        # Override the `deck.deal` method to return mocked cards
        project.deck.deal = mock_deck_deal

        # Override the `Dealer` class to use the mock
        project.Dealer = MockDealer

        # Call dealerPlay and assert that it raises SystemExit(1) when dealer wins
        with pytest.raises(SystemExit) as exc_info:
            project.dealerPlay(10)

        # Ensure the exit code is 1, indicating the dealer won
        assert exc_info.value.code == 1

    finally:
        # Restore the original references
        project.deck = original_deck
        project.Dealer = original_Dealer
