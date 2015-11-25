# coding: utf-8

'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''


''' Note: 2 different methods used'''


from math import factorial
from helpers import memoize_multiple_args


@memoize_multiple_args
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


def result2(i):
    '''
    Alternatively, for square problem,
    it can be seen as the selection of n choices
    (the length of the path is always n) among n + n possibilties.
    '''
    return int(factorial(2 * i) / factorial(i) ** 2)


def main():
    return result2(20)


if __name__ == '__main__':
    test_result()
    print(result(20, 20))
    print(result2(20))
    # 137846528820 in 1.4usec
