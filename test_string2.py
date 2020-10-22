from string2 import verbing, not_bad, front_back


def test_verbing():
    assert verbing("hail") == "hailing"
    assert verbing("swiming") == "swimingly"
    assert verbing("do") == "do"


def test_not_bad():
    assert not_bad("This movie is not so bad") == "This movie is good"
    assert not_bad("This dinner is not that bad!") == "This dinner is good!"
    assert not_bad("This tea is not hot") == "This tea is not hot"
    assert not_bad("It's bad yet not") == "It's bad yet not"


def test_front_back():
    assert front_back("abcd", "xy") == "abxcdy"
    assert front_back("abcde", "xyz") == "abcxydez"
    assert front_back("Kitten", "Donut") == "KitDontenut"
