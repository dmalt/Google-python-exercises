from list2 import remove_adjacent, linear_merge


def test_remove_adjacent():
    assert remove_adjacent([1, 2, 2, 3]) == [1, 2, 3]
    assert remove_adjacent([2, 2, 3, 3, 3]) == [2, 3]
    assert remove_adjacent([]) == []


def test_linear_merge():
    assert linear_merge(["aa", "xx", "zz"], ["bb", "cc"]) == [
        "aa",
        "bb",
        "cc",
        "xx",
        "zz",
    ]

    assert linear_merge(["aa", "xx"], ["bb", "cc", "zz"]) == [
        "aa",
        "bb",
        "cc",
        "xx",
        "zz",
    ]

    assert linear_merge(["aa", "aa"], ["aa", "bb", "bb"]) == [
        "aa",
        "aa",
        "aa",
        "bb",
        "bb",
    ]
