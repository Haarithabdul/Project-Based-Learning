from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/10") == 10
    assert convert("99/100") == 99
    assert convert("1/100") == 1

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

def test_errors():
    with pytest.raises(ValueError):
        convert("one/two")
    with pytest.raises(ValueError):
        convert("1-2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
