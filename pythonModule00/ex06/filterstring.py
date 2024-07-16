from ft_filter import ft_filter
import sys


def testB(nbr: int):
    """test function for ft_filter"""
    return lambda word: True if (len(word) > nbr) else False


def main():
    try:
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
        assert all(char.isspace() or char.isalpha() for char in sys.argv[1]), \
            "AssertionError: the arguments are bad"
        assert sys.argv[2].isdigit(), "AssertionError: the arguments are bad"
    except AssertionError as msg:
        print(msg)
        return

    print(ft_filter(testB(int(sys.argv[2])), sys.argv[1].split()))


if __name__ == "__main__":
    main()
