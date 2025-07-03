from seasons import checkDateFormat, calcAgeMinutes

def test_checkDateFormat():
    assert checkDateFormat("2006-11-11") == "2006-11-11"

def test_calcAgeMinutes():
    assert calcAgeMinutes("2006-11-11") == 9534240
