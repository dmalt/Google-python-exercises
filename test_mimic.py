from mimic import mimic_dict, print_mimic


def test_mimic():
    dict = mimic_dict("small.txt")
    print_mimic(dict, "")
