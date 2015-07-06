# coding: utf-8

'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''


''' Note: 2 different methods used'''


def memoize(f):
    memo = {(1, 1): 1}

    def helper(i, j):
        if (i, j) not in memo or not (j, i) in memo:
            memo[(i, j)] = memo[(j, i)] = f(i, j)
        return memo[i, j]

    return helper


@memoize
def result(i, j):
    if j == 0:
        return 1
    elif j == 1:
        return i + 1
    elif i == j:
        return 2 * result(i, j - 1)
    else:
        return result(i - 1, j) + result(i, j - 1)


def test_result():
    assert result(2, 2) == 6
    assert result(3, 3) == 20


print result(20, 20)


'''
Alternatively, for square problem, it can be seen as the selection of n choices
(the length of the path is always n) among n + n possibilties.
'''

from math import factorial
print factorial(2 * 20) / factorial(20) ** 2
