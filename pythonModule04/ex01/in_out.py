def square(x: int | float) -> int | float:
    """return x^2"""
    return x * x


def pow(x: int | float) -> int | float:
    """return x^x"""
    return x ** x


def outer(x: int | float, function) -> object:
    """use an inner function to keep the result of
    function(x) at each iteration"""
    def inner() -> float:
        """return function(x), with x being a variable of outer"""
        nonlocal x
        x = function(x)
        return x
    return inner
