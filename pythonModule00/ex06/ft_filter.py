def ft_filter(fct: any, iter: any) -> any:
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    return [a for a in iter if fct(a)]


def testA(iter: any) -> bool:
    """test function for ft_filter"""
    if (iter > 0):
        return True
    return False


def main():
    print(ft_filter(testA, [-5, 0, 2, 3, -1, 10]))
    print(ft_filter.__doc__)


if __name__ == "__main__":
    main()
