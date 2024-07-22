import sys


def main():
    size = len(sys.argv)
    if (size == 1):
        return
    try:
        assert size < 3, "AssertionError: more than one argument is provided"
        assert sys.argv[1].isdigit() or \
            (sys.argv[1] and sys.argv[1][0] == '-' and sys.argv[1][1:].isdigit()), \
            "AssertionError: argument is not an integer"
    except AssertionError as msg:
        print(msg)
        return
    nbr = int(sys.argv[1])
    if (nbr % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
