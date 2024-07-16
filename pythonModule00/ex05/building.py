import sys
import string


def main():
    try:
        assert len(sys.argv) < 3, "AssertionError: too many arguments"
    except AssertionError as msg:
        print(msg)
        return
    if (len(sys.argv) == 1 or sys.argv[1] is None):
        strCount = input("Enter a text:\n")
    else:
        strCount = sys.argv[1]
    print("The text contains", len(strCount), "characters.")
    print(sum(c.isupper() for c in strCount), "upper letters.")
    print(sum(c.islower() for c in strCount), "lower letters.")
    print(sum(c in string.punctuation for c in strCount), "ponctuation marks.")
    print(sum(c.isspace() for c in strCount), "spaces.")
    print(sum(c.isdigit() for c in strCount), "digits.")


if __name__ == "__main__":
    main()
