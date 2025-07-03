from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0


def test_h():
    assert value("Hi") == 20
    assert value("Hey") == 20


def test_no_h():
    assert value("Greetings") == 100
    assert value("What's up?") == 100
