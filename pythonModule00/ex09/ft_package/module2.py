def count_in_list(lst, str) -> int:
    """return the number of str iteration in lst"""
    nbr = 0
    for i in range(len(lst)):
        if (str == lst[i]):
            nbr += 1
    return nbr
