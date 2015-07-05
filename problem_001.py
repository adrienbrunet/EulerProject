# coding: utf-8

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def multiple(number, _list):
    for multiple in _list:
        if number % multiple == 0:
            return True
    return False


def sum_multiple_of_3_5_6_9_below(number):
    return sum([i for i in range(number) if multiple(i, [3, 5, 6, 9])])


def test_problem1():
    assert sum_multiple_of_3_5_6_9_below(10) == 23


test_problem1()
print sum_multiple_of_3_5_6_9_below(1000)
