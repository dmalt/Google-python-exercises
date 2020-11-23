import sys
from collections import Counter


def print_words(filename):
    for key in sorted(wordcount(filename)):
        print(key, '->', wordcount(filename)[key])


def wordcount(filename):
    with open(filename) as file:
        words = file.read().lower().split()
    count = Counter(words)
    return count


def print_top(filename):
    for i, j in wordcount(filename).most_common(20):
        print(i, ' -> ', j)


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print("usage: ./wordcount.py {--count | --topcount} file")
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == "--count":
        print_words(filename)
    elif option == "--topcount":
        print_top(filename)
    else:
        print("unknown option: " + option)
        sys.exit(1)


if __name__ == "__main__":
    main()
