# coding: utf-8

'''
The sum of the squares of the first ten natural numbers is,
1 ** 2 + 2 ** 2 + ... + 10 ** 2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10) ** 2 = 55 ** 2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


def sum_square(_max):
    return sum([i ** 2 for i in range(_max + 1)])


def square_sum(_max):
    return sum(range(_max + 1)) ** 2


def result(_max):
    return square_sum(_max) - sum_square(_max)


def test_sum_square():
    assert sum_square(10) == 385


def test_square_sum():
    assert square_sum(10) == 3025


def test_result():
    assert result(10) == 2640


test_sum_square()
test_square_sum()
test_result()

print result(100)
