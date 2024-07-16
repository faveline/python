import sys


def main():
    try:
        assert len(sys.argv) == 2, "AssertionError: the arguments are bad"
        assert all(char.isspace() or char.isalnum() for char in sys.argv[1]), \
            "AssertionError: the arguments are bad"
    except AssertionError as msg:
        print(msg)
        return
    NESTED_MORSE = {
        " ": "/ ", "A": ".- ", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--",
        "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----",
        "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
        "7": "--...", "8": "---..", "9": "----."
    }
    # [print(NESTED_MORSE[code.upper()], end=" ") for code in sys.argv[1]]
    for i in range(len(sys.argv[1]) - 1):
        print(NESTED_MORSE[sys.argv[1][i].upper()], end=" ")
    print(NESTED_MORSE[sys.argv[1][len(sys.argv[1]) - 1].upper()])


if __name__ == "__main__":
    main()
