def callLimit(limit: int):
    """wrappers decorator to ensure that a function
    can't be call more than limit times"""
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print("Error:", function, "call too many times.")
                return
        return limit_function
    return callLimiter
