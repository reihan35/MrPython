def f(L):
    """ list[int] -> int """
    #M : list[list[int]]
    M = [[1, 2, 3], L]
    M[0].append(2)
    return 0

assert f([1, 2, 3]) == 0
assert f([10, 11, 12]) == 0
