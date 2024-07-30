def mean(args: int) -> None:
    """print the mean of a list"""
    print("mean :", sum(args) / len(args))


def median(args: int) -> None:
    """print the median of a list"""
    args.sort()
    print("median :", args[int(len(args) / 2)])


def quartile(args: int) -> None:
    """print the quartile of a list"""
    args.sort()
    print("quartile :",
          [args[int(len(args) * 0.25)], args[int(len(args) * 0.75)]])


def std(args: int) -> None:
    """print the standard deviation of a list"""
    moy = sum(args) / len(args)
    print("std :",
          pow(sum([pow(moy - arg, 2) for arg in args]) / len(args), 0.5))


def var(args: int) -> None:
    """print the standard deviation of a list"""
    moy = sum(args) / len(args)
    print("var :", sum([pow(moy - arg, 2) for arg in args]) / len(args))


def ft_dict(args: int, kwarg: any) -> None:
    try:
        assert len(args) > 0
    except AssertionError:
        print("Error")
        return
    kw_dict = {"mean": mean, "median": median,
               "quartile": quartile, "std": std, "var": var}
    [value(list(args)) for key, value in kw_dict.items() if key == kwarg]


def ft_statistics(*args: any, **kwargs: any) -> None:
    """from a list of number, print the asked statistics"""
    try:
        assert all(isinstance(a, (int)) for a in args), \
            "the list should only contain int"
    except AssertionError as msg:
        print("AssertionError:", msg)
        return
    [ft_dict(args, kw) for kw in [*kwargs.values()]]
    return
