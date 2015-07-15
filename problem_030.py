# coding: utf-8


'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1 ** 4 + 6 ** 4 + 3 ** 4 + 4 ** 4
8208 = 8 ** 4 + 2 ** 4 + 0 ** 4 + 8 ** 4
9474 = 9 ** 4 + 4 ** 4 + 7 ** 4 + 4 ** 4
As 1 = 1 ** 4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

# Tips
# 9 ** 5 = 59049
# 9 999 999 = 7*59049 --> au maximum on atteint: 413343


def result(power):
    _list = [i for i in range(413343) if sum([int(j) ** power for j in str(i)]) == i]
    return sum(_list) - 1  # the power of 1


if __name__ == '__main__':
    assert result(4) == 19316
    print(result(5))
