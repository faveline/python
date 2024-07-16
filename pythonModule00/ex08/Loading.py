import os


def ft_tqdm(lst: range) -> None:
    """Decorate an iterable object, returning an iterator which acts exactly
like the original iterable, but prints a dynamically updating
progressbar every time a value is requested."""
    cpt = 0
    sizeTer = os.get_terminal_size()[0] - 43
    while (cpt < len(lst)):
        yield cpt
        cpt += 1
        ptg = int(cpt / len(lst) * 100)
        if (cpt != len(lst)):
            print(" ",  end="")
        if (ptg < 10):
            print(" ",  end="")
        print(ptg, "%|[", end="", sep="")
        i = 0
        while (i / sizeTer < cpt / len(lst)):
            i += 1
            print("=", end="")
        print(">", end="")
        while (i < sizeTer):
            i += 1
            print(" ", end="")
        print("]| ", cpt, "/", len(lst), end="\r", sep="")
